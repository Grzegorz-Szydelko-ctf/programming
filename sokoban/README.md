## Gra Sokoban-like (ASCII) w Pythonie 


Napisana przeze mnie prosta gra logiczna w terminalu w stylu klasycznego Sokobana. Gracz przesuwa skrzynie na wyznaczone miejsca, planując wcześniej swoje ruchy, aby się nie zablokować. 

Użyłem klasycznych symboli ASCII:
+ \# - ściana
+ . - cel
+ @ - gracz
+ \+ - gracz stojący na celu
+ $ - skrzynka
+ \* - skrzynka na celu

Sterowanie: W, S, A, D
   
Pozycja gracza i cele są odczytywane z pliku map.txt, zamiast być przypisane na sztywno w kodzie. Dzięki temu można tworzyć własne mapy i łatwo doawać nowe poziomy bez konieczności modyfikowania kodu gry. 

Nauczyłem się:
+ Przetwarzania danych z plików tekstowych w Pythonie.
+ Dynamicznego przypisywania pozycji obiektów w grze na podstawie wczytanych danych.
+ Logiki gier i zarzadzania stanem planszy.
+ Debugowania, testowania kodu.

