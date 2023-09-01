# # g1=int(input('How many students on the course?'))
# # b1=int(input('Desiredgroupsize?'))
# # sonuc =g1//b1
# # if g1/b1>sonuc:
# #     sonuc +=1 
# #     if True:
      
# # print(f'Numberofgroupsformed:{sonuc}')

# # ö = int(input("How many students on the course? "))
# # g = int(input("Desired group size? "))
# # sonuç = 0.0
# # if (ö % g) > 0:
# #  sonuç = (ö / g) + 1
# # else:
# #  sonuç = ö / g
# # print(f"Number of groups formed: {int(sonuç)}")

# birth_year = int(input("Enter your age"))
# age = 2023 - birth_year # Arithmetic Expression
# is_adult = age >= 18 # Boolean Expression

# if is_adult:
#  print("You can Vote!")
# "sait" str
# 1 int
# 1.5 float
# True - bool

#1 syntax error
#2 runtime error
#3 logical error

# x = 10
# y = 5
# result = x / y

# print(f"{x} divided by {y} is {result}")
hourly_wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")

daily_wages = hourly_wage * hours
if day == "sunday":
    daily_wages *= 2
    
