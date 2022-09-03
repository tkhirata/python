'''list of palindromes and non-palindromes'''
strings = ["Anna", "madam", "apples", "mango", "gravy", "repaper", "taco cat", "top spot", "Don't nod.", "I did, did I?", "Eva, can I see bees in a cave?"]

'''empty list for storing letters of string'''
separated_string = []

'''empty list for storing letters of string reversed'''
reversed_separated_string = []

'''counter for returning original strings in final output'''
i = 0

'''takes string out of list'''
for string in strings:
	'''removes any white spaces and makes everything lower case'''
	string = string.replace(' ','').lower()
	
	'''takes each letter of string and adds it to a list'''
	for letter in string:
		'''Checks to see if a letter is a letter'''
		character_check = letter.isalpha()

		'''if character is a letter it adds to the list'''
		if character_check == True:
			separated_string.append(letter)

			'''takes letter and add it to front of reversed string list'''
			reversed_separated_string.insert(0,letter)

	'''combines all the elements together in separated string list'''
	combined_string = "".join(separated_string)

	'''combines all the elements together in reversed string list'''
	combined_string_reversed = "".join(reversed_separated_string)
	
	'''final conditional check the compares reversed string with non-reversed'''
	if combined_string == combined_string_reversed:
		print(f"\"{strings[i]}\" is a palindrome!")
		'''clears out list so elements aren't combined with next string'''
		separated_string.clear()
		reversed_separated_string.clear()
	else:
		print(f"\"{strings[i]}\" is not a palindrome!")
		separated_string.clear()
		reversed_separated_string.clear()

	i = i + 1


