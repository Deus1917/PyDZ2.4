import datetime


class Persona:
    def __init__(self, familia, date=datetime.date):
        self.familia = familia
        self.date = date

    def print_info(self):
        print(f"Информация о персоне: фамилия - {self.familia}, дата рождения - {self.date}")

    def opr_age(self):
        today = datetime.date.today()
        return today.year - self.date.year - ((today.month, self.date.month) < (today.day, self.date.day))


Prikol = Persona("Armian", datetime.date(2005, 9, 23))
Prikol.print_info()
print(f"Возраст : {Prikol.opr_age()}")


class Abiturient(Persona):
    def __init__(self, fakultet, familia, date):
        self.fakultet = fakultet
        super().__init__(familia, date)

    def print_info(self):
        print(
            f"Информация о абитуриенте: Фамилия - {self.familia} , дата рождения - {self.date} , факльтет, на который хочет поступить {self.fakultet}")


Drug = Abiturient("POKS", "Аветисян", datetime.date(1996, 9, 23))
Drug.print_info()


class Student(Abiturient):
    def __init__(self, curs, fakultet, familia, date):
        self.curs = curs
        super().__init__(fakultet, familia, date)

    def print_info(self):
        print(
            f"Информация о студенте: Фамилия - {self.familia} , дата рождения - {self.date} , факльтет, на который поступил {self.fakultet}, курс {self.curs}")


Kent = Student(1, "Poks", "Аветисян", datetime.date(1999, 9, 23))
Kent.print_info()


class Teacher(Abiturient):
    def __init__(self, doljnost, staj, fakultet, familia, date):
        self.doljnost = doljnost
        self.staj = staj
        super().__init__(fakultet, familia, date)

    def print_info(self):
        print(
            f"Информация о преподавателе: Фамилия - {self.familia} , дата рождения - {self.date} , факльтет, на котором работает {self.fakultet}, должность - {self.doljnost}, стаж - {self.staj} ")


Anbdryxa = Teacher("Хокаге", 10, "POKS", "FASH_KRUT", datetime.date(2001, 10, 19))
Anbdryxa.print_info()
Personi = [Prikol, Drug, Kent, Anbdryxa]
for i in Personi:
    i.print_info()
diapozon_min = int(input("Введите минимум поиска возраста - "))
diapozon_max = int(input("Введите максимум поиска возраста - "))
print("Люди, в заданном диапазоне: ")
for i in Personi:
    if (i.opr_age() >= diapozon_min) and (i.opr_age() <= diapozon_max):
        i.print_info()
