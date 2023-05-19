from agregar import agregar
from modulo import restar
from multiplicar import multiplicar
from dividir import dividir

def main():
    # Pide al usuario que ingrese los números y la operación deseada
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operation = input("Ingrese la operación (+, -, *, /): ")

    # Realiza la operación correspondiente
    if operation == '+':
        result = agregar(num1, num2)
    elif operation == '-':
        result = restar(num1, num2)
    elif operation == '*':
        result = multiplicar(num1, num2)
    elif operation == '/':
        result = dividir(num1, num2)
    else:
        print("Operación inválida")
        return

    # Imprime el resultado
    print("El resultado es:", result)

if __name__ == '__main__':
    main()