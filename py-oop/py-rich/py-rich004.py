from rich.traceback import install

install()

def divisao(x, y):
    try:
        div = x / y
        return f"{div:.2f}"
    except ZeroDivisionError:
        return f"divisor não pode ser zero."

    
print(divisao(20,0))
