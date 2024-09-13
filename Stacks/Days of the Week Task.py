class WeekDayError(Exception):
    pass


class Weeker:
    __week_days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in self.__week_days:
            raise WeekDayError()
        self.__current_day = self.__week_days.index(day)

    def __str__(self):
        return self.__week_days[self.__current_day]

    def add_days(self, n):
        self.__current_day = (self.__current_day + n) % 7

    def subtract_days(self, n):
        self.__current_day = (self.__current_day - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")

