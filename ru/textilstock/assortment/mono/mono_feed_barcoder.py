import pandas as pd

WILDBERRIES_MONO_TEMPLATE_XLS = '/home/stani/PycharmProjects/texstock/ru/textilstock/assortment' \
                                '/mono/wildberries_barcode_template.xls'


def write_data_to_csv(data_frame, output_file_csv):
    s = data_frame.to_csv(index=False)
    with open(output_file_csv, "w") as text_file:
        text_file.write(s)


def generate_handbook_and_template(monofeed_xlsx, nomen_xlsx, barcodes_list_xlsx,
                                   handbook_out_csv, template_out_xlsx):
    mono_feed_df = pd.read_excel(monofeed_xlsx)

    wild_nomen_dataset = pd.read_excel(nomen_xlsx, skiprows=2)

    skipped = mono_feed_df.join(wild_nomen_dataset.set_index('Артикул поставщика'), on='артикул',
                                how='left')
    skipped = skipped[skipped['Баркод'].isnull()]
    if len(skipped) > 0:
        print("Баркод NOT exist in " + wild_nomen_dataset)
        print(skipped)

    nomenclatured_df = mono_feed_df.join(wild_nomen_dataset.set_index('Артикул поставщика'), on='артикул')

    wildberries_barcodes_list = pd.read_excel(barcodes_list_xlsx)
    nomenclatured_df['box_barcode'] = wildberries_barcodes_list
    nomenclatured_df = nomenclatured_df[['box_barcode', 'номер короба', 'артикул', 'Кол-во', 'Баркод']]

    write_data_to_csv(nomenclatured_df, handbook_out_csv)

    wild_template_df = pd.read_excel(WILDBERRIES_MONO_TEMPLATE_XLS)

    wild_template_df['ШК короб единицы'] = nomenclatured_df['box_barcode']
    wild_template_df['ШК eдиницы'] = nomenclatured_df['Баркод']
    wild_template_df['Кол-во'] = nomenclatured_df['Кол-во']
    wild_template_df['ШК короба'] = nomenclatured_df['box_barcode']
    wild_template_df['Кол-во коробок'] = 1

    writer = pd.ExcelWriter(template_out_xlsx)
    wild_template_df.to_excel(writer, 'Лист1', index=False)
    writer.save()

# generate_handbook_and_template('mono_feed.xlsx', 'nomen.xlsx', 'wildberries_barcodes_list.xlsx',
#                                'out.csv', 'output.xlsx')

# generate_handbook_and_template('monofeed1.xlsx', '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-05-22T223634.988.xlsx',
#                                'wildberries_barcodes_list.xlsx',
#                                'out.csv', 'output.xlsx')