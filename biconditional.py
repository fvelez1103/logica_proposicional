# biconditional_gate.py

# Definimos la función para la compuerta lógica Bicondicional (A ↔ B)
def biconditional(a, b):
    return (a and b) or (not a and not b)

# Creamos una función para generar la tabla de verdad
def truth_table():
    print("A\tB\tA ↔ B")
    print("---------------------")
    for a in [False, True]:
        for b in [False, True]:
            biconditional_result = biconditional(a, b)
            print(f"{int(a)}\t{int(b)}\t{int(biconditional_result)}")

# Llamamos a la función para mostrar la tabla de verdad
if __name__ == "__main__":
    truth_table()