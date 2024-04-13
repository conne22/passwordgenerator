import random

# Define lists of characters
nummer = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Initialize variables
passwords = []
howmuchp = 0

# Combine lists
nummer.extend(text)


# Main loop
while True : 
    try:
        styrka = int(input("how good password do you need? choose between 1-10 in password power "))
        if 1 <= styrka <= 10:
            styrka = (styrka) * 4
            password = "".join(random.choice(nummer) for _ in range(styrka))
            passwords.append(password)
            howmuchp += 1
                
            print("Du har valt styrka:", password)
            print("Ammount: ", howmuchp, " Passwords: ", passwords)
            if len(passwords) >=10:
                break
        else:
            print("choose a number between  1-10")
    except ValueError:
        print("password strength is between 1-10")        




