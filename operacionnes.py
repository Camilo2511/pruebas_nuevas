def dividir(a, b):
    return a / b

__main__ = __name__ == "__main__"
if __main__:
    num1 = float(input("digite un numero a dividir:")) 
    num2 = float(input("digite el segundo numero a dividir:"))
    resultado = dividir(num1, num2)
    print(f"el resusltado de la divicion es {resultado}")