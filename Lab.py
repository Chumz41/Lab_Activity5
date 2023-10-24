# Jose Diaz
#10/12/23
# Code Number 1
# program prints out hello world
print("Hello World")


# Code Number 2
# says hello to you
name = input("Type your name >> ")
print("Hello " + name)

# Code Number 3
# says hello only to me and young
names = input("Type your name >> ")

if names.lower() == "jose":
    print("Hello, jose")
elif names.lower() == "young":
    print("Hello, instuctor young")
else:
    print("Hello, " + names)


# Code Number 4
# Gives you the area of a circle given the radius
rad_Circle = int(input("Enter radius: "))
RadiusofCircle = (3.14 * rad_Circle ** 2)
print("The area will be : ")
print(RadiusofCircle)

# Code Number 5
# Calculates Mileage given user inputs
Miles_Driven = int(input("How many miles have you driven :"))
Gallons = int(input("Estimated gallons used : "))
Mileage = (Miles_Driven / Gallons)
print(" your gas mileage is : ")
print(Mileage)


# Code number 6
# Converts F to C user interacts
degree_fahrenheit = int(input("What is the temperature in F that you want to convert?"))
degree_Celsius = (degree_fahrenheit - 32) * (5/9)

print("The conversion to Celsius is >> ")
print(degree_Celsius)

# Code number 7
# Calculates the the day you will return using the floor %
start_Day = int(input("Enter the starting day number >> "))
length_of_Day = int(input("Enter length of stay >> "))
return_day = (start_Day + length_of_Day) % 7


days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print("You will return on ", days_of_week[return_day])

