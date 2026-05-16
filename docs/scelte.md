# Scelte implementative

> Qui va la parte più **metacognitiva** del progetto: cosa avete scelto, perché, cosa avete scartato. Non può essere scritta dall'IA — è il ragionamento che mostra che avete capito quello che avete fatto.

## Scelte rilevanti

### Struttura e gestione dei dati dello Scoring

1. **Cosa**: Abbiamo scelto di gestire il punteggio e i contatori delle risposte (`correct_answers`, `wrong_answers`) direttamente come variabili nel loop principale del `main.py`, passandoli come parametri alle funzioni del modulo `ui.py` e aggiornando il punteggio tramite la funzione `apply_answer`.
2. **Perché**: Inizialmente avevamo ipotizzato strutture più complesse, ma l'architettura attuale ci permette di mantenere l'aggiornamento dei dati estremamente lineare e trasparente direttamente nel flusso degli eventi della tastiera.
3. **Alternative considerate**: L'uso di variabili globali (scartato subito per non sporcare il codice) o la creazione di una dataclass dedicata allo stato del punteggio. Abbiamo preferito la gestione diretta nel `main.py` perché l'interfaccia deve mostrare i contatori separati in tempo reale nei pulsanti inferiori, e passare variabili pulite rende il codice più leggibile.
4.**Conseguenze**: Il flusso dei dati è chiarissimo. Il `main.py` ha il pieno controllo dello stato del gioco; l'unico svantaggio è che il codice del ciclo principale deve gestire l'incremento dei singoli contatori all'evento della pressione dei tasti, ma il guadagno in termini di stabilità e facilità di lettura è buono.
---

### Gestione del tempo (Timer dei 60 secondi)

1. **Cosa**: Usiamo `pygame.time.get_ticks()` per calcolare il tempo rimasto con una sottrazione matematica rispetto all'inizio della partita.
2. **Perché**: Ci serviva precisione assoluta al millisecondo che fosse totalmente indipendente dagli FPS (il frame rate del gioco). Se avessimo contato semplicemente i frame dello schermo, su un computer più vecchio e lento la partita sarebbe durata più di 60 secondi reali, falsando il test,Inoltre, abbiamo scelto di visualizzare il timer in formato puramente testuale in alto a sinistra per non sovraccaricare graficamente l'HUD.
3. **Alternative considerate**: Creare una barra grafica temporale che si accorcia o utilizzare un timer integrato di Pygame (`pygame.USEREVENT`). La barra è stata scartata per mantenere l'interfaccia pulita, mentre l'evento andava troppo a scatti.
4. **Conseguenze**:Calcolare il tempo rimanente è immediato. L'unico svantaggio risiede nel fatto che, non essendoci una barra visiva , il giocatore deve lanciare un rapido sguardo all'angolo dello schermo per controllare i secondi residui.
---

### Fading delle istruzioni di aiuto

1. **Cosa**: Abbiamo scelto una soglia discreta netta (On/Off) basata sul contatore delle risposte corrette del giocatore.
2. **Perché**: All'inizio volevamo fare una sfumatura figa con un'interpolazione lineare (il testo che diventa sempre più trasparente a ogni risposta). Però ci siamo accorti che calcolare il valore Alpha del testo mentre il gioco andava veloce creava un effetto strano di sfarfallio che dava fastidio agli occhi e distorceva i font.
3. **Alternative considerate**: Far sparire le scritte di aiuto basandoci su un timer (ad esempio dopo i primi 10 secondi di gioco). Scartata perché se un giocatore all'inizio è lento o fa fatica, rischiava di trovarsi senza istruzioni prima ancora di aver capito bene il meccanismo dello switch.
4. **Conseguenze**: Il codice si è semplificato tantissimo, basta un banale controllo `if` dentro `ui.py`. Se il giocatore ha indovinato meno di 10 carte vede l'aiuto, dalla decima in poi il testo sparisce del tutto lasciando lo schermo pulito per concentrarsi. Lo svantaggio è che il distacco visivo è un po' brusco, ma provandolo ci siamo accorti che per il gameplay è molto più chiaro così.

---

### Posizionamento della carta  (Layout Grafico)
1. **Cosa**: Abbiamo posizionato la carta in modo **fisso al centro dello schermo**. La regola attiva (TOP o BOTTOM) viene comunicata al giocatore tramite un **cue visivo laterale**: un box di testo dinamico contenente la domanda associata, unito a una freccia (`←`).
2. **Perché**: Volevamo che l'interfaccia grafica rispecchiasse fedelmente i requisiti visivi . Questo layout mantiene l'attenzione visiva del giocatore fissa sul centro dello schermo, migliorando il task-switching.
3. **Alternative considerate**: Far saltare fisicamente la carta nella metà superiore dello schermo (per il compito sulle lettere) o inferiore (per i numeri). Abbiamo scartato questa opzione perché lo spostamento continuo dell'intero corpo della carta generava affaticamento visivo e non corrispondeva alla disposizione della consegna.
4. **Conseguenze**: Il posizionamento fisso rende il rendering in `ui.py` molto pulito. La logica di commutazione della regola rimane solida, poiché il `generator.py` assegna comunque la posizione logica (`TOP`/`BOTTOM`) al trial, determinando quale domanda e freccia mostrare a schermo.

---

## Cosa non siamo riusciti a fare e perché

* **Il sistema audio (Iniziato e poi abbandonato del tutto)** Questa è la nota più dolente del progetto. Avevamo scaricato i file `.wav` per gli effetti sonori e scritto il codice usando `pygame.mixer` per dare un feedback acustico alle risposte (il classico "bep" se corretto e "boop" se errato). Durante i test incrociati sui nostri PC ci siamo scontrati con la realtà: su Linux dava errori di segmentazione continui all'avvio del mixer, mentre su Windows causava un microscopico lag nel frame rate proprio nel millisecondo esatto in cui veniva generata la nuova carta. Visto che questo gioco è una corsa contro il tempo basata sui riflessi e sulla fluidità, abbiamo preferito **segare via completamente l'audio** piuttosto che consegnare al prof un progetto che rischiava di crashare o scattare durante la correzione. Abbiamo compensato potenziando il flash visivo sul bordo della carta.

* **La gestione dinamica delle costanti grafiche (Fatta male per mancanza di tempo)** Se si va a vedere dentro il modulo `ui.py`, ci sono diversi "numeri magici" scritti direttamente a mano nelle funzioni (come `x + 15` o `y + 45`) per centrare la lettera e il numero dentro il rettangolo della carta. Sappiamo che dal punto di vista della programmazione è fatto male: se provassimo a ridimensionare la finestra del gioco o a cambiare la risoluzione dello schermo nel `config.py`, le scritte rimarrebbero ferme lì e si spaccherebbe tutto il layout visivo. Non abbiamo avuto il tempo di scrivere una logica di posizionamento proporzionale o dinamica, quindi abbiamo lasciato le coordinate fisse accettando il vincolo della risoluzione standard richiesta nella consegna.
