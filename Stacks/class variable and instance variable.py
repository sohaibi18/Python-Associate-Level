# class Tech:
#     tool = "Php"
#
#     def __init__(self, val):
#         self.val = val
#
#     # def second(self, val):
#     #     self.sec_val = val
#
#
# tc = Tech(1)
# tc1 = Tech(2)
# print(tc.val)
# print(tc1.val)
#
# print(tc.tool)
# Tech.tool = "PHP"
# print(tc.tool)
#============================================================
# class Animal:
#     pass
#
#
# class Mammal(Animal):
#     pass
#
#
# class Bird(Animal):
#     pass
#
#
# class Bat(Mammal, Bird):
#     pass
#
#
# def printBases(cls):
#     print('( ', end='')
#     print(f"{cls.__name__} base classes: (", end='')
#     for x in cls.__bases__:
#         print(x.__name__, end=' ')
#     print(')')
#
#
# printBases(Animal)
# printBases(Mammal)
# printBases(Bird)
# printBases(Bat)
#===========================================================
