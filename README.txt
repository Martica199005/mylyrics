Esercizio "Cattura la canzone"

Scrivere un programma che permetta di recuperare e successivamente mostrare il testo di una canzone attraverso l'utilizzo di un'applicazione a linea di comando (terminale). Il programma deve recuperare la canzone attraverso i siti (provider):
https://www.azlyrics.com/ oppure https://www.elyrics.net/ . Ad esempio per ottenere la canzone: "Can't Stop dei Red Hot Chili Peppers" da azlyrics l'utente scriverà da terminale:

python mylyrics.py -p azlyrics -a "red hot chili peppers" -l "can't stop"

viceversa con elyrics utilizzerà:

python mylyrics.py -p elyrics -a "red hot chili peppers" -l "can't stop"

in entrambi i casi il risultato sarà il testo della canzone seguito dalla dicitura, "Provided by: <nome del provider>"
 
Attraverso l'utilizzo del flag -s (opzionale) l'utente decide di salvare il testo della canzone in una cartella dedicata all'artista, successivi utilizzi dello script leggeranno il testo della canzone dal disco invece che recuperare dai provider se è stato salvato.

Lo script possiede i seguenti parametri e comportamenti:

-p --provider nome del provider

-a --artist nome dell'artista
-l --lyrics nome della canzone
-s --save salva il testo della canzone in formato txt

