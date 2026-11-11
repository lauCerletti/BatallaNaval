def mostrarTablero(lista):
    """Se encarga de mostrar la matriz"""
    coordsX = [1,2,3,4,5,6,7,8,9,10]
    coordsY = "ABCDEFGHIJ"
    print(*coordsX,sep=' ')
    for i in range(len(lista)):
        print(*lista[i]) # el asterisco elimina los corchetes y las comas


def tablero():
    """Generacion de tablero. 10x10.
    El 0 representa el agua"""
    Tablero = []
    for i in range(10):
        fila = []
        for i in range(10):
            fila.append([0])
        Tablero.append(fila)
    return Tablero

tablero()
mostrarTablero(tablero())