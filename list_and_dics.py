from multiprocessing.sharedctypes import Value


def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"Firstname": "Dejesus", "Lastname": "Chaparro"}

    super_list = [
        {"Firstname": "Dejesus", "Lastname": "Chaparro"},
        {"Firstname": "Evelio", "Lastname": "Suarez"},
        {"Firstname": "Gerardo", "Lastname": "Irala"},
        {"Firstname": "Nicolas", "Lastname": "Bogado"},
        {"Firstname": "David", "Lastname": "Vazquez"},
    ]
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.5, 1.2, 4.5, 3.65] 
    }

    for key, value in super_dict.items():
        print(key, "-", value)
if __name__ == "__main__":
    run()