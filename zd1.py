#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {
        '1a': 31,
        '1b': 30,
        '2c': 28,
        '5a': 24,
        '9c': 30,
        '11b': 17
    }
    for key, value in school.items():
        print("В классе ", key, " учатся ", value, "учеников")
    print('Меняем список....')
    school['11b'] = 12
    del school['1a']
    school['9c'] = '29'

    for key, value in school.items():
        print("Теперь в классе ", key, " учатся ", value, "студентов")

    s = 0
    for i in school:
        s = s + int(school[i])
    print("Теперь в школе учится:", s)
