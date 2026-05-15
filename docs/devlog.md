# Devlog — Brain Shift

---

## Entry

### Settimana 1 (22-28 aprile 2026)

Abbiamo iniziato analizzando la struttura dei file che ci è stata fornita dal prof. All'inizio abbiamo dovuto studiare come far dialogare i vari moduli (come rules.py e generator.py) perché non eravamo abituati a lavorare con così tanti file separati. Abbiamo capito che questa organizzazione serve a rendere il codice testabile con pytest, quindi abbiamo iniziato a scrivere le prime funzioni seguendo  lo schema richiesto.

Cosa ci ha fatto perdere tempo: capire esattamente cosa dovesse andare in ogni modulo per non "sporcare" la struttura definita nella consegna. Alla fine abbiamo capito che tenere la logica separata dalla grafica in ui.py ci avrebbe aiutato a non fare confusione.

### Settimana 2 (29 aprile - 5 maggio 2026)

In questa fase abbiamo lavorato sull'integrazione tra la logica e la grafica. Abbiamo implementato il generatore di trial. Una scelta tecnica che abbiamo preso noi, all'interno della consegna, è stata l'uso del seed per rendere il gioco deterministico durante i test.

Cosa abbiamo imparato: l'importanza di seguire un'architettura predefinita. Anche se all'inizio ci sembrava rigida, ci ha aiutato a dividere il lavoro: uno si è occupato di riempire i "buchi" della logica e l'altro quelli della UI, senza sovrascriverci a vicenda.

### Settimana 3 (6-12 maggio 2026)

Questa settimana è stata dedicata alla macchina a stati e alla gestione del tempo, e abbiamo incontrato le prime vere difficoltà tecniche.

Il problema del Timer: Inizialmente il timer continuava a scorrere anche quando il gioco era in pausa o nello stato INTRO. Abbiamo perso un pomeriggio a capire che non potevamo usare un semplice countdown, ma dovevamo calcolare il "tempo di gioco effettivo" sottraendo i momenti di pausa dal tempo totale di Pygame.

Cosa abbiamo imparato: Abbiamo capito come gestire il delta-time e l'importanza di resettare i clock quando si cambia stato.

Fading delle istruzioni: Abbiamo deciso di implementare il fading non come un timer, ma come un controllo sulla variabile correct_answers. È stato interessante capire come mappare un numero intero (le risposte) su un valore di trasparenza Alpha per il testo.

Cosa pianifichiamo: Pulizia dei bug grafici e gestione della schermata finale.

### Settimana finale (13-17 maggio 2026)

L’ultima settimana è stata un caos. Siamo arrivati lunedì convinti di dover solo "abbellire" il gioco, invece ci siamo ritrovati a combattere con dei bug che non avevamo visto. Il problema più grosso è stato il conflitto tra gli stati: quando passavamo da PAUSED a PLAYING, il gioco a volte "mangiava" un input, facendo sbagliare la carta all'utente senza colpa. Abbiamo perso due giorni solo per capire che dovevamo resettare la coda degli eventi di Pygame ogni volta che si riprendeva la partita.

Il fallimento dell'audio: Qui abbiamo dovuto fare una scelta drastica. Avevamo implementato i suoni, ma crashavano a caso. Invece di passare le ultime notti a impazzire dietro alle librerie audio di Windows e Linux che non andavano d'accordo, ci siamo confrontati e abbiamo deciso di togliere tutto il modulo audio. È stato frustrante buttare quel codice, ma non volevamo consegnare un progetto che "forse crasha". Abbiamo convertito tutta la comunicazione all'utente in feedback visivo, cambiando i colori dei bordi delle carte.

Cosa abbiamo imparato: Che la semplicità vince sempre sulla complessità dell'ultimo minuto. Meglio una cosa che non c'è, piuttosto che una che funziona male.

---

## Bilancio finale

Arrivati alla fine, possiamo dire che il bilancio è positivo, ma molto più sudato del previsto. La cosa che ci dà più soddisfazione è la stabilità del gioco: dopo i crash della settimana finale, vedere che ora il programma regge anche sotto stress, gestendo correttamente il timer e i cambi di stato senza "impallarsi", ci fa capire che abbiamo lavorato bene sull'architettura. Abbiamo imparato a nostre spese che la programmazione  non è solo teoria: se non avessimo diviso la logica dalla UI come richiesto dal prof, il bug della gestione eventi dell'ultimo minuto ci avrebbe costretto a riscrivere tutto da capo, mentre così siamo riusciti a isolarlo e risolverlo nel main.

Lavorare con Pygame ci ha insegnato che la gestione del tempo è un incubo. Sottovalutavamo completamente quanto fosse difficile sincronizzare un timer con il refresh dello schermo e la latenza degli input. Abbiamo capito che Git è fondamentale per non sovrascrivere il lavoro dell'altro. All'inizio abbiamo sottovalutato enormemente la parte grafica: pensavamo che allineare quattro scritte e due rettangoli fosse banale, invece abbiamo perso intere serate a litigare con le coordinate pixel per pixel per colpa di una gestione poco furba delle costanti nel config.py.

Cosa rifaremmo diversamente? Sicuramente non perderemmo tempo con l'audio. Abbiamo sprecato ore preziose cercando di far funzionare il mixer di Pygame, che alla fine abbiamo dovuto togliere perché rendeva il progetto instabile su diversi PC. Se avessimo avuto un'altra settimana, avremmo usato quel tempo per curare meglio il feedback estetico (magari con delle transizioni fluide tra le carte) o per aggiungere una tabella dei record locali.

La divisione del lavoro è stata equa ma "turbolenta": uno di noi si è sporcato le mani con la logica dei trial e i test, l'altro con la macchina a stati e il rendering. Lavorare insieme ci ha insegnato che non basta che il proprio pezzo funzioni; se non capisci come l'altro ha strutturato la sua parte, il momento dell'unione dei moduli diventa un campo di battaglia.

Voto onesto: 27/30. Il progetto è tecnicamente fatto bene: la logica è separata, il codice è pulito e i test passano tutti. Ci togliamo qualche punto da soli perché la rinuncia all'audio ci brucia ancora e perché la grafica, pur essendo funzionale, è rimasta un po' troppo semplice rispetto all'idea iniziale. Però, considerando che il gioco non crasha mai e rispetta ogni riga della specifica, siamo molto orgogliosi del risultato.

---

