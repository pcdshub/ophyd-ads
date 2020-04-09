# Install the package
$PYTHON setup.py install --single-version-externally-managed --record=record.txt

# Create auxiliary dirs
mkdir -p $PREFIX/etc/conda/activate.d
mkdir -p $PREFIX/etc/conda/deactivate.d
mkdir -p $PREFIX/etc/ophyd-ads

# Create auxiliary vars
ACTIVATE=$PREFIX/etc/conda/activate.d/ophyd-ads
DEACTIVATE=$PREFIX/etc/conda/deactivate.d/ophyd-ads

ETC_PATH=$PREFIX/etc/ophyd-ads
DESIGNER_PATH=$ETC_PATH/designer

DESIGNER_PLUGIN=$DESIGNER_PATH/ophyd_ads_designer_plugin.py
DATA_PLUGIN=$ETC_PATH/ophyd_ads_data_plugin.py

echo "from ophyd_ads.pydm import *" >> $DESIGNER_PLUGIN
echo "from ophyd_ads.pydm import *" >> $DATA_PLUGIN

echo "export PYQTDESIGNERPATH=\$CONDA_PREFIX/etc/ophyd-ads/designer:\$PYQTDESIGNERPATH" >> $ACTIVATE.sh
echo "export PYDM_DATA_PLUGINS_PATH=\$CONDA_PREFIX/etc/ophyd-ads:\$PYDM_DATA_PLUGINS_PATH" >> $ACTIVATE.sh
echo "unset PYQTDESIGNERPATH" >> $DEACTIVATE.sh

echo '@ECHO OFF' >> $ACTIVATE.bat
echo 'IF "%PYQTDESIGNERPATH%" == "" (' >> $ACTIVATE.bat
echo 'set PYQTDESIGNERPATH=%CONDA_PREFIX%\etc\ophyd-ads\designer' >> $ACTIVATE.bat
echo ')ELSE (' >> $ACTIVATE.bat
echo 'set PYQTDESIGNERPATH=%CONDA_PREFIX%\etc\ophyd-ads\designer;%PYQTDESIGNERPATH%' >> $ACTIVATE.bat
echo ')' >> $ACTIVATE.bat

echo 'IF "%PYDM_DATA_PLUGINS_PATH%" == "" (' >> $ACTIVATE.bat
echo 'set PYDM_DATA_PLUGINS_PATH=%CONDA_PREFIX%\etc\ophyd-ads' >> $ACTIVATE.bat
echo ')ELSE (' >> $ACTIVATE.bat
echo 'set PYDM_DATA_PLUGINS_PATH=%CONDA_PREFIX%\etc\ophyd-ads\;%PYDM_DATA_PLUGINS_PATH%' >> $ACTIVATE.bat
echo ')' >> $ACTIVATE.bat

unset DESIGNER_PLUGIN
unset ACTIVATE
unset DEACTIVATE
