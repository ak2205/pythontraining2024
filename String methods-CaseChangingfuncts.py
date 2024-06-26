#in-built String functions (methods) - totally 48, from GFG
#case-changing string functions

#1. lower() - Converts all uppercase characters in a string into lowercase
#2. upper() - Converts all lowercase characters in a string into uppercase
#3. title() - Convert string to title case
#4. swapcase() - Swap the cases of all characters in a string
#5. capitalize() - Convert the first character of a string to uppercase

#Time complexity: O(n), n -> string length
#Auxiliary space: O(1)

#1. lower()
practice_string = "Liverpool_John_moores_university"
print(f"The original string {practice_string} converted is: {practice_string.title()}")

#2. upper()
dummy_string = "Australia_got_karma"
print(f"The original string {dummy_string} converted is: {dummy_string.title()}")

#3. title()
foe_string = "yUvRaj iS a sIxEr KiNg"
print(f"The original string {foe_string} converted is: {foe_string.title()}")

#4. swapcase()
friend_string = "dHONI_fINISHES_oFF_iN_sTYLE"
print(f"The original string {friend_string} converted is: {friend_string.swapcase()}")

#5. capitalize()
ubuntu_string = "Auschwitz_Detention_camp"
print(f"The original string {ubuntu_string} converted is: {ubuntu_string.capitalize()}")