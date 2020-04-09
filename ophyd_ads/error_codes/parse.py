import subprocess

import bs4 as bs
import pandas as pd

ERROR_CODE_FILES = '''
infosys.beckhoff.com/content/1033/tcncerrcode2/63050395296338187.html
infosys.beckhoff.com/content/1033/tcncerrcode2/54043197050248075.html
infosys.beckhoff.com/content/1033/tcncerrcode2/36028797532093707.html
infosys.beckhoff.com/content/1033/tcncerrcode2/27021598472560011.html
infosys.beckhoff.com/content/1033/tcncerrcode2/18014399022626059.html
infosys.beckhoff.com/content/1033/tcncerrcode2/18014399022608139.html
infosys.beckhoff.com/content/1033/tcncerrcode2/9007200776586379.html
infosys.beckhoff.com/content/1033/tcncerrcode2/9007199767874315.html
infosys.beckhoff.com/content/1033/tcncerrcode2/513147659.html
infosys.beckhoff.com/content/1033/tcncerrcode2/513140491.html
infosys.beckhoff.com/content/1033/tcncerrcode2/513136907.html
infosys.beckhoff.com/content/1033/tcncerrcode2/513122571.html
'''.strip().splitlines()


def generate_errors():
    info = {}

    for fn in ERROR_CODE_FILES:
        with open(fn, 'rt') as f:
            source = f.read()

        soup = bs.BeautifulSoup(source, 'lxml')

        title = soup.find('title').text.strip()
        info[title] = []

        for table in soup.find_all('table'):
            for tr in table.find_all('tr'):
                td = tr.find_all('td')
                row = [tr.text.strip() for tr in td]
                if len(row) == 4:
                    if row[0] in ('CodeHex', ''):
                        continue
                    row[1] = title

                    if '-' in row[0]:
                        low, high = row[0].split('-')
                        for i in range(int(low, 16), int(high, 16) + 1):
                            row = list(row)
                            row[0] = i
                            info[title].append(row)
                    else:
                        row[0] = int(row[0], 16)
                        info[title].append(row)

        info[title] = pd.DataFrame(
            info[title],
            columns=['Code', 'Category', 'Error type', 'Description']
        )

    df = pd.concat((df for df in info.values()), ignore_index=True)

    with open('errors.py', 'wt') as f:
        print('errors = {}'.format(df.set_index('Code').to_dict('index')),
              file=f)

    subprocess.check_output(['black', 'errors.py'])


if __name__ == '__main__':
    generate_errors()
