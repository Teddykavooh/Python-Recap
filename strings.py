#The is_palindrome function checks if a string is a palindrome.
#  A palindrome is a string that can be equally read from left 
# to right or right to left, omitting blank spaces, and ignoring 
# capitalization. Examples of palindromes are words like kayak and
#  radar, and phrases like "Never Odd or Even". Fill in the blanks 
# in this function to return True if the passed string is a palindrome, 
# False if not.
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for ___:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if ___:
			new_string = ___
			reverse_string = ___
	# Compare the strings
	if ___:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


'''Solution'''
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for i in input_string.split():
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		new_string = new_string + i.replace(" ", "")
		reverse_string = new_string[::-1]
	# Compare the strings
	if new_string.lower() == reverse_string.lower():
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

#The replace_ending function replaces the old string in a
#  sentence with the new string, but only if the sentence
#  ends with the old string. If there is more than one 
# occurrence of the old string in the sentence, only the 
# one at the end is replaced, not all of them. For 
# example, replace_ending("abcabc", "abc", "xyz") should
#  return abcxyz, not xyzxyz or xyzabc. The string 
# comparison is case-sensitive, so 
# replace_ending("abcabc", "ABC", "xyz") should return
#  abcabc (no changes made).

'''Solution'''
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = len(sentence)-len(old)
		new_sentence = sentence[0:i] + new
		return new_sentence
	new_sentence = sentence.replace(old, new)

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"