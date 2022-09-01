import re

strings = ["racecar", "apples", "ana", "a santa at nasa", "meSSenger", "the !cAt in!! the hat", "avId diva", "Amy, must I jujitsu my ma??", "Ah, Satan sees Natasha!!"]


for string in strings:
	'''Using regex to return only letters in a list'''
	remove_characters = re.findall(r"[aA-zZ]+",string)
	
	'''Using the join method to merge elements in the list'''
	remove_characters = ''.join(remove_characters).replace(" ","").lower()

	'''This reverses the order of remove_characters'''
	flippled_remove_characters = remove_characters[::-1].replace(" ","")

	'''Conditional check to see if the reversed string matches unreversed string'''
	if remove_characters == flippled_remove_characters:
		print(f"{string} is a palindrome!")
	else:
		print(f"{string} is not a palindrome!")
