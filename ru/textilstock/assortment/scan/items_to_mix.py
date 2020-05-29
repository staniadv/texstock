import pandas as pd


def items_to_mix(scan_df, nomen_file, supply_number):
    scan_df = scan_df[scan_df['Баркод'].notnull()]
    scan_df = scan_df.astype({'Баркод': 'int64'})

    scan_groupped = scan_df.groupby(["номер короба", "Баркод"]).size().to_frame('count')

    #scan_groupped.to_csv('3.csv')
    scan_groupped = scan_groupped.reset_index()

    nomen_df = pd.read_excel(nomen_file, skiprows=2)

    grp_with_nomen = pd.merge(scan_groupped, nomen_df,
                              how='left', left_on=['Баркод'],
                              right_on=['Баркод']
                              )
    grp_with_nomen = pd.DataFrame(data=grp_with_nomen, columns=['номер короба', 'Артикул поставщика', 'count',
                                                                'Баркод', 'Бренд', 'Предмет'])
    max_box_count = grp_with_nomen['номер короба'].max()

    grp_with_nomen['count'] = grp_with_nomen['count'] / 2
    grp_with_nomen = grp_with_nomen.rename(columns={"count": "количество", "Артикул поставщика": "артикул"})
    grp_with_nomen['едизм'] = "шт."
    grp_with_nomen['порядковый номер'] = grp_with_nomen.groupby(['номер короба']).cumcount() + 1
    grp_with_nomen['всего коробов'] = max_box_count
    grp_with_nomen['код груза'] = supply_number
    grp_with_nomen = grp_with_nomen.sort_values(by=['номер короба', 'порядковый номер'])


    grp_with_nomen.to_csv('output/' + str(supply_number) + '.csv')
