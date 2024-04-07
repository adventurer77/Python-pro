import re

# Task 1

my_string = input("Enter>> ")

pattern = r"R{1}[b]+[r]{1}"

result = re.findall(pattern, my_string) # fRbbrsdfrbbrs RbRew3gsRbrf32erwbvweRbbbbbbr
print (*result)

match = re.search(pattern,my_string)
if match:
    print(match.group())
else:
    print("pattern not found")

# Task 2 

def valid_bank_card(my_card):
    """
    Checks the correctness of the card.

    Arguments:
    my_card: String with card numbers.

    Return:
    Valid if the card numbers is correct, False otherwise.
    """

    pattern = r"^[1-9]{4}-{1}[1-9]{4}-{1}[1-9]{4}-{1}[1-9]{4}$" 

    match = re.search(pattern,my_card)

    if match:
        return(f"Card {match.group()} is valid.")
    else:
        return("Wrong card number.Try again.")


print(valid_bank_card(input("Enter card number. Example 9999-9999-9999-9999 >> "))) # 9999-9999-9999-9999


# Task 3


def checking_mail(email):
  """
  Checks if the email address is valid.

    Arguments:
      email: a string containing an email address.

    Return:
      True if the email address is valid, False otherwise.
  """

  
  pattern = re.compile(r"""
    ^[a-zA-Z0-9_.+-]+
    @[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$
  """, re.X)

  # Checks whether the email matches the template.
  if not pattern.match(email):
    return False

  # Checks that the first character of an email is not "_" and "-".
  if email[0] in ["_", "-"]:
    return False

  # Checks whether the character "-" is repeated.
  if "--" in email:
    return False

  return True

email1 = "user@example.com"
email2 = "user_name@example.com"
email3 = "user-name@example.com"
email4 = "_user@example.com"
email5 = "user@examp--le..com"

print(f"Email {email1} valid: {checking_mail(email1)}")
print(f"Email {email2} valid: {checking_mail(email2)}")
print(f"Email {email3} valid: {checking_mail(email3)}")
print(f"Email {email4} valid: {checking_mail(email4)}")
print(f"Email {email5} valid: {checking_mail(email5)}")

# Task 4


def valid_login(my_login):
    """
    Checks the correctness of the login.

    Arguments:
      my_login: String with login.

    Return:
      True if the login is correct, False otherwise.
    """

    letter  = False
    number = False

    for i in my_login:
        if i.isalpha():
            letter = True
        elif i.isdigit():
            number = True

    if not letter or not number:
        return False

    pattern =  re.compile(r"^[a-zA-Z0-9]{2,10}$")

    if not pattern.match(my_login):
        return False

    return True

# login1 = "u2s3e4r"
# login2 = "username"
# login3 = "1234567890"
# login4 = "_user"
# login5 = "user@"
# login6 = "1user"
# login7 = "123f"

# print(f"Login {login1} valid: {valid_login(login1)}")
# print(f"Login {login2} valid: {valid_login(login2)}")
# print(f"Login {login3} valid: {valid_login(login3)}")
# print(f"Login {login4} valid: {valid_login(login4)}")
# print(f"Login {login5} valid: {valid_login(login5)}")
# print(f"Login {login6} valid: {valid_login(login6)}")
# print(f"Login {login7} valid: {valid_login(login7)}")    
print(valid_login(input("Enter> ")))