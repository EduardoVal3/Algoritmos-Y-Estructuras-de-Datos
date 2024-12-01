# BinarySearchTreeTester.py
# Prueba interactiva de la clase BinarySearchTree
from BinarySearchTree import *

theTree = BinarySearchTree()  # Comenzar con un árbol vacío

# Insertar algunos datos
theTree.insert("Don", "1974 1")
theTree.insert("Herb", "1975 2")
theTree.insert("Ken", "1979 1")
theTree.insert("Ivan", "1988 1")
theTree.insert("Raj", "1994 1")
theTree.insert("Amir", "1996 1")
theTree.insert("Adi", "2002 3")
theTree.insert("Ron", "2002 3")
theTree.insert("Fran", "2006 1")
theTree.insert("Vint", "2006 2")
theTree.insert("Tim", "2016 1")

def print_commands(names):  # Imprimir una lista de los comandos posibles
    print('Los comandos disponibles son:', names)

def clearTree():  # Eliminar todos los nodos del árbol
    while not theTree.isEmpty():
        data, key = theTree.root()
        theTree.delete(key)

def traverseTree(traverseType="in"):  # Recorrer e imprimir todos los nodos
    for key, data in theTree.traverse(traverseType):
        print('{', str(key), ', ', str(data), '}', end=' ')
    print()

# Lista de comandos con su función asociada y parámetros requeridos
commands = [
    ['print', theTree.print, []],
    ['insert', theTree.insert, ('key', 'data')],
    ['delete', theTree.delete, ('key',)],
    ['search', theTree.search, ('key',)],
    ['traverse', traverseTree, ('type',)],
    ['clear', clearTree, []],
    ['help', print_commands, []],
    ['?', print_commands, []],
    ['quit', None, []],
]

# Recopilar todos los nombres de los comandos en una lista
command_names = ", ".join(c[0] for c in commands)

# Agregar nombres de comandos como argumento para la función print_commands
for i in range(len(commands)):
    if commands[i][1] == print_commands:
        commands[i][2] = [command_names]

# Crear un diccionario que mapea la primera letra del nombre del comando
# con la especificación del comando (nombre, función, parámetros/argumentos)
command_dict = dict((c[0][0], c) for c in commands)

# Imprimir información para el bucle interactivo
theTree.print()
print_commands(command_names)
ans = ' '

# Bucle para recibir un comando del usuario y ejecutarlo
while ans[0] != 'q':  # Continuar mientras no se ingrese 'q' (salir)
    print('El árbol tiene', theTree.nodes(), 'nodos distribuidos en',
          theTree.levels(), 'niveles')
    ans = input("Ingresa la primera letra del comando: ").lower()
    if len(ans) == 0:
        ans = ' '
    if ans[0] in command_dict:
        name, function, parameters = command_dict[ans[0]]
        if function is not None:
            print(name)
            if isinstance(parameters, list):
                arguments = parameters
            else:
                arguments = []
            for param in parameters:
                arg = input("Ingresa " + param + " para el comando " + name + ": ")
                arguments.append(arg)
            try:
                result = function(*arguments)
                print('Resultado:', result)
            except Exception as e:
                print('Ocurrió una excepción')
                print(e)
    else:
        print("Comando no válido: '", ans, "'")
