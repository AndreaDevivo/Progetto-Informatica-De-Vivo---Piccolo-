# Brain Shift — progetto di gruppo

## Chi siamo

- Simone Piccolo 1 — simone.piccolo@jcmaxwell.it /Simone-Piccolo
- Andrea De Vivo 2 — andrea.devivo@jcmaxwell.it / AndreaDevivo

Classe 4A Informatica — a.s. 2025-26.

## Cos'è Brain Shift
Brain Shift è un gioco di velocità che dura 60 secondi.
Il giocatore deve seguire una regola diversa in base a dove compare la carta sullo schermo:
- Se la carta è in **ALTO**: bisogna verificare se il numero visualizzato è **pari**.
- Se la carta è in **BASSO**: bisogna verificare se la lettera visualizzata è una **vocale**.
- Le risposte utilizzabili sono **SI** o **NO**
## Come giocare

Istruzioni minime ma complete per far partire il gioco da clone pulito:

```bash
git clone <https://github.com/AndreaDevivo/Progetto-Informatica-De-Vivo---Piccolo->
cd brain_shift 
pip install -r requirements.txt
python main.py
```

Specificate:

- versione Python richiesta: 3.10
- versione pygame richiesta: 2.0
- versione Pytest richiesta: 9.0.3

## Controlli

- ← freccia sinistra: per rispondere NO
- → freccia destra: per rispondere SI

## Screenshot
![FotoUI](docs/img/UI1.png)

![FotoUI](docs/img/UI2.png)
## Struttura del repository 

Breve spiegazione di dove sta cosa:

```
brain_shift/
├── main.py           ← entry point
├── ui.py             ← interfaccia grafica
├── rules.py          ← logica regole
├── scoring.py        ← sistema scoring
├── models.py         ← contenitore di classi
├── generator.py      ← generatore di oggetti
├── config.py         ← configurazione per interfaccia
├── docs/             ← documentazione
└── tests/            ← test pytest


```
### Come Lanciare i test
```bash
pytest tests/
---
```
