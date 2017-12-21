antigo = 0
novo = 1

def fibonacci(sequencia):
    global antigo, novo
    if sequencia != 0:
        print novo

    else:
        return True

    antigo, novo = novo, antigo + novo
    fibonacci(sequencia - 1)

if __name__ == "__main__":
    fibonacci(5)