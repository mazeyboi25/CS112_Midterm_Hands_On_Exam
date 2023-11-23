import random
#   Random number generator
a1 = random.randint(1, 99)
a2 = random.randint(1, 99)
s1 = random.randint(1, 99)
s2 = random.randint(1, 99)
m1 = random.randint(1, 99)
m2 = random.randint(1, 99)
d1 = random.randint(1, 99)
d2 = random.randint(1, 99)
#   Expressions
add = a1 + a2
sub = max(s1, s2) - min(s1, s2)
mult = m1 * m2
division = max(d1, d2) / min(d1, d2)
div = round(division, 2)
#   Addition
sum_input = input(f"What is {a1} + {a2}? ")
sum_final = int(sum_input)
if sum_final == add:
    print("You got the correct answer!")
else:
    print("You got it wrong. :(")
#   Subtraction
difference_input = int(input(f"What is {max(s1, s2)} - {min(s1, s2)}? "))
difference_final = int(difference_input)
if difference_final == sub:
    print("You got the correct answer!")
else:
    print("You got it wrong. :(")
#   Multiplication
product_input = input(f"What is {m1} * {m2}? ")
product_final = int(product_input)
if product_final == mult:
    print("You got the correct answer!")
else:
    print("You got it wrong. :(")
#   Division
quotient_input = float(input(f"What is {max(d1, d2)} / {min(d1, d2)}? "))
quotient_final = quotient_input
if quotient_final == div:
    print("You got the correct answer!")
else:
    print("You got it wrong. :(")
