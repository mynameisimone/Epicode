#include <stdio.h>
#include <ctype.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define DEFAULT_NAME "----UNSET----" //inseriamo "----UNSET----" in DEFAULT_NAME

//DICHIARAZIONE DELLE FUZIONI
int partita(); //funzione che ritorna un valore intero e non ha nessun valore in input
int domanda(char*,int);
bool contains(int*, int);

int main() {
    // Presentare una rapida introduzione all'utente con lo scopo del programma
    char *intro = "Benvenutə al quiz più inutile del mondo, 2 domande ma solo una risposta è corretta! In premio tanta gloria per chi vincerà!";
    printf("%s\n\n", intro);


    char *prompt_scelta = "Scegli tra:\n\tA) Iniziare una nuova partita\n\tB) Uscire dal gioco";
    char scelta;
    int score = 0;
    char nome[512] = DEFAULT_NAME; //allocazione di 512 bite a nome 


    while(true) { 
        // Mostrare allʼutente un menu di scelta iniziale tra: A) Iniziare una nuova partita; B) Uscire dal gioco
        // Questo ciclo sarà infinito finché non si sceglie di uscire dal gioco
        printf("%s\n", prompt_scelta);


        // Ricevere in input la scelta dellʼutente
        printf("\nComunicami la tua scelta: ");
        scanf(" %c", &scelta);

        // Creare o meno una nuova partita in base allʼinput utente
        switch(tolower(scelta)) {
            case 'a':
                if(strcmp(nome, DEFAULT_NAME) == 0) { // se il valore inserito diverso a "----UNSET----" (strcmp confronta le due stringhe)...
                    printf("\nInserisci il tuo nome: ");//stampa "inserici il tuo nome"
                    scanf("%s", nome);//inserisce l'input dell'utente nella variabile nome
                    printf("\n");
                }
                score += partita(); //inizia la partita
                break;
            case 'b':
                printf("Congratulazioni %s, il tuo risultato è: %d\n", nome, score);
                return 0;
            default:
                printf("scelta sbagliata\n");
                break;
        }
    }    
}

int partita() { //Funzione "partita" 
    int score = 0; //inizializziamo score a 0

    score += domanda( //somma il risultato della funzione "domanda()" alla variabile "score". Ogni volta che la risposta è corretta "score" aumenta di 1
        "Chi ha creato il linguaggio di programmazione C?\n\t1) Bill Gates\n\t2) Dennis Ritchie\n\t3) Elon Musk\n",
        2 //secondo argomento della funzione "domanda" e indica che 2 è la risposta corretta
    );

    score += domanda(
        "Cosa fa la funzione 'scanf' in C?\n\t1) Prende input da tastiera\n\t2) Stampa qualcosa\n\t3) Compila il programma\n",
        1
    );
    
    return score; //alla fine della funzione partita(), viene restituito il punteggio totale
}


// controlla che l'elemento sia contenuto nell'array, quindi che la scelta sia dentro "possible_answers")
bool contains(int *arr, int element) { //funzione che ritorna un valore booleano (vero/falso), accetta un array di interi (*arr è il puntatore al primo elemneto dell'array)
    for(int i=0; i<sizeof(arr); i++) { // inizializza l'indice a 0, finché l'indice è minore alla dimensione dell'array, esegue il codice che sta dentro e, alla fine di ogni iterazione aumenta "i" di uno
        if(arr[i] == element) { // confronta l'elemento "i" dell'array con il valore corretto "element" e se coincidono
            return true; //ritorna vero, altimenti ricomincia il ciclo fino a quando "i" sarà inferiore alla dimensione dell'array
        }
    }
    return false;
}


// generalizza il processo per il quiz
//"domanda" è una funzione che pone la domanda che viene passata e confronta la risposta con la risposta corretta
int domanda(char *d, int correct) {
    int scelta;//inizializza la variabile "scelta" in cui salverà la scelta
    int possible_answers[] = {1, 2, 3}; //inizializza un array di 3 valori (possibili risposte alla domanda)

    //inizia il cilco while che andrà avavnti all'infinito fino all'inserimento di una risposta accettabile
    while(true) {
        printf("%s\nRisposta: ", d); //pone la domanda
        scanf("%d", &scelta); //prende la risposta inserita

        if(scelta == correct) { // confronta la risposta con la risposta corretta
            return 1; //se la risposta è la stessa, ritorna 1 a signicare che è corretta
        } else if(contains(possible_answers, scelta)) {//altrimenti controlla cosa c'è dentro "possible_answers" per verificare se "scelta" è una possibile risposta
                                                       //non sarà la risposta giusta altrimenti si sarebbe fermato allo step precedente 
            return 0;//se la risposta non è corretta e non è nemmeno tra le risposte valide
        } else {
            printf("Risposta non valida\n");//se si verifica return 0 non succede nulla, ricomincia il ciclo while e viene fatta di nuovo la domanda
        }
    }
}