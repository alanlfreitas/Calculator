# ==================== Calculator ==================== #

########## Function with outputs ##########
# def format_name(first_name, last_name):
#   if first_name == "" or last_name == "":
#     return "No entry." 
#   formated_first_name = first_name.title()
#   formated_last_name = last_name.title()
  
#   return f"{formated_first_name} {formated_last_name}"
  
# print(format_name(input("What's your first name? "), input("What's your last name? ")))

# def is_leap(year):
#   # Conditions to check if the year is a leap year or not
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
#   # Function to use info received from user
# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if month == 2 and is_leap(year):
#     return 29
#   else:
#     return month_days[month -1]

# # Inputs and output 
# year = int(input("Year: ")) # Enter a year
# month = int(input("Month: ")) # Enter a month
# days = days_in_month(year, month)
# print(f"{days} days")


############# Calculator Project #############
from art import logo
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide}

def calculator():
  print(logo)
  num1 = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()