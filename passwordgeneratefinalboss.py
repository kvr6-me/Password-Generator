import random
import string

length = int(input("Enter the desired password length<3: "))


def passwordy(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password_chars = random.choices(characters, k=length)

    return "".join(password_chars)


if __name__ == "__main__":
    for i in range(10):
        password = passwordy(length)
        print(f"Password {i+1}: {password}")
