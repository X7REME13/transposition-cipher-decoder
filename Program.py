# mensaje cifrado
text = "ITCRNSEEOLAHMEREPUOOSOUOIQCMEEEOIRLHTSEUEUMEXPNRLQNSOAONAPUERRNREIQIQEUE"

# contrasenia para descifrar
key = [3,1,6,4,8,5,2,7]

# Columnas
y = 9

# Filas
x = 8


table = []

for a in range(x):
    table.append(text[a * y: a*y + y])
    # print(key[a], text[a * y: a*y + y])

tableSort = [0 for a in range(x)]

for a in range(x):
    tableSort[key[a] -1] = table[a]

print("Mensaje decodificado: ", end="")

for b in range(x+1):
    for a in tableSort:
        print(a[b], end="")