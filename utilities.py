import xlwt
import io
import csv
import json

date_format = xlwt.XFStyle()
date_format.num_format_str = 'dd/mm/yyyy'

styles = { 
    'title' :  xlwt.easyxf('pattern: pattern solid, fore_colour aqua; font: height 250; align: wrap on, vert center, horiz center; borders: left thin, right thin, top thin, bottom thin'),
    'regular' : xlwt.easyxf(' borders: left thin, right thin, top thin, bottom thin'),
    'sum' : xlwt.easyxf('font: bold on; borders: left thin, right thin, top thin, bottom thin'),
    'date': xlwt.easyxf(' borders: left thin, right thin, top thin, bottom thin')
}

def get_price_info():
    f = open('price_data.json')
    data = json.load(f)
    f.close()
    return data


def export_to_excel(hot_data, htitle):
    file_excel = io.BytesIO()
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet1 = workbook.add_sheet('Hot Drinks')

    for col_num, cell_data in enumerate(htitle) :
        sheet1.write(0, col_num, cell_data, style=styles['title'])

    for row_num, row_data in enumerate(hot_data, 1):
        for col_num, cell_data in enumerate(row_data) :
            if col_num == 2:
                sheet1.write(row_num, col_num, cell_data, date_format)
            elif col_num in [31, 32, 33]:
                sheet1.write(row_num, col_num, cell_data, style=styles['sum'])
            else:
                sheet1.write(row_num, col_num, cell_data, style=styles['regular'])

    workbook.save(file_excel)
    file_excel.seek(0)
    return file_excel 


def export_to_csv(hot_data):
    proxy = io.StringIO()
    
    writer = csv.writer(proxy)
    for row_data in hot_data:
        writer.writerow(row_data)
    
    mem = io.BytesIO()
    mem.write(proxy.getvalue().encode())
    mem.seek(0)
    proxy.close()
    return mem
