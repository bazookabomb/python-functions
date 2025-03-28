def greet():
    print("Hello, dear world!")
    print("End of the greet function.")

greet()

name1 = "Thor"
name2 = "Joel"
list_of_names = ["Katja", "Olga", "Tim"]

# name = parameter
def greet_person(name):
    print("Hello, ", name)
    print("End of the greet_person function.")

# the named argument
greet_person(name=name1)
# name1 = argument
greet_person(name1)
# name2 = argument
greet_person(name2)

# the named argument
greet_person(name="Najat")
greet_person(name="Zito")

# a value as a function argument
greet_person("Hanno")

for name in list_of_names:
    greet_person(name)

