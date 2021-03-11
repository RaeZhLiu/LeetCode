def remove_signed(str_num: str) -> str:
    if str_num[0] == '+':
        str_num = str_num[1:]

    length = len(str_num)

    return [str_num, length]


def add(str1: str, str2: str) -> str:
    str1, m = remove_signed(str1)
    str2, n = remove_signed(str2)

    while m > n:
        str2 = '0' + str2
        n += 1
    while m < n:
        str1 = '0' + str2
        m += 1

    response = ''
    tmp_num = 0
    for i in range(m - 1, -1, -1):
        a = int(str1[i])
        b = int(str2[i])
        sum = a + b + tmp_num
        response = str(sum % 10) + response
        tmp_num = sum // 10

    if tmp_num != 0:
        response = '1' + response

    return response


if __name__ == '__main__':
    print(add("+111111111", "23456"))