import random

loteria = [(1, 'gallo'), (2, 'diablito'), (3, 'dama'), (4, 'catrin'), (5, 'paraguas'), (6, 'sirena'), (7, 'escalera'),
           (8, 'botella'), (9, 'barril'), (10, 'arbol'), (11, 'melon'), (12, 'valiente'), (13, 'gorrito'),
           (14, 'muerte'), (15, 'pera'), (16, 'bandera'), (17, 'bandolon'), (18, 'violoncello'), (19, 'garza'),
           (20, 'pajaro'), (21, 'mano'), (22, 'bota'), (23, 'luna'), (24, 'cotorro'), (25, 'borracho'), (26, 'negrito'),
           (27, 'corazon'), (28, 'sandia'), (29, 'tambor'), (30, 'camaron'), (31, 'jaras'), (32, 'musico'),
           (33, 'arania'), (34, 'soldado'), (35, 'estrella'), (36, 'cazo'), (37, 'mundo'), (38, 'apache'),
           (39, 'nopal'), (40, 'alacran'), (41, 'rosa'), (42, 'calavera'), (43, 'campana'), (44, 'cantarito'),
           (45, 'venado'), (46, 'sol'), (47, 'corona'), (48, 'chalupa'), (49, 'pino'), (50, 'pescado'), (51, 'palma'),
           (52, 'maceta'), (53, 'arpa'), (54, 'rana')]

card = []
cards = []
cards_ordered = []


def get_random():
    a = random.randint(1, 54)
    while card.count(a) >= 1:
        a = random.randint(1, 54)
    else:
        return a


def get_position():
    return random.randint(1, 16)


def create_card():
    card.clear()
    for i in range(1, 16):
        x = get_random()
        if i < 15:
            card.append(x)
            # card.append(loteria[x])
        else:
            p = get_position()
            card.insert(p, x)
            # card.insert(p, loteria[x])
            p = get_position()
            card.insert(p, x)
            # card.insert(p, loteria[x])


def create_cards():
    for i in range(1, 50):
        create_card()
        d = card.copy()
        d.sort()
        while d in cards_ordered:
            create_card()
            d = card.copy()
            d.sort()
        else:
            cards.append(card.copy())
            cards_ordered.append(d)


create_cards()
print(f'cards = ', cards)
print(f'cards_ordered = ', cards_ordered)
print()
