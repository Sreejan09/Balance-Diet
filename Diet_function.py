#impoting all the details of the nutrient from Detail Nutrient
from details_nutrient import *

def bmi_cal(weight, height):
    bmi = (weight)/(height*height)
    return bmi

#defing the weight status depending upon the bmi value
def weight_status(bmi):
    if bmi<18.5:
        return "Under Weight"
    elif bmi <24.9:
        return "Normal Weight"
    elif bmi<29.9 :
        return "Over Weight"
    else:
        return "Obesity"

#printing the nutrient as per the value
def Basic_Nutrient(bmi):
    if bmi< 18.9:
        print("List of Fruits are : ", end=' ')
        print(Fruits_underWeight)
        print("\nList of Grains are : ", end=' ')
        print(Grain_underWeight)
        print("\nList of Vegetables are : ", end=' ')
        print(vegetable_underWeight)
    elif bmi< 24.9:
        print("\nList of Fruits are : ", end=' ')
        print(Fruits_normal)
        print("\nList of Grains are : ", end=' ')
        print(Grain_normal)
        print("\nList of Vegetables are : ", end=' ')
        print(vegetable_normal)
    else :
        print("\nList of Fruits are : ", end=' ')
        print(Fruits_overWeight)
        print("\nList of Grains are : ", end=' ')
        print(Grain_overWeight)
        print("\nList of Vegetables are : ", end=' ')
        print(vegetable_overWeight)

    
def Fruits_details():
    user_liked_fruit = []
#taking the input fruits liked by the user
    no_of_fruits = int(input("Enter the number of Fruits you like : "))
    i =1
    for i in range(1,no_of_fruits+1):
        fruit=input(f"{i})")
        user_liked_fruit.append(fruit)

    i=0
    print()

    for i in user_liked_fruit:
        if i in Fruits : 
            pass
        else:
            print("\nGiven Fruit is not present in the Dictionary : ")
            print(f"Add the details of {i} : ", end ='')
            detail = input()
            Fruits[i] = detail
        print()

    print("\nThe benefit's of the following Fruits are : \n")
    for i in user_liked_fruit:
        if i in Fruits : 
            print(f"{i} : {Fruits.get(i)}")
        print()
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

def vegetable_details():

    user_liked_vegetable = []
#taking the input vegetable liked by the user
    no_of_vegetable = int(input("Enter the number of vegetable you like : "))
    i =1
    for i in range(1,no_of_vegetable+1):
        vegetable=input(f"{i} : ")
        user_liked_vegetable.append(vegetable)

    i=0
    print()

    for i in user_liked_vegetable:
        if i in vegetables : 
           pass
        else:
            print("\nGiven vegetable is not present in the Dictionary : ")
            print(f"Add the details of {i} : ", end ='')
            detail = input()
            vegetables[i] = detail
        print()

    print("\nThe benefit's of the following vegetable are : \n")
    for i in user_liked_vegetable:
        if i in vegetables : 
            print(f"{i} : {vegetables.get(i)}")
        print()
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")



def grains_details():

    user_liked_grains = []
#taking the input vegetable liked by the user
    no_of_grains = int(input("Enter the number of Grains : "))
    i =1
    for i in range(1,no_of_grains+1):
        grain=input(f"{i}) ")
        user_liked_grains.append(grain)

    i=0
    print()

    for i in user_liked_grains:
        if i in Grains : 
           pass
        else:
            print("\nGiven Grains is not present in the Dictionary : ")
            print(f"Add the details of {i} : ", end ='')
            detail = input()
            Grains[i] = detail
        print()

    print("\nThe benefit's of the following Grains are : \n")
    for i in user_liked_grains:
        if i in Grains : 
            print(f"{i} : {Grains.get(i)}")
        print()
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")



