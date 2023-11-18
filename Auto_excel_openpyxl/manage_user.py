import boto3


iam = boto3.client('iam')
pw = 'Passw0rd!'

def create_user(usernames: list):
    """
    ユーザーの追加
    ----------
    usernames : ユーザー名のリスト
    """
    flag = True
    for username in usernames:
        try:
            response = iam.create_login_profile(
                UserName=username['user_name'],
                Password=pw,
                PasswordResetRequired=True
            )
        except Exception as e:
            flag = False
            # エラーが発生した場合の処理をここに書きます
            print(f"ユーザー {username['user_name']} の追加中にエラーが発生しました: {str(e)}")
    # return flag
    return True

# def update_user(usernames:list):
#     """
#     ユーザー名の更新
#     ----------
#     oldname : 旧ユーザー名
#     newname : 新ユーザー名
#     """
#     for oldname in oldnames,:
#         response = iam.update_user(
#             UserName=oldname,
#             NewUserName=newname
#         )
#     return

def delete_user(usernames:list):
    """
    ユーザーの削除
    ----------
    usernames : ユーザー名のリスト
    """
    flag = True
    for username in usernames:
        try:
            response = iam.delete_user(
                UserName=username['user_name']
            )
        except Exception as e:
            flag = False
            # エラーが発生した場合の処理をここに書きます
            print(f"ユーザー {username['user_name']} の削除中にエラーが発生しました: {str(e)}")
    
    # return flag
    return True

def add_group(usernames:list):
    """
    ユーザーをグループへ追加
    ----------
    usernames : ユーザー名のリスト
    """
    flag = True
    for username in usernames:
        try:
            response = iam.add_user_to_group(
                GroupName=username['group_name'],
                UserName=username['user_name']
            )
        except Exception as e:
            flag = False
            # エラーが発生した場合の処理をここに書きます
            print(f"ユーザー {username['user_name']} をグループ {username['group_name']}へ追加中にエラーが発生しました: {str(e)}")
    return flag

# def remove_group(username:str,groupname:str):
#     """
#     ユーザーをグループから除外
#     ----------
#     username : ユーザー名
#     """
#     response = iam.remove_user_from_group(
#         GroupName=groupname,
#         UserName=username
#     )
#     return

# def delete_group(username:str):
#     """
#     グループの削除
#     ----------
#     username : ユーザー名
#     """
#     response = client.delete_user(
#     UserName='string'
# )
#     return

# def add_group(username:str):
#     """
#     グループへ追加
#     ----------
#     username : ユーザー名
#     """
#     return
