#include <stdio.h> // Contiene le dichiarazioni di funzioni per inut e output
#include <math.h> // Libreria necessaria per calcolare la radice quadrata di un numero


int main()
{
    float D; // Dichiarazione della variabile

    //ESERCIZIO FACOLTATIVO
    float D1, D2, D3; // Definiamo 3 variabili per calcolarne la media aritmetica

    printf("Inserisci un numero: "); //il comando printf serve a stampare la richiesta di inserire un numero
    scanf("%f %f %f", &D1, &D2, &D3); 
    /* scanf legge l'input immesso da tastiera, "%" indica il tipo di argomento, "&"" assegna alla variabile "D" l'argomento inserito. 
    In questo caso sono 3 perché l'esercizio facoltativo richiede di inserire 3 valori per il calcolo della media aritmetica */
    D = (D1+D2+D3)/3; // formula per calcolare la media aritmetica dei tre valori inseirti

    printf("Questa è l'area del quadrato %.0f %.2f\n", D*D, D*D);
        /*
        %f indica dove andrà inserita la stringa nel testo stampato 
        ho inserito prima %.0f per restituire prima il valore senza decimali e poi %.2f per restituire subito lo stesso valore ma con due cifre decimali
        \n (new line) serve per andare a capo
        */
    printf("Questa è l'area del triangolo %.0f %.2f\n",sqrt(3)/4 * D * D, sqrt(3)/4 * D * D); 
        /*
        sqrt è la funzione per calcolare la radice quadrata
        */
    printf("Questa è l'area del cerchio %.0f %.2f\n", D * D/4 * M_PI, D * D/4 * M_PI);
        /*
        M_PI è la costante che rappresenta pi greco (3.14)
        */

}
