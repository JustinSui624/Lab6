#Justin Sui
def menu():
    print()
    print('Menu')
    print('-------------')
    print('1.Encode')
    print('2.Decode')
    print('3.Quit')
    
    
def encode(user_password):
    password = []
    for i in iter(str(user_password)):
        s = int(i)+3
        password.append(s)
        
    return password
    
while True:
    menu()
    option = int(input("Please enter an option: "))
    if option ==1:
        user_password = int(input("Please enter your password to encode: "))
        password = encode(user_password)        
        print('Your password has been encoded and stored!')
    elif option==2:
        decoded_password = decode(password)
        password1 = ''.join(str(x) for x in password)
        print("The encoded password is", password1, "and the original password is", decoded_password + ".")
    elif option==3:
        break
        

