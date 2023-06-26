MOVIMIENTOS_CABALLO = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

from collections import deque

def knight_bfs(start, end, obstaculos):

    obstaculos = set(obstaculos)

    queue = deque([(start, 0)])

    visitados = set([start])

    while queue:
        (x, y), pasos = queue.popleft()

        if (x, y) == end:
            return pasos

        for dx, dy in MOVIMIENTOS_CABALLO:
            nx, ny = x + dx, y + dy

            if (nx, ny) not in obstaculos and (nx, ny) not in visitados:

                queue.append(((nx, ny), pasos + 1))
                visitados.add((nx, ny))

    return None
