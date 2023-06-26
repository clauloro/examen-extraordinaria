def potencia(base, exponente):
    if exponente < 0:
        return None
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

print(potencia(2, 3))  
print(potencia(10, 0))  
print(potencia(-5, 3)) 
print(potencia(-4, 2))  
