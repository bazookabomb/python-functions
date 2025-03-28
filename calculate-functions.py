# definitions
def add_numbers(number1, number2):
    return number1 + number2    


def power(base, exponent=2):
    return base ** exponent


def average(*numbers):
    return sum(numbers) / len(numbers)


# the same average function written in a different way
def avg(*args):
    return sum (args) / len (args)

# **kwargs


# tests
a = 10
b = 20

add_numbers(number1=a, number2=b)
add_numbers(a, b)

c = add_numbers(a, b)
print(f"Die Summe von a={a} und b={b} ist {c}.")

d = add_numbers(c, 5)
print(f"Die Summe von c={c} und 5 ist {d}.")

e = power(b, a) # 20 ** 10
print(f"{b} hoch {a} ist gleich {e}.")

print(f"{a} Quadrat ist {power(a)}.")
print(f"{b} Quadrat ist {power(b)}")

print(f"Der Mittelwert von 10, 20, 30 ist {average(10, 20, 30)}.")
print(f"Der Mittelwert von 1, 2, 3, 4 ist {average(1, 2, 3, 4)}.")

# calculations in multiple steps

price_book = 20
price_movie = 10
price_pen = 2

purchase1 = add_numbers(price_book, price_pen)
purchase2 = add_numbers(price_book, price_movie)
purchase3 = add_numbers(price_book, price_movie)

print(f"Der Mittelwert aller Einkaeufe ist: {average(purchase1, purchase2, purchase3)}")