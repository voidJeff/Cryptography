"""
cryptography.py
Author: Jeff
Credit: None

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
action = input("Enter e to encrypt, d to decrypt, or q to quit: ")
while action != "q":
    associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
    n_num = []
    new_n = []
    action = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if action == "e":
        message = input("Message: ")
        key = input("Key: ")
    
        messagE = list(message)   #message
        n = len(message)        #how many letters
        n_num = [associations.find(x) for x in messagE]  #transformed into numbers
    
        keY = list(key)     #key
        m = len(key)        #how many
        M = m               #a copy
        m_num = [associations.find(x) for x in keY]   #transformed into numbers
    
        while n > 0:
            new_num = n_num[-n] + m_num[-m]
            while new_num > 84:
                new_num -= 85
            new_n.append(new_num)
            m -= 1
            n -= 1
            if m == 0:
                m = M

        new_message = [associations[x] for x in new_n]
        print("".join(new_message))
 
    elif action == "d":
        message = input("Message: ")
        key = input("Key: ")
    
        messagE = list(message)   #message
        n = len(message)        #how many letters
        n_num = [associations.find(x) for x in messagE]  #transformed into numbers
    
        keY = list(key)     #key
        m = len(key)        #how many
        M = m               #a copy
        m_num = [associations.find(x) for x in keY]   #transformed into numbers
    
        while n > 0:
            new_num = n_num[-n] - m_num[-m]
            while new_num < 0:
                new_num = 85 + new_num
            new_n.append(new_num)
            m -= 1
            n -= 1
            if m == 0:
                m = M
             
        new_message = [associations[x] for x in new_n]
        print("".join(new_message))

    else:
        print("Did not understand command, try again.")
print("Goodbye!")



