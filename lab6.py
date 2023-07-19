#Justin Sui
def menu():
    print()
    print('Menu')
    print('-------------')
    print('1.Encode')
    print('2.Decode')
    print('3.Quit')
    
    
def encode(user_password):
    count = 0
    encoded_pass = ''
    while count < len(user_password):
        if int(user_password[count]) > 7:
            encoded_pass += str(int(user_password[count]) + 3)
            count += 1
        elif int(user_password[count]) == 7:
            encoded_pass += "0"
        elif int(user_password[count]) == 8:
            encoded_pass += "1"
        elif int(user_password[count]) == 9:
            encoded_pass += "2"
    return encoded_pass

    
while True:
    menu()
    option = int(input("Please enter an option: "))
    if option ==1:
        user_password = int(input("Please enter your password to encode:"))
        password = encode(user_password)        
        print('Your password has been encoded and stored!')
    elif option==2:
        decoded_password = decode(password)
        print("The encoded password is", password, "and the original password is", decoded_password + ".")
    elif option==3:
        break

