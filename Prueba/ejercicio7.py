def will_survive(attackers, defenders):
    attacker_power = sum(attackers)
    defender_power = sum(defenders)
    
    attacker_survivors = 0
    defender_survivors = 0
    
    if len(attackers) == len(defenders):
        for i in range(len(attackers)):
            if attackers[i] > defenders[i]:
                attacker_survivors += 1
            elif attackers[i] < defenders[i]:
                defender_survivors += 1
    else:
        if len(attackers) > len(defenders):
            attacker_survivors = len(attackers) - len(defenders)
        else:
            defender_survivors = len(defenders) - len(attackers)
            
    if defender_survivors > attacker_survivors:
        return True
    elif defender_survivors < attacker_survivors:
        return False
    else:
        return defender_power >= attacker_power
    
