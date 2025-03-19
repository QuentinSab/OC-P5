def log_decorator(func):
    def wrapper():
        print("Test avant la fonction.")
        func()
        print("Test après la fonction.")

    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
