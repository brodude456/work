import random


def take_second(element):
    return element[1]


import string


def get_random_name():
    name = ""
    for i in range(random.randint(5, 15)):
        name += random.choice(string.ascii_letters)
    return name


imenik = [(777, "zejneba"), (324, "fahro"), (23, "fatih"), (2334, "muamer"), (435, "kerim"),(4568,"zzzzzzz")]

print(sorted(imenik,key=take_second))
for i in range(100000):
    novi_element = (random.randint(1, 10000), get_random_name())
    imenik.append(novi_element)

imenik.sort(key=take_second)
print(imenik)

name = input('enter a name: ')

min_index = 0
max_index = len(imenik)

previous_guess_name = ""
counter = 0
while True:

    mid_index = (max_index + min_index) // 2
    guess_score = imenik[mid_index][0]
    guess_name = imenik[mid_index][1]

    if guess_name == previous_guess_name:
        print("Not found")
        break

    if guess_name == name:
        print("your score is", guess_score)
        break
    elif name > guess_name:
        min_index = mid_index
    else:
        max_index = mid_index

    previous_guess_name = guess_name
    counter += 1

print("Number of comparisons", counter)

print("after")
found = False
counter = 0
for i in range(len(imenik)):
    counter += 1
    if imenik[i][1] == name:
        print("your score is", guess_score)
        found = True
        break

if not found:
    print("Not found")

print("Number of comparisons after", counter)
