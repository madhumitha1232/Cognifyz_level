import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Define a function for
# for validating an Email
def check(email):

	# pass the regular expression
	# and the string into the fullmatch() method
	if(re.fullmatch(regex, email)):
		print("Valid Email")

	else:
		print("Invalid Email")

# Driver Code
if __name__ == '__main__':

	# Enter the email
	email = "kavallimadhumitha@gmail.com"

	# calling run function
	check(email)

	email = "my.ownsite@our-earth.org"
	check(email)