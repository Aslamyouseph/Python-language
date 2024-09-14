year=int(input("enter the year  "))
month=int(input("enter the month  "))
week=int(input("enter the week  "))
day=int(input("enter the days  "))
bir=int(input("enter the birth day "))
sample_year=year*12
main_year=1080-sample_year
sample_month=month-bir
orginal_year=main_year-sample_month
sample_week=week*7
main_week=30-sample_week
orginal_week=main_week%7
orginal_days=orginal_week%7+30-day
print(f"you have {orginal_days} days and {orginal_week} weeks and {orginal_year} month are left")
