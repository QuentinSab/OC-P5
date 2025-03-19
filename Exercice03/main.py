words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

vowels = "aeiouyAEIOUY"

tuples = []

for word in words:
    vowel_count = 0

    for letter in word:
        if letter in vowels:
            vowel_count += 1

    tuples.append((word, vowel_count))

print(tuples)