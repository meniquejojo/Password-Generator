import string
import secrets

def generate_password(length=12,special_character='yes',digits='yes'):
    
    if special_character.lower() =='yes':
        if digits =='yes':
            characters = string.ascii_letters + string.punctuation +string.digits
        else:
            characters = string.ascii_letters +string.punctuation 
    else:
        if digits =='yes':
            characters = string.ascii_letters +string.digits
        else:
            characters = string.ascii_letters 
    # Generate the password using a secure random choice from the defined characters
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password

# Get user input for password length
password_length = int(input("Enter password length: "))
special_character=input('Do you want a special character?')
digits = input('Do you want digits in your password?')

# Generate and display the password
generated_password = generate_password(password_length,special_character,digits)
print(f"Your generated password is : {generated_password}")