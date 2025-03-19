# Écrivez votre code ici !
def square(number):
    """
    try :
        return number * number
    except TypeError:
        print("Le paramètre doit être un nombre !")
        return None
    """

    if isinstance(number, (int, float)):
        return number * number
    else:
        print("Le paramètre doit être un nombre !")
        return None
