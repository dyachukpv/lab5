import csv
import os.path
from random import random


class Travels:

    def __init__(self):

        self.data = []
        self.reader_csv()

    def __repr__(self):
        """
        Возвращает путь к данным и сами данные, если пытаться отобразить класс не в виде строки

        :return: string
        """
        return "D:\\test1\\, data)"

    def __str__(self):
        """
        Возвращает данные словари при использовании str() или print()  в строком представлении

        :return: {}
        """
        return self.data

    def __iter__(self):
        """
        Возвращает итератор для данных объекта при вызове iter

        :return:
        """
        return iter(self.data)

    def __len__(self):
        """
        Возвращает кол-во элементов в списке data

        :return: int
        """
        return len(self.data)

    def __getitem__(self, i):
        return self.data[i]

    def reader_csv(self):
        """
        Считывание данных из CSV-файла с последующим выводом отсортированной информации
        :return:
        """
        with open("C:\\test1\\travels.csv") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                self.data.append(row)

    def writer_csv(self):
        """
        Запись новой строки в CSV-файл
        :return:
        """
        with open("C:\\test1\\travels2.csv", "a", newline="") as file:
            columns = ["number", "date", "nomer", "marka", "price"]
            writer = csv.DictWriter(file, delimiter=';', fieldnames=columns)
            writer.writerows(self.data)


class Travel(Travels):

    def __repr__(self):
        """
        Возвращает __repr__ от класса Travels

        :return: string
        """
        return super().__repr__()

    def __init__(self):
        super().__init__()

    def __str__(self):
        """
        Возвращает данные словари при использовании str() или print()  в строком представлении

        :return: string
        """
        return self.data_output()

    def __getitem__(self, i):
        return super().__getitem__(i)

    def __setattr__(self, key, value):
        """
        Функция, отвечающая за присваивание значений свойствам

        :param key
        :param value:str/int
        :return:
        """
        if key == "data" and isinstance(value, list):
            self.__dict__[key] = value
        if key == "number" and isinstance(value, str):
            self.__dict__[key] = value
        elif key == "date" and isinstance(value, str):
            self.__dict__[key] = value
        elif key == "gosnomer":
            print("Нельзя изменять 'gosnomer' напрямую")

    @staticmethod
    def static_method(value):
        print("Вывод введённых данных через статический метод: ", value)

    def generator(self, n):
        while n > 0:
            yield '*'
        n -= 1


    def data_output(self):
        strr = ""
        print("Данные из файла")
        for i in self.data[0].keys():
            strr += ("{:16s}".format(i) + " ")
        strr += "\n"
        for row in self.data:
            for q in row.values():
                strr += ("{:16s}".format(q) + " ")
            strr += "\n"
        return strr

    def count_file(self):
        """
        Подсчёт кол-ва файлов в папке вод этого кол-ва в консоль
        :return:
        """
        print(len([name for name in os.listdir("D:\\test1") if os.path.isfile(os.path.join("D:\\test1", name))]))

    def sortirovka(self):
        """
        Сортировка данных по строковому и числовому типу

        """
        print("Отсортированная информация по числовому типу:", sorted(self.data, key=lambda k: k['price']))
        print("Отсортированная информация по строковому типу:", sorted(self.data, key=lambda k: k['marka']))

    def sortt(self):
        """
        Вывод данных, где number > 3

        """
        for i in self.data[0].keys():
            print("{:16s}".format(i), end=" ")
        print()
        for q in self.data:
            if int(q['number']) > 3:
                for k in q.values():
                    print("{:16s}".format(k), end=" ")
                print()


a = Travel()
a.count_file()

print(a.data_output())
print("Вывод исходных данных, где номер(number)>3")
a.sortt()
a.sortirovka()
a.writer_csv()
c = a.__getitem__(2)
print("Возвращение элемента под индексом 2\n", c)
a.static_method(145)
j = a.generator(3)
print(next(j))


