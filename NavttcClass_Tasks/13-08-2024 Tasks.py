# 4.3.1.6
# def is_year_leap(year):
#     # A leap year is divisible by 4, but not every year divisible by 4 is a leap year.
#     # If a year is divisible by 100, it is not a leap year unless it is also divisible by 400.
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# # Testing the function
# test_data = [1700, 2001, 2016, 1987]
# test_results = [False, True, True, False]
#
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr, "->", end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")

# 4.3.1.7

# def is_year_leap(year):
# 	if year % 4 == 0:
# 		if year % 100 == 0:
# 			if year % 400 == 0:
# 				return True
# 			else:
# 				return False
# 		else:
# 			return True
# 	else:
# 		return False
#
# def days_in_month(year, month):
# 	month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 	if month == 2 and is_year_leap(year):
# 		return 29
# 	else:
# 		return month_days[month - 1]
#
#
# test_years = [1900, 2000, 2016, 1987]
# test_months = [3, 2, 1, 12]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
# 	yr = test_years[i]
# 	mo = test_months[i]
# 	print(yr, mo, "->", end="")
# 	result = days_in_month(yr, mo)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Failed")

# 4.3.1.8
# def is_year_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return True
#
#
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 2 and is_year_leap(year):
#         return 29
#     else:
#         return month_days[month - 1]
#
#
# def day_of_year(year, month, day):
#     days = 0
#     for m in range(1, month):
#         days += days_in_month(year, m)
#     days += day
#     return days
#
#
# print("The Corresponding Day of the Year is:", day_of_year(2000, 12, 25))

# 4.3.1.9

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()

# 4.3.1.10
def liters_100km_to_miles_gallon(liters):
    km_to_miles = 100 * 1/1.609344
    liters_per_gallon = 1/3.785411874
    miles_per_gallon = km_to_miles * liters_per_gallon
    miles_per_gallon_100km = (km_to_miles / 3.785411874) * 100
    final_miles_per_gallon = miles_per_gallon_100km / liters / 100
    return final_miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    km_per_gallon = miles * 1609.344
    liters_per_gallon = 3.785411874
    liters_per_100km = (100 / km_per_gallon) * liters_per_gallon



#
# Write your code here
#

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))
