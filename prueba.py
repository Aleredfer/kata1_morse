letras = "ABCDEFGHIJKLMNÑOPSRSTUVWXYZ"
simbolos = ['·—','—···','—·—·','—··','·','··—·','——·','····','··','·———','—·—','·—··','——','—·','——·——','———','·——·','——·—','·—·','···','—','··—','···—','·——','—··—','—·——','——··','—————','·————','··———','···——','····—','·····','—····','——···','———··','————·','·—·—·—','—·—·——','··——··']

cadena = 'Hola, mundo'.upper()


for letra in cadena:
    posicion = 0
    while posicion < len(letras):
        l = letras[posicion]
        if l == letra:
            break
        posicion += 1

    if posicion == len(letras):
        print('no encontrado')
    else:
        #obterner simbolo morse de posion = posicion
        print("{} - {}".format(letra, simbolos[posicion]))
