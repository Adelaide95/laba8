#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Список студентов.
    students = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            # Запросить данные о работнике.
            name = input("Фамилия и инициалы? ")
            num = input("Номер группы? ")
            print("Успеваемость?  ")
            mat = int(input())
            rus = int(input())
            hist = int(input())
            phis = int(input())
            bio = int(input())
            # Создать словарь.
            student = {
                'name': name,
                'num': num,
                'mat': mat,
                'rus': rus,
                'hist': hist,
                'phis': phis,
                'bio': bio
            }
            # Добавить словарь в список.
            students.append(student)
            # Отсортировать список в случае необходимости.
            if len(students) > 1:
                students.sort(key=lambda item: item.get('num', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20,
                '-' * 20,
                '-' * 20,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Номер группы",
                    "математика",
                    "русский",
                    "физика",
                    "история",
                    "биология"
                )
            )
            print(line)
            # Вывести данные о всех сотрудниках.
            for idx, student in enumerate(students, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>20} | {:>20} | {:<20} | {:<20} | {:>20} |'.format(
                        idx,
                        student.get('name', ''),
                        student.get('num', ''),
                        student.get('mat', ),
                        student.get('rus', ),
                        student.get('hist', ),
                        student.get('phis', ),
                        student.get('bio', )
                    )
                )
            print(line)

        elif command.startswith('select '):
            count = 0
            for student in students:
                averg = (student.get('mat', '') + student.get('rus', '')
                         + student.get('hist', '') + student.get('phis', '') + student.get('bio', '')) / 5
                if averg >= 4:
                    count += 1
                    print(
                            '{:>4}: {}'.format(count, student.get('name', ''), student.get('num', ''))
                        )
            # Если счетчик равен 0, то студенты не найдены.
            if count == 0:
                print("Ученики со средним баллом выше 4-х не найдены.")
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select - вывести имена студентов со среднем баллом выше 4")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
