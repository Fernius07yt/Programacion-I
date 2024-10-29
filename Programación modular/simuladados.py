import random

tiradas = []

for _ in range(10):
    tirada = random.randint(1, 100)
    tiradas.append(tirada)

contadores = {}

for n in tiradas:
    if (n not in contadores):
        contadores[n] = 1
    else:
        contadores[n] = contadores[n] + 1
    
print(contadores)





candidatos = [ "Pablo", "Borja", "MLuz", "Ana", "Jenny", "Xabi" ]

votos = []

# Simular 300 votos...
for _ in range(300):
    voto = random.choice(candidatos)
    votos.append(voto)

# Contar votos
contadores = {}

for v in votos:
    if (v not in contadores):
        contadores[v] = 1
    else:
        contadores[v] = contadores[v] + 1

print(contadores)


