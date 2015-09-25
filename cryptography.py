"""
cryptography.py
Author: Jeff
Credit: None

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
n_num = []
new_n = []
action = input("Enter e to encrypt, d to decrypt, or q to quit: ")
if action == "e":
    message = input("Message: ")
    key = input("Key: ")
    
    messagE = list(message)   #message
    n = len(message)
    n_num = [associations.find(x) for x in messagE]
    
    keY = list(key)     #key
    m = len(key)
    M = m
    m_num = [associations.find(x) for x in keY]
    
    print(n_num)
    print(m_num)
    
    while n > 0:
        new_n.append(n_num[-n] + m_num[-m])
        m -= 1
        n -= 1
    if m == 0:
        m = M
        


