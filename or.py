# or_gate.py

# Definimos la función para la compuerta lógica OR
def OR(a, b):
    return a or b

# Creamos una función para generar la tabla de verdad
def truth_table():
    print("A\tB\tOR")
    print("------------------")
    for a in [False, True]:
        for b in [False, True]:
            or_result = OR(a, b)
            print(f"{int(a)}\t{int(b)}\t{int(or_result)}")

# Llamamos a la función para mostrar la tabla de verdad
if __name__ == "__main__":
    truth_table()