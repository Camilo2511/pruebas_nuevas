def multiplica(a, b):
    return a * b

__main__ = __name__ == "__main__"
if __main__:
    num1 = float(input("digite un numero a multiplicar:")) 
    num2 = float(input("digite el segundo numero a multiplicar:"))
    resultado = multiplica(num1, num2)
    print(f"el resusltado de la multiplicacion es {resultado}")