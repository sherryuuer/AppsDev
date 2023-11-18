from read_data import *
from write_data import *
from manage_user import *

WS_WORKSHEET = "作業シート"
WS_MANAGERSHEET = "管理シート"
WS_DELETE = "削除済み"

input_ope = input()  # delete, create
name_list = read_data()
if input_ope == 'create': 
    target_sheet = WS_MANAGERSHEET
    # success = True/False
    result = create_user(name_list)
    if result == True:
        write_data(target_sheet)
elif input_ope == 'delete':
    target_sheet = WS_DELETE
    delete_user(name_list)

else:
    print('createまたはdeleteという文字を入力してください。')

