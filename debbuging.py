def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    while True:
        try:
            num = (input("Ingresa un numero: "))
            assert num.isnumeric(), "Debes ingresar un número"
            if num < 0:
                raise ValueError
            print (divisors(num))
            print("Terminó mi programa")
            break
        except ValueError:
            print("Debes ingresar un numero positivo.")



if __name__ == '__main__':
    run()