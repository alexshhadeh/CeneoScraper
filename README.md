# CeneoScraper
## Etap 1 - Ekstrakcja pojedynczej opinii o produkcie, którego kod będzie wpisany w kodzie programu
- pobranie kodu pojedynczej strony z opiniami o produkcie
- wydobycie z kodu strony fragmentu odpowiadającego pojedynczej opinii
- zapisanie do pojedynczych zmiennych wartości składowych opinii
- obsługa błędów
- transformacja danych do docelowych typów

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|------------|--------------|----------|
|Opinia|div.js_product-review|opinion|bs4.element.Tag|
|Identyfikator opinii|["data-entry-id"]|opinionId|str|
|Autor|span.span.user-post__author-name|author|str|
|Rekomendacja|span.user-post__author-recomendation > em|rcmd|bool|
|Liczba gwiazdek|span.user-post__score-count|stars|float|
|Treść opinii|div.user-post__text|content|str|
|Lista zalet|div[class*="positives"] ~ div.review-feature__item|pros|list|
|Lista wad|div[class*="negatives"] ~ div.review-feature__item|cons|list|
|Czy potwierdzona zakupem|div.review-pz|purchased|bool|
|Data wystawienia|span.user-post__published > time:nth-child(1)["datetime"]|publishDate|str|
|Data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchaseDate|str|
|Dla ilu osób przydatna|span[id^="votes-yes"]|useful|int|
|Dla ilu osób nieprzydatna|span[id^="votes-no"]|useless|int|

## Etap 2 - Ekstrakcja wszystkich opinii o produkcie z pojedynczej strony
- utworzenie słownika do przechowywania wszystkich składowych pojedynczej opinii
- utworzenie listy, do której będą dodawane słowniki reprezentujące pojedyncze opinie
- dodanie pętli, w której pobierane były składowe kolejnych opinii z pojedynczej strony

## Etap 3 - Ekstrakcja wszystkich opinii o produkcie ze wszystkich stron
- dodanie pętli, w której:
    * pobierana jest strona z opiniami
    * dla każdej opinii na stronie pobierane są jej składowe
    * sprawdzane jest, czy istnieje kolejna strona z opiniami, które powinny zostać pobrane
- zapisanie wszystkich opinii o produkcie do pliku .json

## Etap 4 - Refaktoryzacja kodu
- parametryzacja identyfikatora opinii
- zdefiniowanie funkcji do ekstrakcji pojedynczych składowych opinii
- dodanie słownika opisującego strukturę opinii wraz z selektorami potrzebnymi do ekstrakcji pojedynczych składowych
- użycie wyrażenia słownikowego (dictionary commprehension) do pobrania (i zapisania) składowych pojedynczej opinii
- rezygnacja z transformacji składowych opinii (przeniesienie tego procesu do analizy opinii)

## Etap 5 - Analiza statystyczna zbioru opinii o produkcie
- wyświetlenie listy kodów produtów, dla których zostały pobrane opinie
- wczytanie opinii o wskazanym produkcie do obiektu DataFrame
- obliczenie podstawowych statystyk
    * liczba opinii o produkcie
    * liczba opinii w których podana została lista zalet
    * liczba opinii w których podana została lista wad
    * średnia ocena produktu wyznaczona na podstawie liczby gwiazdek

## Etap 6 - Narysowanie wykresów opartych o dane ze zbioru opinii o produkcie
- wykres kołowy obrazujący udział poszczególnych wartości rekomendacji w ogólnej liczbie opinii
- wykres kolumnowy/słupkowy obrazujący czestość występowania opinii z poszczególnymi ocenami wyrażonymi liczbą gwiazdek