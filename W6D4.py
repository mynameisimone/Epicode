import math # è una libreria, in questo caso ci serve per il valore pi greco


def scelta_utente(scelte_possibili:list[int]) -> int:
    print()
    print("Scegli un'opzione tra le seguenti:")
    if 1 in scelte_possibili:#se 1 è tra scelte_possibili comparirà "1) Perimetro e area del quadrato"
        print("\t1) Calcolare perimetro e area del quadrato")
    
    if 2 in scelte_possibili:#Se 2 è tra scelte_possibili coparirà "2) Perimetro e area del cerchio")
        print("\t2) Calcolare perimetro e area del cerchio")
    
    if 3 in scelte_possibili:#Se 3 è tra scelte_possibili coparirà "3) Perimetro e area del rettangolo"
        print("\t3) Calcolare perimetro e area del rettangolo")

    ok = False

    while not ok:
        #se l'utente inseirsce un valore non numerico, la conversione di tale valore in intero non andrà a buon fine e genererà un'eccezione
        try:
            print()
            opzione:int = int(input("Scegli: "))
            if opzione in scelte_possibili:#questa stringa controlla se l'input è qualcosa che non è già stato scelto che rientra in scelte_possibili
                ok = True #se l'opzione scelta è tra le scelte possibili "ok" è True e si esce dal ciclo
            else:
                print(f"La tua scelta ({opzione}) non andava bene!")#altrimenti viene satmpata questa stringa indicando che il valore inserito, memorizzato in "opzione" non è valido

        except ValueError:#se il valore inserito non è numerico viene generata quest'eccezione che stamperà "Dammi un valore numerico!!"
            print("Dammi un valore numerico!!")

    return opzione


ok = False
while not ok:#Questo ciclo While chiede di inseirre un valore finché non si inserisce un volore numerico
    try:
        valore:float = float(input("Inserici un valore tramite il quale calcolerò il perimetro e l'area della figura scelta: "))#per capire se il valore inseritò sarà un valore numerico tenterà di convertire l'input in un valore di tipo float, se non ci riesce restituisce un'eccezione
        ok = True #"ok" verrà settato su "False" e ricomincerà il ciclo finché non riceverà un valore numerico

    except ValueError:#Se l'input non è un valore numerico l'eccezione viene catturata in "ValueError", verrà stamapto il testo "Dammi un valore numerico"
        print("Dammi un valore numerico!!")

#Se il valore inserito in precedenza è un valore numerico, viene convertito in float. Quindi inizializziamo le variabili "perimetro" e "area" a zero
perimetro: float = 0.0
area: float      = 0.0

scelte_possibili = [1, 2, 3] #Definizione della lista con le scelte possibili
while len(scelte_possibili) > 0:
    opzione = scelta_utente(scelte_possibili)
    
    scelte_possibili.remove(opzione)#rimuoviamo elementi dalle scelte possibili in base alla "secelta_utente", se sceglie 1 rimuove 1 e così anche per le altre due.

    # quadrato - Se viene scelta l'opzione 1 viene calcolato perimetro e area del quadrato
    if opzione == 1:
        perimetro = valore * 4
        area      = valore * valore

    # cerchio - Se viene scelta l'opzione 2 viene calcolato perimetro e area del cerchio
    elif opzione == 2:
        perimetro = 2 * math.pi * valore
        area      = valore * valore * math.pi

    # rettangolo - Se viene scelta l'opzione 3 viene calcolato perimetro e area del rettangolo
    elif opzione == 3:
        # lato corto (l) è metà lato lungo (L)
        # ( 2 * L + 2 * l ) = ( 2 * L + L ) = ( 3 * L )
        perimetro = 3 * valore
        area      = valore * valore / 2

    #questa eccezione non si verificherà mai perché se si inserisce un'opzione non valida non si arriverà mai a questo punto
    else:
        raise Exception("Eccezione Impossibile!!!!11!!1!11!")

    valore = area #Il contenuto di "valore" che verrà usato nel prossimo giro verrà impostato con il contenuto della variabile "area" appena calcolato

    #stampiamo perimetro e area e il ciclo ricomincerà
    print()
    print(f"Il perimetro della figura selta è {perimetro:.2f}")
    print(f"L'area della figura scelta è {area:.2f}")






