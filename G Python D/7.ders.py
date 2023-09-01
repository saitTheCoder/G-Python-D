# A kursu icin sertifika alma sartlari
# 1- %70 derslere katilma sarti
# 2- kurs sonu sinavindan en az 70 puan almak

# katilim = 100
# sinav = 70

# sertifika_alabilir_mi = katilim >= 70 and sinav >= 70

# if sertifika_alabilir_mi:
#     print("sertifika alabilir")
# else:
#     print("sertifika alamaz")
# # print("sertifika_alabilir_mi -->",sertifika_alabilir_mi)

# 5ten buyuk 10 dan kucuk sayilar 6,7,8,9
# number = int(input("sayi giriniz: "))

# print(number > 5 and number < 10)

# 6 dan kucuk yada  9 dan buyuk sayilar 

# print(number < 6 or number > 9 )

# B kursu icin sertifika alma sartlari
# 1- %70 derslere katilma sarti
# 2- kurs sonu sinavindan en az 70 puan almak

# katilim = 10
# sinav = 50

# sertifika_alabilir_mi = katilim >= 70 or sinav >= 70
# print(sertifika_alabilir_mi)
# print(True and True and True or True and False)

number = int(input("enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("pozitif cift sayi")
        if number % 5 == 0:
            print("super number")
    else:
        print("pozitif tek sayi")
else:
    print("negatif sayi")

# if number > 0 and number % 2 == 0:
#     print("pozitif cift sayi")
# elif number > 0 and number % 2 != 0:
#     print("pozitif tek sayi")
# else:
#     print("negatif sayilar")  
