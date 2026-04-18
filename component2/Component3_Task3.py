import random


def mail(add, dom):
    """Determines if an email fits the requirements to be valid."""
    if add[-1] == "@" and len(add) >= 3 and dom == 'pop.ac.uk':
        print(add + dom, 'is valid at pop.ac.uk.')
    else:
        print(add + dom, 'is invalid at pop.ac.uk.')
        exit()


def random_string(L):
    """Randomly picks an element from a list and displays it."""
    ele = random.choice(L)
    return ele


def axe(email):
    """Exacts the beginning of an email to return user's name."""
    r = email.find('@')
    o = email[:r]
    return o


def run_it_back(cent):
    """Makes the program end at a given percentage chance."""
    if random.randrange(1, 100) <= cent:
        print("*** NETWORK ERROR ***")
        exit()


def answer(quest, word):
    """Searches through a given question for an exact word within it."""
    quest = quest.casefold()
    word = word.casefold()
    sub = quest[quest.find(word):len(word) + quest.find(word)]
    if sub == word:
        return True
    elif sub != word:
        return False


names = ["Bob", "Jack", "Shanice", "Linda", "Jan"]
go_on = ["Hmmm", "Oh, yes, I see", "Tell me more", "What you said?", "Come again", "I didnt get that"]
done = ["exit", "bye", "done", "leave", "end", "adios", "good day", "so long"]

print("\nWelcome to Pop Chat\nOne of our operators will be pleased to help you today.\n")
E_user = input("Enter your University of Poppleton email address: ")

# Indexing the given email so that it can be used in the mail function.
mail(E_user[:E_user.find("@") + 1], E_user[E_user.find("@") + 1:])

run_it_back(10)

print("Hi",axe(E_user) + "! Thank you, and Welcome to PopChat!")
print("My name is",random_string(names) + ", and it will be my pleasure to help you.")


q = input("What is your question today? ")
# Goes through the done list to see if the user wishes to end the chat.
for x in done:
    if answer(q, x):
        print("\nThanks", axe(E_user), "for using PopChat. See you again soon!")
        exit()
# Sequence of if statements to simulate an actual chat room.
if answer(q, "library"):
    print("The library is closed today.")
elif answer(q, "WIFI"):
    print("WiFi is excellent across the campus.")
elif answer(q, "deadline"):
    print("Your deadline has been extended by two working days.")
elif answer(q, "timetable"):
    print("Timetables will be issued next week.")
elif answer(q, "health"):
    print("Visit our home page under student union should have helpful info else contact your GP.")
elif answer(q, "exam"):
    print("All exams are continuing as scheduled from January 10th")
else:
    # Display random string from the go_on list to prompt user to reenter if their question is not count for.
    print(random_string(go_on))

# While loop that repeats the above.
while True:
    run_it_back(10)
    q = input(": ")
    for x in done:
        if answer(q, x):
            print("\nThanks", axe(E_user), "for using PopChat. See you again soon!")
            exit()
    if answer(q, "library"):
        print("The library is closed today")
    elif answer(q, "WIFI"):
        print("WIFI is excellent across the campus.")
    elif answer(q, "deadline"):
        print("Your deadline has been extended by two working days.")
    elif answer(q, "timetable"):
        print("Timetables will be issued next week.")
    elif answer(q, "health"):
        print("Visit our home page under student union should have helpful info else contact your GP.")
    elif answer(q, "exam"):
        print("All exams are continuing as scheduled from January 10th")
    else:
        print(random_string(go_on))
