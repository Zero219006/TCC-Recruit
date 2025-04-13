import random, math

def random_noise():
    random_characters = ['$', '!', 'p', '-_-', ':D', '~', '@', '#']
    random_index = [random_characters[random.randint(0, len(random_characters) - 1)] for i in range(4)]

    temp = ""
    for i in random_index:
        temp = temp + i

    return temp
## The next line is buggy due to it being hypotenuse(x.b) bu the following line refers to x and y
def hypotenuse(x, y):
    return math.sqrt(x**2 + y**2)

if __name__ == "__main__":
    print("TRY TO STOP THIS FROM BEING PRINTED IN FILE a.py WITHOUT DELETING THIS PRINT STATEMENT")
