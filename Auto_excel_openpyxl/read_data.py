import openpyxl as xl
import re


WS_WORKSHEET = "作業シート"
#フォーマットExcelの読み込み
wb = xl.load_workbook('ToolBox\Auto_excel_openpyxl\ユーザ管理.xlsx')
def read_data():
    ws_work = wb[WS_WORKSHEET]

    data_list = []   
    for row in ws_work.iter_rows(min_row=3, values_only=True):
        # print(row[1])
        if row[1] is not None:
            # 正規表現を使用して "@" の前の部分を抽出
            match = re.match(r'([^@]+)@', row[2])
            if match:
                user_name = match.group(1)
            user_data = {
                "user_name": user_name,
                "group_name": row[3]
            }
            data_list.append(user_data)   
    return data_list


data_list = read_data()
print(data_list)
# [{'user_name': 'midori.kikuchi', 'group_name': 'BAP'}]
