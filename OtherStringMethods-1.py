#6. casefold() - used to convert string to lowercase.

# It is similar to the lower() string method
# but the case removes all the case distinctions present in a string.
#Syntax:  string.casefold()
#Parameters: The casefold() method does not take any parameters.
#Return value: Returns the case folded string the string converted to lower case.

string = "GEEKSFORGEEKS"
print(f"\nString '{string}' to lowercase is: {string.casefold()}")

#Python String casefold() Method is more aggressive in conversion to lowercase characters
#because it tends to remove all case distinctions in a String.

sample_string = "ß"
print(f"\nString '{sample_string}' using lower() is: {sample_string.lower()}")
print(f"\nString '{sample_string}' using casefold() is: {sample_string.casefold()}")

#Here, we have a Python String with characters of mixed cases.
#We are using the Python casefold() Method to convert everything to lowercase.

case_string = "WeightAGE oF THe DiScuSSiON"
print(f"\nString '{case_string}' after casefold() is: '{case_string.casefold()}'")

#7. center() - creates & returns a new string that is padded with the specified character
#Syntax:  string.center(length[, fillchar]) or string.center(__width: , __fillchar:'') or string.center(40, 'e')
#Parameters:
#1) length: length of the string after padding with the characters.
#2) fillchar: (optional) characters which need to be padded. If it’s not provided, space is taken as the default argument.
#Returns: Returns a string padded with specified 'fillchar' and it does not modify the original string.
#if width is

despac_string = "Wisconsin-Madison University"
print(f"\nString '{despac_string}' of length {despac_string.__len__()} using centre() is: '{despac_string.center(40)}'")
print(f"\nString '{despac_string}' of length {despac_string.__len__()} using centre() is: '{despac_string.center(40, '#')}'")

#8. count() -> syntax: count(character, start(optional), end(optional))
print(f"\nThe count() of 'i' for '{despac_string}' is: {despac_string.count('i')}")
print(f"Whereas the count() of 'i' within a specified range 0 to 16 in '{despac_string}' is: {despac_string.count('i', 0, 16)}")

#9. endswith() - returns True if a string ends with the given suffix
print(f"\nThe string '{despac_string}' using endswith() is: {despac_string.endswith("str", 0, 18)}")

#10. find() - returns the lowest index or first occurrence of the substring if it is found in a given string.
print(f"\nThe string '{despac_string}' using find() returns: {despac_string.find("Madison", 0, 20)}")

#11. format() - formats string with a dependent value
print("\nThe string used for all examples is: ", format(str(despac_string)))

pi = 3.14159
radius = float(input("\nThe radius 'r' is: "))  #/a prints with bell symbol at start
area_of_circle = pi*radius*radius
print("Area of circle with pi {} and radius {} is {}".format(pi, radius, int(area_of_circle)))






