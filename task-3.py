import random
import string

def generate_password(length, lowercase=True, uppercase=True, digits=True, symbols=True):
  """Generates a random password based on user-specified complexity.

  Args:
      length (int): Desired length of the password (minimum 8 characters).
      lowercase (bool, optional): Include lowercase letters (default: True).
      uppercase (bool, optional): Include uppercase letters (default: True).
      digits (bool, optional): Include digits (default: True).
      symbols (bool, optional): Include symbols (default: True).

  Raises:
      ValueError: If no complexity options are chosen or password length is less than 8.

  Returns:
      str: The generated password.
  """

  # Define character sets
  characters = []
  if lowercase:
    characters.extend(string.ascii_lowercase)
  if uppercase:
    characters.extend(string.ascii_uppercase)
  if digits:
    characters.extend(string.digits)
  if symbols:
    characters.extend(string.punctuation)

  # Ensure at least one character type is included
  if not characters:
    raise ValueError("Please choose at least one complexity option (lowercase, uppercase, digits, or symbols).")

  # Ensure minimum password length
  if length < 8:
    raise ValueError("Password length must be at least 8 characters.")

  # Generate password using random selection
  password = ''.join(random.choice(characters) for _ in range(length))
  return password

def main():
  """Prompts user for password complexity and displays generated password."""
  try:
    length = int(input("Enter desired password length (minimum 8 characters): "))
    lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
    uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
    digits = input("Include digits (y/n)? ").lower() == 'y'
    symbols = input("Include symbols (y/n)? ").lower() == 'y'
  except ValueError as e:
    print("Invalid input:", e)
    return

  # Generate and display password
  password = generate_password(length, lowercase, uppercase, digits, symbols)
  print("Your generated password is:", password)

if __name__ == "__main__":
  main()