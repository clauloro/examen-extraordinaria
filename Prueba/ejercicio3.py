def evaluar_mano(mano, comunitarias):
    ranks = '23456789TJQKA'
    mano = mano + comunitarias
    mano_ranks = ''.join(sorted([r for r, s in mano], key=ranks.index, reverse=True))
    mano_suits = ''.join([s for r, s in mano])
    
    def escalera(ranks):
        return len(set(ranks)) == 5 and ranks.index(ranks[0]) - ranks.index(ranks[-1]) == 4

    def mismo_palo(suits):
        return len(set(suits)) == 1

    def contar_rangos(ranks):
        return ''.join(sorted(ranks, key=ranks.count, reverse=True))

    def cuatro_iguales(ranks):
        return ranks.count(ranks[0]) == 4 or ranks.count(ranks[-1]) == 4

    def full_house(ranks):
        return ranks.count(ranks[0]) == 3 and ranks.count(ranks[-1]) == 2 or ranks.count(ranks[0]) == 2 and ranks.count(ranks[-1]) == 3

    def tres_iguales(ranks):
        return ranks.count(ranks[0]) == 3 or ranks.count(ranks[-1]) == 3 or ranks.count(ranks[2]) == 3

    def dos_pares(ranks):
        pairs = [r for r in set(ranks) if ranks.count(r) == 2]
        return len(pairs) == 2

    def un_par(ranks):
        pairs = [r for r in set(ranks) if ranks.count(r) == 2]
        return len(pairs) == 1

    if escalera(mano_ranks) and mismo_palo(mano_suits):
        return 'escalera de color', mano_ranks
    elif cuatro_iguales(mano_ranks):
        return 'four of a kind', contar_rangos(mano_ranks)
    elif full_house(mano_ranks):
        return 'full house', contar_rangos(mano_ranks)
    elif mismo_palo(mano_suits):
        return 'color', mano_ranks
    elif escalera(mano_ranks):
        return 'directo', mano_ranks
    elif tres_iguales(mano_ranks):
        return 'three of a kind', contar_rangos(mano_ranks)
    elif dos_pares(mano_ranks):
        return 'doble pareja', contar_rangos(mano_ranks)
    elif un_par(mano_ranks):
        return 'pareja', contar_rangos(mano_ranks)
    else:
        return 'nada', mano_ranks
