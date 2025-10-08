full_name = input("Enter your full name (First, Middle, Last): ")

first, middle, last = full_name.split(',')

first = first.capitalize()
middle = middle.capitalize()
last = last.title()

middle_initial = middle[0] + "."

print("Formatted Name:", last + ", " + first + " " + middle_initial)
