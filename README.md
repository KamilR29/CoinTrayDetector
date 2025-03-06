# CoinTrayDetector

## Opis projektu
**CoinTrayDetector** to aplikacja służąca do analizy obrazu i automatycznego wykrywania oraz klasyfikacji monet na podstawie zdjęcia tacki. Program wykorzystuje techniki przetwarzania obrazu, takie jak wykrywanie krawędzi (Canny), konturów oraz transformację Hougha do detekcji okręgów. 

## Funkcjonalność
- Wczytanie obrazu tacki (`tray8.jpg`).
- Redukcja szumów za pomocą rozmycia medianowego.
- Wykrywanie konturu tacki.
- Detekcja monet przy użyciu transformacji Hougha.
- Klasyfikacja monet na:
  - Duże i małe.
  - Znajdujące się **wewnątrz** i **na zewnątrz** tacki.
- Wizualizacja wykrytych monet oraz wyświetlanie wyników.

## Wymagania
Aby uruchomić projekt, potrzebujesz:
- **Python 3.x**
- **OpenCV** (`cv2`)
- **NumPy**

Możesz zainstalować wymagane biblioteki za pomocą:
```sh
pip install opencv-python numpy
```

## Instalacja i uruchomienie
1. Sklonuj repozytorium:
   ```sh
   git clone https://github.com/KamilR29/CoinTrayDetector.git
   ```
2. Przejdź do katalogu projektu:
   ```sh
   cd CoinTrayDetector
   ```
3. Uruchom skrypt:
   ```sh
   python main.py
   ```
4. Po uruchomieniu zobaczysz wykryte monety na obrazie oraz podsumowanie w terminalu.

## Struktura projektu
```
CoinTrayDetector/
│-- main.py             # Główny skrypt analizy obrazu
│-- tray8.jpg          # Przykładowy obraz tacki z monetami
│-- README.md          # Dokumentacja projektu
```

## Jak działa kod?
1. **Wczytanie obrazu i redukcja szumów** – wczytujemy obraz w skali szarości i stosujemy filtr medianowy.
2. **Wykrywanie konturu tacki** – używamy wykrywania krawędzi Canny i konturów.
3. **Wykrywanie monet** – stosujemy transformację Hougha do znalezienia okręgów odpowiadających monetom.
4. **Klasyfikacja** – sprawdzamy, czy moneta jest w tacce i określamy jej rozmiar.
5. **Wizualizacja wyników** – rysujemy wykryte elementy na obrazie i wyświetlamy statystyki.

## Przykładowe wyniki
Po uruchomieniu programu w terminalu zobaczysz:
```
Big coins in tray: 2
Small coins in tray: 5
Big coins out of tray: 1
Small coins out of tray: 3
```
Oraz obraz z zaznaczonymi monetami i konturem tacki.

## Możliwe ulepszenia
- Udoskonalenie segmentacji konturu tacki.
- Zmiana parametrów transformacji Hougha dla lepszej detekcji monet.
- Dodanie interfejsu graficznego (GUI) do obsługi aplikacji.

## Autor
**KamilR29**

---
Projekt open-source – możesz dowolnie modyfikować i rozwijać!
