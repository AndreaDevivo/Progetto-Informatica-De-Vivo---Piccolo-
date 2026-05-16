# Uso dell'IA nel progetto

> Questa pagina serve a dichiarare **in modo onesto e granulare** come avete usato assistenti IA (ChatGPT, Claude, Copilot, Gemini, ecc.) durante lo sviluppo. È obbligatoria. Va scritta **da voi**, non dall'IA.

---

## Politica del progetto

L'IA è consentita come assistente (spiegazioni, suggerimenti, debug, codice di dettaglio ben compreso) ma non come risolutore automatico (generazione e consegna di codice non compreso). Le parti di **documentazione e metacognizione** (questa pagina inclusa, `devlog.md`, `scelte.md`) vanno scritte senza IA.

---

## Strumenti usati

- [X] Gemini (modello: 3 Flash)
- [ ] ChatGPT (modello: …)
- [ ] Claude (modello: …)
- [ ] GitHub Copilot
- [ ] altro: …

---

## Uso granulare per modulo / parte

### Entry 1: Gestione del Timer in Pausa

**Dove**: `main.py`, nel loop principale durante la gestione dello stato `PAUSED_STATE`.

**Cosa abbiamo chiesto**: Come "congelare" il tempo di gioco in Pygame quando l'utente mette in pausa, visto che `pygame.time.get_ticks()` continua a scorrere in background.

**Cosa ci ha suggerito**: Ci ha spiegato l'idea di salvare il timestamp del momento in cui si preme pausa (`start_pause_time`) e calcolare la durata totale della pausa (`paused_duration`) da sottrarre poi al tempo di gioco effettivo.

**Cosa abbiamo fatto**:
- [ ] accettato integralmente
- [X] modificato adattandolo al nostro codice
- [ ] preso solo l'idea e riscritto
- [ ] rifiutato, perché…

**Perché**: Il suggerimento dell'IA usava variabili globali. Noi abbiamo preso la logica matematica della sottrazione dei millisecondi e l'abbiamo inserita all'interno della nostra macchina a stati nel `main.py`, usando i nostri contatori per evitare di sporcare il codice.

---

### Entry 2: Calcolo del Fading (Trasparenza Alpha)

**Dove**: `ui.py`, nella funzione che disegna i testi di aiuto a schermo.

**Cosa abbiamo chiesto**: Qual è il metodo corretto in Pygame per rendere un font o un testo trasparente usando i valori Alpha (0-255).

**Cosa ci ha suggerito**: Ci ha spiegato che gli oggetti `Font.render` non supportano l'alpha direttamente e che bisognava creare una `Surface` di supporto, renderizzarla con `.set_alpha()` e poi fare il `blit`.

**Cosa abbiamo fatto**:
- [ ] accettato integralmente
- [ ] modificato adattandolo al nostro codice
- [X] preso solo l'idea e riscritto
- [ ] rifiutato, perché…

**Perché**: Abbiamo preso solo un blocco di codice su come creare la Surface trasparente. La logica per decidere *quando* far sparire il testo (ovvero il controllo basato sulle 10 risposte corrette consecutive) l'abbiamo scritta interamente noi.

---

### Entry 3: Generazione dei diagrammi dell'architettura

**Dove**: File `README.md`,`architettura,md`.

**Cosa abbiamo chiesto**: Abbiamo descritto a parole come avevamo diviso i nostri moduli (`main`, `ui`, `scoring`, `rules`) e abbiamo chiesto all'IA di generarci il codice sorgente in formato **Mermaid** per creare il diagramma a blocchi delle relazioni.

**Cosa ci ha suggerito**: Ci ha restituito lo schema a nodi in codice Mermaid che mostrava visivamente il flusso dei dati e quali moduli importavano gli altri.

**Cosa abbiamo fatto**:
- [X] accettato integralmente
- [ ] modificato adattandolo al nostro codice
- [ ] preso solo l'idea e riscritto
- [ ] rifiutato, perché…

**Perché**: Lo schema rispecchiava esattamente la struttura del codice che avevamo scritto. Invece di perdere tempo a disegnare i blocchi a mano con programmi di grafica, abbiamo incollato il codice Mermaid per avere subito un grafico pulito da mostrare nella documentazione.

---

### Entry 4: Controllo degli input ripetuti (Debounce della tastiera)

**Dove**: `main.py`, dentro la lettura degli eventi della tastiera.

**Cosa abbiamo chiesto**: Come evitare che tenendo premuta la freccia direzionale il gioco continui a saltare le carte a raffica, registrando un sacco di risposte sbagliate al millisecondo.

**Cosa ci ha suggerito**: Ci ha spiegato la differenza tra `pygame.key.get_pressed()` (che controlla se il tasto è giù in quel frame) e l'evento `pygame.KEYDOWN` dentro la coda degli eventi (che scatta una volta sola per pressione).

**Cosa abbiamo fatto**:
- [X] accettato integralmente
- [ ] modificato adattandolo al nostro codice
- [ ] preso solo l'idea e riscritto
- [ ] rifiutato, perché…

**Perché**: Stavamo usando il metodo sbagliato nel loop principale. Abbiamo corretto la lettura degli input spostandola dentro il ciclo `for event in pygame.event.get():` seguendo il consiglio dell'IA e il problema delle risposte multiple è sparito subito.

---

### Entry 5: Debug Errore di Pytest

**Dove**: Cartella `tests/`, errore nel terminale durante il lancio di `pytest`.

**Cosa abbiamo chiesto**: Abbiamo incollato un errore del terminale che diceva che Pytest non trovava i moduli locali (errore di `ModuleNotFoundError` per `rules` o `scoring`).

**Cosa ci ha suggerito**: Ci ha spiegato come configurare il file `conftest.py` o come lanciare il comando usando `python -m pytest` per fare in modo che Python inserisse la cartella radice del progetto nel `sys.path`.

**Cosa abbiamo fatto**:
- [X] accettato integralmente
- [ ] modificato adattandolo al nostro codice
- [ ] preso solo l'idea e riscritto
- [ ] rifiutato, perché…

**Perché**: Era un problema di configurazione dell'ambiente di test e non di codice del gioco. Abbiamo usato il comando `python -m pytest` come suggerito e i test hanno iniziato a girare correttamente.

---

## Verifiche di comprensione

Dopo ogni uso dell'IA su parti di codice non banali, fatevi questa domanda: «Se il docente mi chiede di spiegare questa riga all'orale, so farlo?». Se la risposta è no, fermatevi e chiedete all'IA di *spiegare*, non di *scrivere*.

All'orale, ogni membro del gruppo deve saper spiegare ogni parte del codice. Se avete usato l'IA senza capire, all'orale si vede immediatamente.

---

## Cosa non abbiamo chiesto all'IA

* **Tutti i test strutturali con Pytest**: li abbiamo scritti a mano per verificare che la logica delle regole funzionasse secondo le specifiche del prof.
* **La macchina a stati**: la struttura degli stati (`PLAYING`, `PAUSED`, `INTRO`, `RESULTS`) e il passaggio da uno stato all'altro tramite gli eventi della tastiera è farina del nostro sacco.
* **La logica di `rules.py` e `generator.py`**: il controllo dei requisiti (vocale/consonante, pari/dispari) e il bilanciamento dei trial YES/NO basato sul seed.
* **I file di documentazione**: `docs/devlog.md` e `docs/scelte.md` (scritti interamente da noi analizzando il nostro lavoro).
