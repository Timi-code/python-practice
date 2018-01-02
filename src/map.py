def normalize(name):
    return name.capitalize()


def normalize2(name):
    return name[0:1].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize2, L1))

print(L2)
