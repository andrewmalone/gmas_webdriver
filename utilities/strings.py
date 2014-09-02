import string
import random


def string_generator(size=6, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))


def random_string(size=6, lowercase=True, uppercase=True, numbers=False):
    chars = ''
    if lowercase is True:
        chars += string.ascii_lowercase
    if uppercase is True:
        chars += string.ascii_uppercase
    if numbers is True:
        chars += string.digits
    return string_generator(size, chars)


def random_sentence(words=5):
    return ' '.join(random_string(random.randint(2, 10), uppercase=False) for _ in range(words)).capitalize()


if __name__ == "__main__":
    print random_sentence()
