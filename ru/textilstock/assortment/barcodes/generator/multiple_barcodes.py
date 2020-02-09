import csv

article_multiple_factor_dict = dict()
DEFAULT_MULTIPLE_FACTOR = 8
need_multiple = 1
default_article_factor = 2

with open("/home/stani/PycharmProjects/texstock/ru/"
          "textilstock/assortment/barcodes/generator/multiple_barcode_factor.csv", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        article_multiple_factor_dict[row[0]] = int(row[1])


def calc_repeat_dict_count(row, multiple_factor):
    rc = int(row['cnt'])
    article = row['Артикул ИМТ']

    article_factor = default_article_factor
    if article in article_multiple_factor_dict:
        article_factor = article_multiple_factor_dict[article]
    rc = rc * article_factor
    if need_multiple == 1:
        rc = (int(rc / multiple_factor)) * multiple_factor + min(rc % multiple_factor, 1) * multiple_factor
    return rc


def write_barcode_csv_for_jasper(rows, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['cnt', 'repeat_count', 'Артикул ИМТ', 'Бренд', 'Предмет',
                      'Артикул Цвета', 'Баркод']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            rc = row['repeat_count']
            for counter in range(rc):
                writer.writerow({'cnt': row['cnt'],
                                 'repeat_count': row['repeat_count'],
                                 'Артикул ИМТ': row['Артикул ИМТ'],
                                 'Бренд': row['Бренд'],
                                 'Предмет': row['Предмет'],
                                 'Артикул Цвета': row['Артикул Цвета'],
                                 'Баркод': row['Баркод']
                                 })


def gen_and_write_barcodes(nomenclature_with_count_file_csv, out_file_csv, multiple_factor = DEFAULT_MULTIPLE_FACTOR):
    with open(nomenclature_with_count_file_csv, newline='') as f:
        reader = csv.DictReader(f)
        result_rows = []
        for row in reader:
            ret_count = calc_repeat_dict_count(row, multiple_factor)
            row['repeat_count'] = ret_count
            result_rows.append(row)
        write_barcode_csv_for_jasper(result_rows, out_file_csv)

