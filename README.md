# mastermind_python
Opis zadania:

o	Okno z polem tekstowym na 4 cyfry, listą odpowiedzi, przyciskiem
"Sprawdź", przyciskiem "Oszust!" oraz przyciskiem "Reset".

o	Po rozpoczęciu gry generowana jest losowa liczba (kod) złożona z czterech cyfr od 1 do 6 włącznie ( 1111, 1112, 1113, ... , 3455, 3456, 3461, 3462, ... , 6665, 6666).

o	Gracz wpisuje cztery cyfry od 1 do 6 do pola tekstowego i naciska
przycisk "Sprawdź".

o	Do pola odpowiedzi dopisywana jest odpowiedź zawierająca: liczbę wpisaną przez gracza, liczbę cyfr na poprawnych pozycjach oraz liczbę cyfr występujących w kodzie, ale na złych pozycjach.

o	Jeśli gracz wpisał liczbę będącą kodem, wyświetlane jest okno z
napisem 'Wygrana".

o	Jeśli gracz po 12 próbach nie odgadł kodu, wyświetlane jest okno z
napisem "Przegrana".

o	Logika gry powinna być realizowana przez osobną klasę, dziedziczącą po klasie RegulyGry. Z klasy RegulyGry powinna być również wydziedziczona druga klasa, generująca niepoprawne odpowiedzi. Wybór zestawu reguł powinien być dokonywany losowo przed każdą grą.

o	Jeśli gracz nacisnął przycisk "Oszust!" przy poprawnych regułach gry, program powinien wyświetlić okno z napisem "Tere fere." oraz wylosowanym kodem.

o	Jeśli gracz nacisnął przycisk "Oszust!" przy niepoprawnych regułach gry, program powinien wyświetlić okno z napisem "Złapałeś/łaś mnie!"

Testy:

1.	Wyświetlenie (wypisanie w konsoli) wylosowanego kodu, wpisanie odpowiedzi z błędnymi cyframi - oczekiwana informacja o braku poprawnych trafień.

2.	Wyświetlenie wylosowanego kodu, wpisanie odpowiedzi z poprawnymi cyframi w złych miejscach - oczekiwana informacja o niepoprawnym położeniu.

3.	Wyświetlenie wylosowanego kodu, wpisanie odpowiedzi z dwoma poprawnymi cyframi w dobrych miejscach i dwoma poprawnymi w złych miejscach -oczekiwana informacja o dwóch trafieniach i dwóch złych pozycjach.

4.	Wyświetlenie wylosowanego kodu, wpisanie poprawnej odpowiedzi -oczekiwana informacja o wygranej.
	
5.	Wpisanie 12 razy niepoprawnego kodu - oczekiwana informacja o przegranej

6.	Próba wpisania niepoprawnego kodu do pola odpowiedzi (mniej lub więcej niż 4 znaki, znaki nie będące cyframi od 1 do 6) - oczekiwane nieuznanie kodu (gracz nie traci tury).

7.	Wciśnięcie przycisku "Oszust" przy poprawnych zasadach gry -
oczekiwana informacja "tere fere".

8.	Wciśnięcie przycisku "Oszust" przy niepoprawnych zasadach gry -
oczekiwana informacja o oszukiwaniu przez komputer.

9. Wpisanie 10 kodów, resetowanie gry, wpisanie 5 kodów - oczekiwane normalne działanie gry (czy licznik tur resetuje się po wciśnięciu "Reset").

https://github.com/mekikula/mastermind_python
