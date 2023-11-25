import requests
import hashlib
import sys


def request_api_data(query_char):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    response = requests.get(url=url)
    if response.status_code != 200:
        raise RuntimeError(f"Error {response.status_code}, check it again.")
    return response


def count_leaks(response, tail):
    res = (line.split(':') for line in response.text.splitlines())
    # print(res)  # generator
    for hash, count in res:
        if hash == tail:
            return count
    return 0


def pwned_api_check(password):
    # check pw if it exsits in api response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    send_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(send_char)
    print(response)
    return count_leaks(response, tail)


def main(args):
    for pw in args:
        count = pwned_api_check(pw)
        if count == 0:
            print(f'{pw} was not found!! Carry on!')
        else:
            print(f'{pw} was found {count} times...change the password!')
    print("Process done!")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
# k-匿名化（k-Anonymity）是一种隐私保护技术，旨在在数据发布的过程中保持个体的隐私。
# 具体而言，k-匿名化要求在发布的数据集中，每个记录都不能被唯一地识别，而是需要保证至少有k个记录在某些属性上具有相同的值，使得攻击者无法将个体追踪到具体的记录。
# 在这个app中只输入前五个hash化的password，返回被hack的列表，然后用户自己检查。
