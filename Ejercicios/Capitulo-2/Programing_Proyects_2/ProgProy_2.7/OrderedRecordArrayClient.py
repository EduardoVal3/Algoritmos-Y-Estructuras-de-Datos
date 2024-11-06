from OrderedRecordArray import OrderedRecordArray

def run_tests():
    # Prueba de crecimiento fijo
    print("\nPrueba con crecimiento fijo (incremento de 5):")
    arr_fixed = OrderedRecordArray(initialSize=5, fixedIncrement=5)
    for i in range(15):  # Inserta más elementos para forzar la redimensión
        arr_fixed.insert((chr(65 + i), i))
        print(f"Insertando ({chr(65 + i)}, {i}) - Tamaño máximo: {arr_fixed._OrderedRecordArray__maxSize}")
    print("Array final (crecimiento fijo):", arr_fixed)

    # Prueba de crecimiento multiplicativo
    print("\nPrueba con crecimiento multiplicativo (factor de 2):")
    arr_multiplicative = OrderedRecordArray(initialSize=5, growthFactor=2)
    for i in range(15):  # Inserta más elementos para forzar la redimensión
        arr_multiplicative.insert((chr(65 + i), i))
        print(f"Insertando ({chr(65 + i)}, {i}) - Tamaño máximo: {arr_multiplicative._OrderedRecordArray__maxSize}")
    print("Array final (crecimiento multiplicativo):", arr_multiplicative)

run_tests()
