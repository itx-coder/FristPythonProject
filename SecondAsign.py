# Answer of Question no 1
Subject_1 = int(input("Enter your Subject 1 marks ?"))
Subject_2 = int(input("Enter your Subject 2 marks ?"))
Subject_3 = int(input("Enter your Subject 3 marks ?"))


Total_Marks = Subject_1 + Subject_2 + Subject_3

percentage = Total_Marks / 300 * 100

print("Persentage of Student is :" , percentage)

if percentage >=  90 :
    print(" Your Grade is A+", "Congratulations! You are topper")

elif percentage <= 90 and percentage >= 80:
    print(" Your Grade is A")
    
elif percentage <= 80 and percentage >= 70:
    print(" Your Grade is B")

elif percentage <= 70 and percentage >= 60:
    print(" Your Grade is C")

elif percentage <= 60 and percentage >= 50:
    print(" Your Grade is D")

else:
    print(" Your Grade is F", "Better luck next time")

# Answer of Question no 2 

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0):
    print( year, " is a leap year.")

else:
    print( year,"is not a leap year.")

# Answer of Question no 3


choice = input("Convert from (C)elsius or (F)ahrenheit? ")

if choice == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print("the converted fahrenheit value to celsius is :" , fahrenheit,"°C")
elif choice == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit - 32 * 5/9
    print("the converted celsius value to Fahrenheit is" , celsius,"°F")
else:
    print("Invalid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Answre of Question no 4


side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Determine the type of triangle
if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
