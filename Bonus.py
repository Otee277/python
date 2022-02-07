#PROGRAM TO GET SALARY AND YEARS OF SERVICE AND GIVE BONUS:
salary = int(input("Enter salary: "))
years = int(input("Enter years of service: "))
if years>10:
  bonus = salary*0.1
  print("Bonus is: ",bonus)
if years>=6 and years<=10:
  bonus = salary*0.08
  print("Your bonus is: ",bonus)
if years<6:
  bonus = salary*0.06
  print("Your bonus is: ",bonus)
  