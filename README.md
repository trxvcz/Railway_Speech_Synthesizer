# 🚂 Syntezator Mowy - Zapowiedzi Kolejowe (Warszawa Centralna)

**Projekt dydaktyczny:** Ćwiczenie z syntezy mowy  
**Prowadzący:** dr inż. Piotr Wrzeciono

---

## 📖 Opis Projektu
Projekt realizuje zadanie budowy prostego **korpuskularnego syntezatora mowy**. System generuje komunikaty głosowe metodą **syntezy konkatenacyjnej**, która polega na łączeniu wcześniej nagranych fragmentów audio (.wav) w jedną, płynną całość.

Głównym celem programu jest automatyczne generowanie zapowiedzi dla pociągów przyjeżdżających i odjeżdżających ze stacji **Warszawa Centralna**.

### Założenia zadania:
1.  **Korpus nagrań:** Program korzysta z bazy plików audio podzielonej na kategorie: `stacje`, `perony_i_tory` oraz `do_z_stacji`.
2.  **Specyfika stacji:** System uwzględnia specyficzną numerację torów i peronów na Warszawie Centralnej (np. peron 1 = tory 7 i 5, peron 2 = tory 3 i 1 itd.).
3.  **Algorytm dopasowania:** Skrypt analizuje tekst i szuka najdłuższych pasujących fraz (metoda 3, 2 lub 1 słowo), co pozwala na zachowanie naturalnej intonacji nagranych wyrażeń.
4.  **Normalizacja tekstu:** Automatyczne usuwanie polskich znaków diakrytycznych w celu dopasowania tekstu do nazw plików.

---

## 🛠️ Wymagania Techniczne

* **Język:** Python 3.12+
* **Biblioteki:** `pygame` (wykorzystywana do stabilnego odtwarzania audio)

---

## ⚙️ Instrukcja Instalacji i Uruchomienia

### 1. Instalacja bibliotek
Do poprawnego działania wymagana jest biblioteka `pygame`. Zainstaluj ją komendą:
```bash
pip install -r requirements.txt
```

### 2. Struktura katalogów
Program oczekuje, że nagrania znajdują się w folderze `audio` w katalogu głównym projektu:
```text
.
├── main.py                 # Kod źródłowy
├── README.md               # Dokumentacja
├── requirements.txt        # Plik z listą bibliotek
└── audio/                  # Korpus nagrań
    ├── do_z_stacji/        # np. pociag_ze_stacji.wav
    ├── perony_i_tory/      # np. przy_peronie_trzecim.wav
    └── stacje/             # np. warszawa_wschodnia.wav
```

### 3. Uruchomienie
Uruchom program i postępuj zgodnie z instrukcją w konsoli:
```bash
python main.py
```
Po wyświetleniu prośby, wpisz treść zapowiedzi, np.:
> *Pociąg do stacji Lublin Główny odjedzie z toru pierwszego przy peronie drugim.*

---

## 🔍 Logika działania

* **Obsługa znaków:** Funkcja `usun_polskie_znaki` mapuje litery (ą -> a, ę -> e itd.), co pozwala na bezbłędne odczytywanie plików z nazwami pozbawionymi polskich znaków.
* **Wyszukiwanie fraz:** Program stosuje algorytm "greedy matching" – najpierw próbuje połączyć 3 kolejne wyrazy w jedną nazwę pliku, jeśli nie znajdzie dopasowania, próbuje z 2 wyrazami, a na końcu z pojedynczym słowem.
* **Raportowanie braków:** Jeśli w korpusie brakuje danego nagrania, program wyświetla komunikat: `Brak nagrania dla fragmentu: [nazwa]`.
* **Odtwarzanie:** Zastosowanie `pygame.mixer` eliminuje błędy dostępu do pamięci (SIGSEGV), które mogą występować przy seryjnym odtwarzaniu plików o różnym próbkowaniu.

---

## 📝 Przykładowe komunikaty do testów
* "Pociąg ze stacji Warszawa Wschodnia do stacji Poznań Główny przez stacje Kutno Konin odjedzie z toru drugiego przy peronie trzecim."
* "Pociąg ze stacji Kraków Główny do stacji Warszawa Centralna odjedzie z toru ósmego przy peronie czwartym. Pociąg kończy bieg."