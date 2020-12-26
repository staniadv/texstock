import os

import pandas as pd

from ru.textilstock.assortment.barcodes.generator.multiple_barcodes import gen_and_write_barcodes
from ru.textilstock.assortment.djama.xls.order_detalization_parser import make_djama_detalization_tmp

from ru.textilstock.assortment.djama.xls.join_detail_and_nomen import join_detail_with_nomen_and_write

detalization_tmp_file = 'detalization.tmp.csv'
detalization_with_nomen_tmp_file = 'details_with_nomen.tmp.csv'

REMOVE_TMP_FILES = True


def generate_barcodes_template(detalization_file_csv, nomen_file_xlsx, barcodes_file_csv,
                               multiple_factor_factor, extra_barcode_count = 1):
    try:
        os.remove(barcodes_file_csv)
    except OSError:
        pass

    make_djama_detalization_tmp(detalization_file_csv, detalization_tmp_file)
    join_detail_with_nomen_and_write(detalization_tmp_file, nomen_file_xlsx,
                                     detalization_with_nomen_tmp_file)
    gen_and_write_barcodes(detalization_with_nomen_tmp_file, barcodes_file_csv, multiple_factor_factor,
                           extra_barcode_count)

    if REMOVE_TMP_FILES:
        try:
            os.remove(detalization_tmp_file)
            os.remove(detalization_with_nomen_tmp_file)
        except OSError:
            pass


def repeat_rows(in_file_name, out_file_name):
    df = pd.read_csv(in_file_name)
    # Create an empty list
    row_list = []
    # Iterate over each row
    for index, rows in df.iterrows():
        # Create list for the current row
        rc = rows['cnt'] + 2
        for counter in range(rc):
            row_list.append(rows)
    df2 = pd.DataFrame(row_list)
    df2.to_csv(out_file_name, index=False)
