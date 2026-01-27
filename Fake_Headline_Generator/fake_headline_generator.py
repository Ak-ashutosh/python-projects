import random


subjects = [
    "Sharukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group of Monkeyss",
    "A Begger from delhi",
    "Primer Minster Modi"
]

actions = [
    "Launches",
    "Cancels",
    "Dances with",
    "Declare War",
    "Acts as a",
    "Celebrates",
    "Orders"
]

places = [
    "At Mannat",
    "In Alibag",
    "In Parliment",
    "At India Gate",
    "At Lal Chowk"
]

while True:
    get_subject = random.choice(subjects)
    get_action = random.choice(actions)
    get_places = random.choice(places)

    headline = f" BREAKING NEWS --> {get_subject} {get_action} {get_places} "
    print("\n", headline)

    user_in = input(
        "Do you want to read another headline (yes/no) : ").strip().lower()

    if user_in == 'no':
        break
print("\n Glad to see your reading skills!")
