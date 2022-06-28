def elo_pred(elo_home: float, elo_away: float):
    e_home = 1/(1+10**((elo_away-elo_home)/400))
    e_away = 1/(1+10**((elo_home-elo_away)/400))
    return e_home, e_away    

def elo_update(e_home: float, e_away: float, k:int, result: int):
    match result:
        case 1:
            #heimsieg implementieren
            return 0
        case 0:
            #heimsieg draw
            return 0
        case -1:
            #heimsieg auswärtssieg
            return 0