import random


def random_word(words):
    return random.choice(words)


names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]

print("Hello, click [Enter] to start the program", end="")
command = input()
if command == "":
    while True:
        random_name = random_word(names)
        random_place = random_word(places)
        random_verb = random_word(verbs)
        random_noun = random_word(nouns)
        random_adverb = random_word(adverbs)
        random_detail = random_word(details)
        print(f'{random_name} from {random_place} {random_verb} {random_noun} {random_adverb} {random_detail}')
        print('Click [Enter] to generate a new sentence', end="")
        command2 = input()
        if command2 == "":
            continue
        else:
            break