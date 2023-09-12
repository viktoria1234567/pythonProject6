# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена
# и текст найден в её выводе и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.

import subprocess


def ttest(comm, text):
    result = subprocess.run(comm, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    # print(result.stdout)
    if text in result.stdout:
        return True
    else:
        return False


ttest("cat /etc/os-release", "22.04.1")
