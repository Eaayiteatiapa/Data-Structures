# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 14:29:26 2023

@author: HP
"""

# list of available cars and their prices
cars= {"SUV":20000, "Bugatti":50000, "Ferarri":60000 ,"Ford Fiesta":40000,"Escort":50000,
      "Tesla":95000,"Chevrolet N":50000,"Kantanka X":30000,"Toyota Camry":40000,"Dans":30000,
      "Verna":30000,"Creta":20000,"Hyundai Aura":40000,"Alcazar":50000,"Kona":40000,"Grandeur":50000,"Hyundai Stargazer":60000,"Santa":100000 }
# get user input for car name
car_name= input("Enter a car name:")
# check if car name is in the list of available cars
if car_name in cars:
    print("Yes")
    # if car name is present,get its price
    car_price = cars[car_name]
    print(f"The price of {car_name} is ${car_price}.")
else:
    #if car name is not present ,inform the user
    print(f"Sorry,{car_name} is not available. ")
    
    from tabulate import tabulate
    
    print('Car brands available')
    print('(1)Ford \
          (2)Toyota\
          (3)Hyundai ')
    brand=int(input('Specify car Brand using integer attached:'))
    if brand==1:
        print('These are the Ford Cars Available ')
        data = [["Fiesta",20000],
                ["Escort",40000],   
                ["Taurus",50000],
                ["Focus",25000],
                ["GT",30000],
                ["Mustang",40000],
                ["Ecosport",25000],
                ["Equator",30000],
                ["Expedition",40000],
                ["Ligthening",100000]]
        col_names =["Cars","Prices"]
        print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
        totype=str(input('Specify Ford using: '))
        if totype=='Fiesta':
         print('this car costs {}'.format(Fiesta))
        elif totype=='Escort':
         print('this car costs {}'.format(Escort))
        elif totype== 'Taurus':
         print('this car costs {}'.format(Taurus))
        elif totype== 'Focus':
         print('this car costs {}'.format(Focus))
        elif totype== 'GT':
         print('this car costs {}'.format(GT))
        elif totype== 'Mustang':
         print('this car costs {}'.format(Mustang))
        elif totype== 'Ecosport':
         print('this car costs {}'.format(Ecosport))
        elif totype== 'Equator':
         print('this car costs {}'.format(Equator))
        elif totype== 'Expedition':
         print('this car costs {}'.format(Expedition))
        elif totype== 'lightening':
         print('this car costs {}'.format(Lightening))
         
         Github account:= https://github.com/Eaayiteaiapa