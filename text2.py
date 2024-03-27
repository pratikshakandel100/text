name = input("Enter your full name")
for letter in name:
    print(f"{letter}:{name.count(letter)}")

