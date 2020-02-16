import pandas as pd
from ru.textilstock.core.xls.XlsUtils import open_xls_as_xlsx


def parse_djama_stocks(filename):
    wb = open_xls_as_xlsx(filename)
    ws = wb.get_sheet_by_name('Sheet')
    result = []
    for row in ws.iter_rows():
        if "(itu)" in row[0].value:
            count = 0
            if str(row[1].value) != "":
                count = int(row[1].value)
            result.append([str(row[0].value), count])
            #print(str(row[0].value) + " " + str(count))
    return pd.DataFrame(result, columns=['article', 'count'], dtype=int)
