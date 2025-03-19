# Fonction calculate_average
def calculate_average(list_numbers):
    average = 0
    for number in list_numbers:
        average += number

    return average / len(list_numbers)


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", round(average, 2))
