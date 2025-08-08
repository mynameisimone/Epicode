
'''
Scrivi una funzione generatrice di password. 
La funzione deve generare una stringa alfanumerica di 8 caratteri qualora 
l'utente voglia una password semplice, o di 20 caratteri ascii qualora 
desideri una password più complicata.
'''


import string #importiamo la libereria "string" per lavorare con stringhe/insieme di caratteri
import random #importaiamo la libreria "random" che serve a generare numeri casuali

ALFANUMERICI = string.ascii_lowercase + string.ascii_uppercase +string.digits #dentro ALFANUMERICI mettiamo una serie di costanti contenute nella libreria "string", rsipettivamente caratteri minuscoli, maiuscoli e numeri
TUTTI_ASCII  = ALFANUMERICI + string.punctuation #creiamo una variabile TUTTI_ASCII in cui inseiriamo ALFANUMERICI aggiungendo caratteri di punteggiatura contenuti nella libreria string "string.punctuation"

def generate_password(lenght:int, charset:str) -> str:
    #definiamo una funzione "generate_password"
    #che riceve una lunghezza della psw desiderata 
    #e una stringa con i caratteri per generare la password
    password = [] #Creiamo una lista che conterrà i caratteri della password
    for i in range(0, lenght): 
        #iniziamo un ciclo che si ripete "lenght" volte per generare ogni carattere della password
        letter = random.choice(charset) #sceglie una lettera a caso da charset: random.choiche
        password.append(letter)#aggiunge "append" il carattere scelto alla fine di della lista "password"



    return ''.join(password)
    #"join" serve per unire una sequenza di stringhe in una unica, ciò che viene orima è esattamente ciò che unirà le stringe
    # Noi non mettiamo nienete ('') così i caratteri risulteranno attaccati


scelta = input("Si desidera una password complessa o semplice?\nc = complessa\ns = semplice\nScelta: ")#Chiediamo in input all'utenete di scegliere tra una password complessa e una semplice
if scelta.lower() == "c":#Se la scelta è c
    password = generate_password(20, TUTTI_ASCII)#la password sarà di 20 caratteri dove il charset è "TUTTI_ASCII"
    print("Password complessa generata:",password)

elif scelta.lower() == "s":#se la scelta è s = semplice
    password = generate_password(8, ALFANUMERICI)#la password sarà di 8 caratteri alfanumerici
    print("Password semplice generata:",password)
else:
    print("Scelta non valida.")#se viene iserito qualsiasi carattere eccetto "c" ed "s" verrà visualizzato il messaggio "Scelta non valida"

