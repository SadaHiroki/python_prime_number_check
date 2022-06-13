sosu_list = [2, 3, 5, 7, 11, 13]


def sosu(check):
    for i in sosu_list:
        if not (int(check) == i) and int(check) % i == 0:
            return str(check) + " is no"
    return str(check)+" is yes"


result = sosu(input("1～100で好きな数字を入力して下さい："))
print(result)