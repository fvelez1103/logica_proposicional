# and_gate.py

# Definimos la función para la compuerta lógica AND
def AND(a, b):
    return a and b

# Creamos una función para generar la tabla de verdad
def truth_table():
    print("A\tB\tAND")
    print("-------------------")
    for a in [False, True]:
        for b in [False, True]:
            and_result = AND(a, b)
            print(f"{int(a)}\t{int(b)}\t{int(and_result)}")

# Llamamos a la función para mostrar la tabla de verdad
if __name__ == "__main__":
    truth_table()