# not_gate.py

# Definimos la función para la compuerta lógica NOT
def NOT(a):
    return not a

# Creamos una función para generar la tabla de verdad
def truth_table():
    print("A\tNOT A")
    print("--------------")
    for a in [False, True]:
        not_a_result = NOT(a)
        print(f"{int(a)}\t{int(not_a_result)}")

# Llamamos a la función para mostrar la tabla de verdad
if __name__ == "__main__":
    truth_table()