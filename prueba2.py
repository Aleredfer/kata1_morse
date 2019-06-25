import morse
import time

mensaje = input("dime algo: ")
telegrama = morse.toMorse(mensaje)
print(telegrama)

original = morse.toPlain(telegrama)
print(original)

print(time.strftime("%d/%m/%Y", time.gmtime()))