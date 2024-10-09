class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):

        print(f"Ngày: {self.day}/{self.month}/{self.year}")

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self, month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if self.is_leap_year(year) else 28
        return 0

    def next(self):
        self.day += 1
        if self.day > self.days_in_month(self.month, self.year):
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1


class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02}/{self.month:02}/{self.year}")

    def next_day(self):
        days_in_month = [31, 29 if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        self.day += 1
        if self.day > days_in_month[self.month - 1]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1


day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
date = Date(day, month, year)
date.display()
date.next_day()
date.display()
