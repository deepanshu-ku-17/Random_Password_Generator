import string
import random

def generate_password(length):
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digit=string.digits
    punctuation=string.punctuation
    s=[]
    s.extend(list(lowercase))
    s.extend(list(uppercase))
    s.extend(list(digit))
    s.extend(list(punctuation))
    random.shuffle(s)
    PASSWORD = "".join(s[0:length])
    return PASSWORD

if __name__=="__main__":
    while True:
        try:
            length=int(input("ENTER THE LENGTH OF YOUR PASSWORD::> "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("INVALID LENGTH, PLEASE ENTER THE POSITIVE INTEGER::>")

    PASSWORD = generate_password(length)
    print("YOUR PASSWORD IS::> ", PASSWORD)

    # Evaluate password strength
    has_lowercase = any(c.islower() for c in PASSWORD)
    has_uppercase = any(c.isupper() for c in PASSWORD)
    has_digit = any(c.isdigit() for c in PASSWORD)
    has_special = any(c in string.punctuation for c in PASSWORD)
    is_strong = len(PASSWORD) >= 8 and has_lowercase and has_uppercase and has_digit and has_special
    if is_strong:
        print("THE STRONG PASSWORD IS...")
    else:
        print("THIS COULD BE A STRONG PASSWORD.")