#Charan Sriram's Encoder File, Noah adds the decoder to this one

# Encoder function
def encode(password):
	encoded_list = []
	encoded_num = 0
	for num in password:
		encoded_num = int(num) + 3
		if encoded_num > 9:
			encoded_num -= 10
		encoded_list.append(str(encoded_num))
	return "".join(encoded_list)

# Decoder Function

# Main
if __name__ == '__main__':
	stored_password = ""
	while True:
		print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit \n ")
		menu_choice = input("Please enter an option: ")
		# Option for Encoder
		if menu_choice == "1":
			input_password = input("Please enter your password to encode: ")
			stored_password = encode(input_password)
			print("Your password has been encoded and stored! \n")
		# Option for Decoder
		elif menu_choice == "2":
			pass
		# Option to Quit
		elif menu_choice == "3":
			break
