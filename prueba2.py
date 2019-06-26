import morse
from docx import Document

mensaje = input("dime algo: ")
telegrama = morse.toMorse(mensaje)
print(telegrama)

original = morse.toPlain(telegrama)
print(original)

