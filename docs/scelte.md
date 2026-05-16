# Scelte implementative

> Qui va la parte più **metacognitiva** del progetto: cosa avete scelto, perché, cosa avete scartato. Non può essere scritta dall'IA — è il ragionamento che mostra che avete capito quello che avete fatto.

## Scelte rilevanti

### Struttura e gestione dei dati dello Scoring

1. **Cosa**: Abbiamo usato una `dataclass` mutabile (`ScoringState`) passata come argomento alle funzioni che gestiscono il punteggio.
2. **Perché**: Volevamo evitare a tutti i costi l'uso delle variabili globali (come `global score`) dentro i moduli. 
3. **Alternative considerate**: Funzioni pure che prendono il vecchio punteggio e restituiscono un valore nuovo. L'abbiamo scartata perché oltre ai punti dovevamo aggiornare contemporaneamente i contatori delle risposte di fila, le combo e gli errori; restituire ogni volta tuple con tre o quattro numeri diversi stava diventando dificile da gestire.
4. **Conseguenze**: Adesso il `main.py` ha in mano l'oggetto del punteggio e lo passa a `scoring.py` che fa i calcoli e lo modifica direttamente. È diventato tutto molto comodo e pulito, l'unico svantaggio è che dobbiamo stare attenti a non resettare o sovrascrivere questa istanza per sbaglio quando cambiamo schermata nel gioco.

---

### Gestione del tempo (Timer dei 60 secondi)

1. **Cosa**: Usiamo `pygame.time.get_ticks()` per calcolare il tempo rimasto con una sottrazione matematica rispetto all'inizio della partita.
2. **Perché**: Ci serviva precisione assoluta al millisecondo che fosse totalmente indipendente dagli FPS (il frame rate del gioco). Se avessimo contato semplicemente i frame dello schermo, su un computer più vecchio e lento la partita sarebbe durata più di 60 secondi reali, falsando il test.
3. **Alternative considerate**: Creare un timer integrato di Pygame (`pygame.USEREVENT`) impostato per scattare da solo ogni secondo. Scartata perché volevamo far vedere i decimi di secondo che scorrono sul display in tempo reale, e l'evento che scatta una volta al secondo andava troppo a scatti ed era brutto da vedere.
4. **Conseguenze**: Mostrare il tempo rimasto è diventato una cavolata. Il problema grosso è nato però con la schermata di pausa: quando blocchi il gioco dobbiamo salvare i millisecondi esatti trascorsi fino a quel momento e "scalari" dal calcolo totale quando si riprende la partita, altrimenti il tempo continuava a scorrere anche a gioco fermo. Ci abbiamo perso un pomeriggio intero per far quadrare i conti.

---

### Fading delle istruzioni di aiuto

1. **Cosa**: Abbiamo scelto una soglia discreta netta (On/Off) basata sul contatore delle risposte corrette del giocatore.
2. **Perché**: All'inizio volevamo fare una sfumatura figa con un'interpolazione lineare (il testo che diventa sempre più trasparente a ogni risposta). Però ci siamo accorti che calcolare il valore Alpha del testo mentre il gioco andava veloce creava un effetto strano di sfarfallio che dava fastidio agli occhi e distorceva i font.
3. **Alternative considerate**: Far sparire le scritte di aiuto basandoci su un timer (ad esempio dopo i primi 10 secondi di gioco). Scartata perché se un giocatore all'inizio è lento o fa fatica, rischiava di trovarsi senza istruzioni prima ancora di aver capito bene il meccanismo dello switch.
4. **Conseguenze**: Il codice si è semplificato tantissimo, basta un banale controllo `if` dentro `ui.py`. Se il giocatore ha indovinato meno di 10 carte vede l'aiuto, dalla decima in poi il testo sparisce del tutto lasciando lo schermo pulito per concentrarsi. Lo svantaggio è che il distacco visivo è un po' brusco, ma provandolo ci siamo accorti che per il gameplay è molto più chiaro così.

---

### Feedback visivo dell'errore (Inter-trial interval)

1. **Cosa**: Gestiamo la durata del lampeggio colorato della carta usando una variabile di timestamp nel loop principale del `main.py`.
2. **Perché**: Quando l'utente preme un tasto, il bordo della carta deve colorarsi di verde o rosso per un istante (circa 100 millisecondi) prima di passare alla carta successiva. Non potevamo assolutamente usare un comando di blocco come `time.sleep(0.1)` perché avrebbe congelato lo schermo e la tastiera, impedendo al giocatore di continuare a premere a ritmo.
3. **Alternative considerate**: Gestire il tempo del colore usando i thread separati in background. Scartata subito perché Pygame non è thread-safe e rischiavamo di far crashare la grafica a caso durante la sovrapposizione delle immagini.
4. **Conseguenze**: Abbiamo dovuto aggiungere una variabile di stato nel `main` che salva il millisecondo esatto in cui l'utente risponde. Il loop continua a disegnare il bordo colorato finché il tempo corrente non supera quel timestamp di 100 millisecondi. Il codice del loop principale si è appesantito un po' ed è meno elegante, ma il gioco non si pianta mai.

---

## Cosa non siamo riusciti a fare e perché

* **Il sistema audio (Iniziato e poi abbandonato del tutto)** Questa è la nota più dolente del progetto. Avevamo scaricato i file `.wav` per gli effetti sonori e scritto il codice usando `pygame.mixer` per dare un feedback acustico alle risposte (il classico "bep" se corretto e "boop" se errato). Durante i test incrociati sui nostri PC ci siamo scontrati con la realtà: su Linux dava errori di segmentazione continui all'avvio del mixer, mentre su Windows causava un microscopico lag nel frame rate proprio nel millisecondo esatto in cui veniva generata la nuova carta. Visto che questo gioco è una corsa contro il tempo basata sui riflessi e sulla fluidità, abbiamo preferito **segare via completamente l'audio** piuttosto che consegnare al prof un progetto che rischiava di crashare o scattare durante la correzione. Abbiamo compensato potenziando il flash visivo sul bordo della carta.

* **La gestione dinamica delle costanti grafiche (Fatta male per mancanza di tempo)** Se si va a vedere dentro il modulo `ui.py`, ci sono diversi "numeri magici" scritti direttamente a mano nelle funzioni (come `x + 15` o `y + 45`) per centrare la lettera e il numero dentro il rettangolo della carta. Sappiamo che dal punto di vista della programmazione è fatto male: se provassimo a ridimensionare la finestra del gioco o a cambiare la risoluzione dello schermo nel `config.py`, le scritte rimarrebbero ferme lì e si spaccherebbe tutto il layout visivo. Non abbiamo avuto il tempo di scrivere una logica di posizionamento proporzionale o dinamica, quindi abbiamo lasciato le coordinate fisse accettando il vincolo della risoluzione standard richiesta nella consegna.
