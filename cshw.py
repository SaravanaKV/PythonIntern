import re
def get_valid_input(prompt, validation_regex):
    while True:
        user_input = input(prompt)
        if re.match(validation_regex, user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")
            
# Get user information
first_name = get_valid_input("Enter your first name: ", r'^[A-Za-z]+$')
last_name = get_valid_input("Enter your last name: ", r'^[A-Za-z]+$')
age = get_valid_input("Enter your age: ", r'^\d+$')
phone_number = get_valid_input("Enter your phone number: ", r'^\d{10}$')
email = get_valid_input("Enter your email id: ", r'^\S+@\S+\.\S+$')

# Capitalize names
first_name = first_name.capitalize()
last_name = last_name.capitalize()
# Print user information
print("\nUser Information:")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Age: {age}")
print(f"Phone Number: {phone_number}")
print(f"Email ID: {email}")
