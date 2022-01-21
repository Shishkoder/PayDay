class Person:
    """
    """
    def __init__(self, name, surname, time=0):
        self._name = name
        self._surname = surname
        self._time = time

    def __str__(self):
        return f"{self._name} {self._surname}, {self._time}"

    def _add_time_self(self, time):
        self._time += time


class Employer(Person):
    """
    """
    global __PAYDAY
    __POST = "Штатный сотрудник"
    __PAYDAY = 120_000

    def show_payday(self):
        if self._time > 160:
            self.__over_pay = __PAYDAY / 160 * (self._time - 160) * 2
            print(self.__over_pay + __PAYDAY)
        else:
            print(__PAYDAY)


class Freelancer(Person):
    """
    """
    global __PAYDAY, __POST
    __POST = "Фрилансер"
    __PAYDAY = 1000

    def __str__(self):
        return super().__str__() + f" {__POST}"

    def show_payday(self):
        print(__PAYDAY * self._time)


class Director(Person):
    """
    """
    global __PAYDAY, __POST, __AWARD
    __POST = "Директор"
    __PAYDAY = 200_000
    __AWARD = 20_000

    def __str__(self):
        return super().__str__() + f" {__POST}"

    def show_payday(self):
        if self._time > 160:
            print(__PAYDAY + __AWARD)
        else:
            print(__PAYDAY)


    def check_has_employer(self, name, surname):
        for i in employers_list:
            if name.title() == i._name and surname.title() == i._surname:
                return True

        return False

    def add_employers(self, name, surname, post, time=0):
        if not self.check_has_employer(name, surname):
            if post.lower() == "директор":
                employers_list.append(Director(name, surname))
            elif post.lower() == "фрилансер":
                employers_list.append(Freelancer(name, surname))
            elif post.lower() == "штатный сотрудник":
                employers_list.append(Employer(name, surname))
            else:
                print("Дурной?")
        else:
            print("Такой сотрудник уже есть!")

    def add_time_others(self, name, surname, time):
        if self.check_has_employer(name, surname):
            for i in employers_list:
                if name.title() == i._name and surname.title() == i._surname:
                    i._time += time
        else:
            print("Такого сотрудника нет!")


employers_list  = [Director("Эльдар", "Шамсиев", 100)]
ls = []

name = input("Введите имя: ")
surname = input("Введите фамилию: ")

a = Director("Эл", "Ша", 10)
a.show_payday()
a.add_employers("Эльдар", "Шамсиев", "Директор")
a.add_employers("Эльдар1", "Шамсиев1", "Директор")
a.add_time_others("Эльдар", "Шамсиев", 3)

for i in employers_list:
    ls.append({"Имя": i._name, "Фамилия": i._surname, "Время": i._time})

print(ls)
