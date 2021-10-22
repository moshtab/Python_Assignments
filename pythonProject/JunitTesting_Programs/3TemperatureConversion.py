'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Temperature Conversion”
'''
def farenheitConversion():
    c=int(input("Enter a celsius degree"))
    f=(c * 9/5) + 32
    return f
def celsiusConversion():
    f = int(input("Enter a farenheit degree"))
    c=(f-32) * 5/9
    return c
def errorhandler():
    print("Invalid choice")
print('''
   1. Farenheit conversions
   2. Celsius conversions
''')
choice = int(input("Enter your choice"))
operations = {
    1: farenheitConversion,
    2: celsiusConversion
}
output = operations.get(choice, errorhandler)()
print(output)