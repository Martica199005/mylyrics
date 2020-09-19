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

Se il nome del provider non è specificato mylyrics effettua la ricerca prima con un provider e successivamente con un altro. La ricerca può terminare immediatamente se si ottiene il risultato da un provider. Nel caso in cui il parametro è specificato il programma cerca solo con il provider specificato.

-a --artist nome dell'artista
-l --lyrics nome della canzone
-s --save salva il testo della canzone in formato txt


Linea guida sull'esercizio:

0) Nell'esercizio verranno valutati oltre che il corretto funzionamento, aspetti come: struttura del codice, ed altri aspetti inerenti alla qualità, gestione degli errori, corretto uso di OOP.

1) Non delegare la risoluzione del task ad una libreria che implementa parte dell'esercizio nel concreto va bene utilizzare librerie come requests, beautifulsoup ecc. ma non va bene utilizzare librerie che lavorano da wrapper completi su questi provider (azlyrics, elyrics).

2) Essendo l'esercizio semplice, puoi dare il tuo meglio nel curare aspetti che sono spesso trascurati come ad esempio struttura del progetto, README, organizzazione in moduli, test di unità, documentazione ecc.

3) La consegna dell'esercizio può avvenire via email (con file zip) oppure attraverso link a progetto github.