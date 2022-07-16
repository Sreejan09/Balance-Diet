#impoting all function present in Diet_function
from Diet_function import * 

#taking the input of the basic Details
print("\n!!! Welcome to Balance Diet World !!!")
print("\n::::: Enter Some detail To Go On Exciting Tour :::::")
name = input("Enter Your Name : ")
weight = float(input ("Enter the weight in Kg : "))
height = float(input("Enter the height in meter : "))


#calculating the bmi of the user and rounding upto two decimal places
bmi = round(bmi_cal(weight,height), 2)
#getting the status of the bmi value 
bmi_status = weight_status(bmi)

#printing the  calculated value
print(f"\nWelcome {name},Good to see that you are giving importance to your Diet.\nAs per your data BMI(Body Mass Index) is {bmi} and which lies in {bmi_status} status")
print("\n------ Based on the above data, the suggest Nurtrient for you are  : ------\n\n")

#printing the list of fruits, vegetable , fruits
Basic_Nutrient(bmi)


flag =1

#while loop for the 
while flag !=0:
    print("\n1 For Fruits Details\n2 For Vegetables\n3 For Grains \n0 For Exit\nEnter : ", end=' ')
    flag = int(input())

    if flag == 1:
        Fruits_details()
    elif flag ==2 :
        vegetable_details()
    elif flag == 3:
        grains_details()
    else:
        break

print("Write your feedback : ")
str=input()

print("\nThanku for your Feedback.\nYour feedback is important for us, Hope you again come for checking your diet")