import string
import random

# Taken from https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits. Generates random names for each incoming packet. 
def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
