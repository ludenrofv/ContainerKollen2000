# ContainerKollen2000

ContainerKollen2000 är ett enkelt webbprojekt för att söka efter containrar via container-ID och visa information om respektive containertyp.

## Funktioner

* Sök container med ID.
* Visar containertyp, bild och mått.
* Visar eventuell notering.
* Sida med alla containertyper.
* Filtrering på:

  * Alla
  * Lift
  * LVX
  * Kombi
* All information om containertyper lagras i en separat JSON-fil.

---

## Projektstruktur

```text
ContainerKollen2000/
│
├── index.html
├── containertyper.html
├── container.json
├── containertyper.json
├── resize.py
├── README.md
└── images/
    ├── Lift öppen 10m3.png
    ├── LVX Täckt 25m3.png
    └── ...
```

---

## JSON-filer

### container.json

Innehåller alla containrar.

Exempel:

```json
{
  "id": "10033",
  "typ": "Lift öppen 10m3",
  "note": "Kort"
}
```

---

### containertyper.json

Innehåller information om varje containertyp.

Exempel:

```json
{
  "typ": "Lift öppen 10m3",
  "bild": "images/Lift öppen 10m3.png",
  "langd": "3,6",
  "bredd": "1,8",
  "hojd": "1,6"
}
```

---

## Starta projektet

Eftersom webbläsaren av säkerhetsskäl inte tillåter att JSON-filer läses direkt från filsystemet behöver projektet köras via en lokal webbserver.

Exempel med Python:

```bash
python3 -m http.server 8000
```

Öppna sedan:

```
http://localhost:8000
```

---

## Förminska bilder

Projektet innehåller ett Python-skript (`resize.py`) som kan förminska alla bilder i mappen `images`.

### Installera Pillow

```bash
python3 -m pip install Pillow
```

### Kör skriptet

Stå i projektets rotmapp och kör:

```bash
python3 resize.py
```

Skriptet:

* läser alla PNG-, JPG-, JPEG- och WEBP-bilder i `images`
* skalar ned dem
* optimerar filstorleken
* skriver över originalbilderna

---

## Git

Visa status:

```bash
git status
```

Lägg till ändringar:

```bash
git add .
```

Skapa en commit:

```bash
git commit -m "Beskrivning av ändring"
```

Pusha till GitHub:

```bash
git push
```

Hämta senaste ändringar:

```bash
git pull origin main
```

---

## Framtida förbättringar

* Fler mått och egenskaper för containertyper.
* Vikt och volym.
* Fler bilder per containertyp.
* Sökning på containertyp.
* Favoriter.
* Mörkt tema.

---

## Licens

Projektet är avsett för internt bruk och utvecklas för ContainerKollen2000.
