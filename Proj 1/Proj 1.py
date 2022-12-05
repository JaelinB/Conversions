#####################################################################
#  Computer Project #1
#
#    Program that takes "rods" and converts them to meters,\
#    feet, miles furlongs, and minutes to walk
#
#    The first section of code is where the user inputs a number
#    The number then results in the number of rods in the format\
#    of a float 
#
#    The next sction(middle) is where I diplay the convesion string
#    I make sure that the num_str1 variable converts to a float
#
#    The third section of code is the conversion 
#    This is where the rods are converted into meters, feet,\
#    miles, furlongs, and minutes to walk
#    
#    By Using mathematics I was able to convert each piece correctly 
#    The core of this project is the num_str1 variable
#####################################################################
 

num_str1 = input('Input rods: \n')
print("You input",float(num_str1),"rods.")

print("\nConversions")
num_str1 = float(num_str1)

print("Meters:",(round(num_str1 * 5.0292,3)))
print("Feet:",(round(num_str1 * 5.0292  / 0.3048,3)))
print("Miles:",(round(num_str1 * 5.0292 / 1609.34,3)))
print("Furlongs:",(num_str1 / 40))
print("Minutes to walk",num_str1, "rods:", round(num_str1 * 5.0292 / 1609.34 / 3.1 * 60,3))





