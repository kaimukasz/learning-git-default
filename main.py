print("Hello World \n")
wieleWitaj = "witaj \n" * 10
print(wieleWitaj)

parzyste_dodatnie = [2, 4, 6, 8]
nieparzyste_dodatnie = [1, 3, 5, 7]
naturalne = parzyste_dodatnie + nieparzyste_dodatnie
print("Naturalne bez sortu ", naturalne)
naturalne.sort()
print("Naturalne posortowane ", naturalne)


# Wypełnij tablice x_tab i y_tab tak, aby zawierały odpowiednio 10 obiektów x i 10 y.
# Stwórz także tablicę o nazwie duza_tab, która będzie zawierała po 10 zmiennych x i y.
# Zrób to dodając do siebie wspomniane wyżej tablice.
#
# Dociekliwych informuję, że funkcja object powołuje do życia obiekt najbardziej podstawowego typu,
# jaki jest dostępny w pythonie. Natomiast metoda .count() zwraca liczbę elementów zapisanych w tablicy.

x_tab = []
x_tab.append(1)
x_tab.append(2)
x_tab.append(3)
x_tab.append(4)
x_tab.append(5)
x_tab.append(6)
x_tab.append(7)
x_tab.append(8)
x_tab.append(9)
x_tab.append(10)
for x in x_tab:
    print(x)


y_tab = []
y_tab.append(1)
y_tab.append(2)
y_tab.append(3)
y_tab.append(4)
y_tab.append(5)
y_tab.append(6)
y_tab.append(7)
y_tab.append(8)
y_tab.append(9)
y_tab.append(10)
for y in y_tab:
    print(y)

duza_tab = []
duza_tab = x + y
print("Wartości połączenia dwóch tablic ", duza_tab)