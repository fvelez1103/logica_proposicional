# implication_gate.py

# Definimos la función para la compuerta lógica Implicación (NOT A OR B)
def implication(a, b):
    return not a or b

# Creamos una función para generar la tabla de verdad
def truth_table():
    print("A\tB\tA → B")
    print("---------------------")
    for a in [False, True]:
        for b in [False, True]:
            implication_result = implication(a, b)
            print(f"{int(a)}\t{int(b)}\t{int(implication_result)}")

# Llamamos a la función para mostrar la tabla de verdad
if __name__ == "__main__":
    truth_table()