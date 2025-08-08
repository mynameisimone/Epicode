'''
Scrivi una funzione che data in ingresso una lista A contenente n parole, 
restituisca in output una lista B di interi che rappresentano la lunghezza 
delle parole contenute in A.
'''

#Definiamo una lista di parole da inserire nella variabile "a"
a = ["ciao", "esercizio", "w7d1", "programma", "python"]
#definiamo una variabile "b" vuota in cui inseiremo le lungehezze delle parole 
b = [ ]
for parola in a:#Iniziamo un ciclo for che verrà iterato per ogni parola contenuta nella lista "a"
    b.append(len(parola))#per ogni "parola" della lista "a", il metodo "append" inserirà nella lista "b" la relativa lunghezza

print ("Le parole sono: ", a) #stampiamo il contenuto di "a"
print("La lungezza delle parole rispettivamente è: ", b) #stampiamo il contenuto di "b" con le varie