import csv

from ru.textilstock.assortment.djama.OrderDetail import OrderDetail
from ru.textilstock.core.xls.XlsUtils import open_xls_as_xlsx


def is_detailzationHeader(row):
    return row[0].value =='№' and row[2].value == 'Артикул'

def make_djama_detalization_tmp(in_filename, out_filename):
    order_details = parse_order_detalization(in_filename)
    write_order_details_to_csv(order_details, out_filename)


def write_order_details_to_csv(order_details, out_filename):
    f = open(out_filename, 'w')
    with f:
        fnames = ['article', 'count', 'price']
        writer = csv.DictWriter(f, fieldnames=fnames)
        writer.writeheader()
        for detail in order_details:
            writer.writerow({'article': detail.article, 'count': detail.count, 'price': detail.price})
        f.close()


def parse_order_detalization(filename):
    wb = open_xls_as_xlsx(filename)
    ws = wb.get_sheet_by_name('Sheet')
    was_detalization_header = False
    order_details = []
    for row in ws.iter_rows():
        if was_detalization_header:
            if row[0].value == '':
                break
            order_details.append(OrderDetail(row[6].value, int(row[23].value), row[28].value))

        for cell in row:
            if was_detalization_header:
                print(cell.value, end=' ')

        was_detalization_header = was_detalization_header or is_detailzationHeader(row)
    return order_details


#make_djama_detalization_tmp('polot.xls', 'order_details_tmp.csv')
