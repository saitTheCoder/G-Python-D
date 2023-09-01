# When using an if-else construction, 
# one and exactly one of the branches will always be executed. 

number = int(input("Please type in a number: "))

# if number % 2 == 0:
#     print("cift sayi") 
# if number % 2 != 0:
#     print("Tek sayi") 

# if number % 2 == 0:
#     print("cift sayi") 
# # elif number % 2 != 0:
# #     print("cift sayi") 
# else:
#     print("tek sayi")  

if number > 0:
    print("pozitif")
elif number <0:
    print("negatif")
else:
    print("sifir")
