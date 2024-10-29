tweets = [
    {"user": "pablo", "post": "hola mundo, este es mi primer tweet"},
    {"user": "pablo", "post": "esta red social es la bomba"},
    {"user": "borja", "post": "mi clase de hoy ha ido genial"},
    {"user": "borja", "post": "ha sido explosiva"},
    {"user": "ana", "post": "mataría por una cocacola"}
]

contadores = {}
diccionario = {}

for t in tweets:
    user = t["user"]
    post = t["post"]
    if (user not in contadores):
        contadores[user] = 1
    else:
        contadores[user] = contadores[user] + 1

print(contadores)

for t in tweets:
    user = t["user"]
    post = t["post"]
    if (user not in diccionario):
        diccionario[user] = [ post ]
    else:
        # diccionario[user].append(post)
        diccionario[user] = diccionario[user] + [ post ]

print(diccionario)