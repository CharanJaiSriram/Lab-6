# Charan Sriram's Encoder File, Noah adds the decoder to this one

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

def decode(encoded_password):
    decoded_password_list = []
    decoded_num = 0
    for num in encoded_password:
        decoded_num = int(num) - 3
        if decoded_num < 0:
            decoded_num += 10
        decoded_password_list.append(str(decoded_num))
    return "".join(decoded_password_list)


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
            print("The encoded_password is " + stored_password + ", and the original password is " + decode(
                stored_password) + ".")
        # Option to Quit
        elif menu_choice == "3":
            break
