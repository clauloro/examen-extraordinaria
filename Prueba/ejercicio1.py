def puntos_y_cajas(lineas):

    cuadricula = [[0]*3 for _ in range(3)]
    
    lados = { (0, 1): [[0,0], [0,1]], (1, 2): [[0,1], [0,2]], 
              (3, 4): [[1,0], [1,1]], (4, 5): [[1,1], [1,2]], 
              (6, 7): [[2,0], [2,1]], (7, 8): [[2,1], [2,2]], 
              (0, 3): [[0,0], [1,0]], (1, 4): [[0,1], [1,1]], 
              (2, 5): [[0,2], [1,2]], (3, 6): [[1,0], [2,0]], 
              (4, 7): [[1,1], [2,1]], (5, 8): [[1,2], [2,2]] }

    puntuaciones = [0, 0]

    jugador = 1

    for linea in lineas:
        linea = tuple(sorted(linea))
        for caja in lados[linea]:
            cuadricula[caja[0]][caja[1]] += 1
            
            if cuadricula[caja[0]][caja[1]] == 4:
                puntuaciones[jugador-1] += 1
            else:
                
                jugador = 3 - jugador
    
    return tuple(puntuaciones)

print(puntos_y_cajas([(0, 1), (1, 2), (0, 3), (1, 4), (2, 5), (3, 4), (4, 5), (4, 7), (5, 8), (7, 8)]))
