import logging

from qtpy import QtCore, QtWidgets

from ads_pcds import Symbol, get_connection, make_address, parse_address
from ads_pcds.ads import enumerate_plc_symbols
from pydm.data_plugins.plugin import (BaseParameterEditor, PyDMConnection,
                                      PyDMPlugin)
from pydm.utilities.channel import parse_channel_config

logger = logging.getLogger(__name__)


class SymbolForPydm(Symbol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = {'CONNECTION': False}

    def value_updated(self, timestamp, value):
        self.data.update(**{
            'CONNECTION': True,
            'VALUE': value,
            'WRITE_ACCESS': True,
            # 'TIMESTAMP': time.time(),
        })
        self.pydm_connection.send_new_value(self.data)

    def set_connection(self, pydm_connection):
        self.pydm_connection = pydm_connection
        self.start()


class Connection(PyDMConnection):
    def __init__(self, channel, address, protocol=None, parent=None):
        super().__init__(channel, address, protocol, parent)
        conn = parse_channel_config(address, force_dict=True)['connection']
        address = conn.get('parameters', {}).get('address')

        self.address = parse_address(address)
        self.ip_address = self.address['ip_address']
        self.ams_id = self.address['ams_id']
        self.port = self.address['port']
        self.poll_rate = self.address['poll_rate']
        self.plc = get_connection(ip_address=self.ip_address,
                                  ams_id=self.ams_id, port=self.port)

        self.symbol_name = self.address['symbol']
        self.symbol = self.plc.get_symbol(self.symbol_name, self.poll_rate,
                                          cls=SymbolForPydm)
        self.symbol.set_connection(self)

    def send_new_value(self, payload):
        self.data.update(payload)
        self.send_to_channel()

    def receive_from_channel(self, payload):
        value = payload['VALUE']
        self.symbol.write(value)

    def close(self):
        print('connection closed', self.symbol_name)
        self.plc.clear_symbol(self.symbol_name)
        super().close()


class AdsBrowser(QtWidgets.QDialog):
    symbol_selected = QtCore.Signal(dict)

    def __init__(self, ip_address, ams_id, port, *, parent=None):
        super().__init__(parent=parent)
        self.setSizeGripEnabled(True)

        self.filter_widget = QtWidgets.QLineEdit()
        self.ip_widget = QtWidgets.QLineEdit(ip_address or '')
        self.ams_id_widget = QtWidgets.QLineEdit(ams_id or '')
        self.port_widget = QtWidgets.QLineEdit(str(port))
        self.symbol_table = QtWidgets.QTableWidget()
        self.symbol_table.setSortingEnabled(True)

        self.update_widget = QtWidgets.QPushButton('Update')
        self.select_widget = QtWidgets.QPushButton('Select')

        self.layout = QtWidgets.QFormLayout()

        ip_layout = QtWidgets.QHBoxLayout()
        ip_layout.addWidget(self.ip_widget)
        ip_layout.addWidget(self.ams_id_widget)
        self.layout.addRow('IP Address / AMS ID', ip_layout)

        self.layout.addRow('Port', self.port_widget)
        self.layout.addRow(self.update_widget)

        self.layout.addRow(self.symbol_table)
        self.layout.addRow('Filter', self.filter_widget)
        self.layout.addRow(self.select_widget)
        self.setLayout(self.layout)

        self.update_widget.clicked.connect(self.update_symbols)
        self.filter_widget.textChanged.connect(self.apply_filter)

        def emit_selected():
            row = self.symbol_table.currentRow()
            self.symbol_selected.emit(
                dict(symbol=self.symbol_table.item(row, 0).text(),
                     type=self.symbol_table.item(row, 1).text(),
                     comment=self.symbol_table.item(row, 2).text(),
                     )
            )
            self.close()

        self.select_widget.clicked.connect(emit_selected)
        self.update_symbols()

    def apply_filter(self):
        # TODO: QTableView + QtCore.QSortFilterProxyModel
        rows = {item.row() for item in
                self.symbol_table.findItems(self.filter_widget.text(),
                                            QtCore.Qt.MatchContains)
                }
        for row in range(self.symbol_table.rowCount()):
            self.symbol_table.setRowHidden(row, row not in rows)

    def update_symbols(self):
        def update_symbols():
            try:
                self.plc = get_connection(self.ip_widget.text(),
                                          self.ams_id_widget.text(),
                                          int(self.port_widget.text())
                                          )
                self.ads = self.plc.ads
                should_close = not self.ads.is_open
                self.ads.open()
                self.symbols = enumerate_plc_symbols(self.ads)
                self.update_symbol_table(self.symbols)
                if should_close:
                    self.ads.close()
            except Exception:
                logger.exception('Symbol update failed')

        self._update_thread = QtCore.QThread()
        self._update_thread.started.connect(update_symbols)
        self._update_thread.start()

    def update_symbol_table(self, symbols):
        self.symbol_table.clear()
        self.symbol_table.setRowCount(len(symbols))
        table = self.symbol_table
        self.symbol_table.setColumnCount(3)
        table.setHorizontalHeaderLabels(['Name', 'Type', 'Comment'])

        for row, (symbol_name, info) in enumerate(symbols.items()):
            table.setItem(row, 0, QtWidgets.QTableWidgetItem(symbol_name))
            table.setItem(row, 1, QtWidgets.QTableWidgetItem(info['type']))
            table.setItem(row, 2, QtWidgets.QTableWidgetItem(info['comment']))

        table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        table.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeToContents)
        table.horizontalHeader().setSortIndicatorShown(True)


class AdsParameterEditor(BaseParameterEditor):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QtWidgets.QFormLayout()
        self.setLayout(self.layout)

        self.layout.setFieldGrowthPolicy(
            QtWidgets.QFormLayout.AllNonFixedFieldsGrow
        )

        self.uri_widget = None
        self.ip_widget = None
        self.ams_id_widget = None
        self.port_widget = None
        self.poll_rate_widget = None
        self.symbol_widget = None

        for label, widget_name, cls in [
                ('URI', 'uri_widget', QtWidgets.QLineEdit),
                ('IP address', 'ip_widget', QtWidgets.QLineEdit),
                ('AMS ID', 'ams_id_widget', QtWidgets.QLineEdit),
                ('Symbol', 'symbol_widget', QtWidgets.QLineEdit),
                ('Port', 'port_widget', QtWidgets.QLineEdit),
                ('Poll rate', 'poll_rate_widget', QtWidgets.QLineEdit),
                ]:
            widget = cls(self)
            setattr(self, widget_name, widget)
            callback = getattr(self, f'{widget_name}_changed', None)
            if callback is not None:
                widget.editingFinished.connect(callback)

            self.layout.addRow(QtWidgets.QLabel(label), widget)

        self.update_widget = QtWidgets.QPushButton('Update URI')
        self.update_widget.clicked.connect(self._update_uri)

        self.browse_widget = QtWidgets.QPushButton('Browse')
        self.browse_widget.clicked.connect(self._browse)

        self.layout.addRow(self.browse_widget, self.update_widget)

    def _browse(self):
        def selected(info):
            logger.info('Selected: %s', info)
            self.symbol_widget.setText(info['symbol'])
            self._update_uri()

        try:
            info = self.address_info
            self.browser = AdsBrowser(info['ip_address'], info['ams_id'],
                                      info['port'], parent=self)
            self.browser.symbol_selected.connect(selected)
            self.browser.show()
        except Exception:
            logger.exception('Unable to show browser :(')
            return

    def _update_uri(self):
        ip_address = self.ip_widget.text() or None
        ams_id = self.ams_id_widget.text() or None
        port = self.port_widget.text() or None
        symbol = self.symbol_widget.text() or None
        poll_rate = self.poll_rate_widget.text() or None
        try:
            address = make_address(ip_address, ams_id, port=port,
                                   symbol=symbol, poll_rate=poll_rate)
        except Exception:
            logger.exception('Unable to make address')
            return

        self.uri_widget.setText(address[6:])

    @property
    def address_info(self):
        text = self.uri_widget.text()
        return parse_address(text, allow_macros=True)

    def uri_widget_changed(self):
        try:
            info = self.address_info
        except Exception:
            logger.exception('Unable to parse address')
            return

        self.ip_widget.setText(info['ip_address'] or '')
        self.ams_id_widget.setText(info['ams_id'] or '')
        self.port_widget.setText(str(info['port'] or ''))
        self.symbol_widget.setText(str(info['symbol'] or ''))
        self.poll_rate_widget.setText(str(info['poll_rate'] or ''))

    @property
    def parameters(self):
        return {'address': self.uri_widget.text()}

    @parameters.setter
    def parameters(self, params):
        address = params.get('address', '')
        self.uri_widget.setText(address)
        self.uri_widget_changed()

    def validate(self):
        return True, ''

    def clear(self):
        self.uri_widget.setText('')

    @staticmethod
    def get_repr(parameters):
        return parameters.get('address', '')


class ADSPlugin(PyDMPlugin):
    protocol = 'ads'
    connection_class = Connection
    param_editor = AdsParameterEditor
