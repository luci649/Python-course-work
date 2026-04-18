
print("Stop! Who would cross the Bridge of Death?\nMust answer me these questions three, 'ere the other side he see.\n")

name = input("What is your name? ")
if name == "Arthur":
    print("My liege! You may pass!")
    exit()

seek = input("What do you seek? ")
if not seek[seek.find("grail"):seek.find("grail")+5]:
    print("Only those who seek the Grail may pass.")
    exit()

colour = input("What is your favourite colour? ")
if name.casefold()[0] != colour.casefold()[0]:
    print("Incorrect! You must now face the Gorge of Eternal Peril.")
else:
    print("You may pass!")
