def format_name(f_name: str, l_name: str):
    if f_name == "" or l_name == "":
        return "no empty pls"
    return f"{f_name.title()} {l_name.title()}"

print(format_name('lEAndRo', 'Da sOUzA'))
print(format_name("", ""))

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year: int, month: int):
    """Return the days of a given month. Use year to calculate if it's a leap year."""

    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(is_leap(year) and month == 2):
        return 29
    return month_days[month -1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

