class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def __str__(self):
        return '({}, {}, {})'.format(self.name, self.surname, self.get_total_income())


a = Position('Maxim', 'Grekov', 'Engineer', '168000', '16800')
print(a.__str__())
'''
print(a.get_full_name(), a.get_total_income())
'''