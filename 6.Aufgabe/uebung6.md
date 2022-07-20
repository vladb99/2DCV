# Morphologische Filter

In dieser Übung werden Sie die morphologischen Operationen Erode und Dilate implementieren.

1. Lesen Sie die Kapitel 10 (Morphologische Filter) aus dem Buch ”Digitale Bildverar- beitung”.

2. Implementieren Sie Funktionen, die es erlauben ein Bild mit den morphologischen Opera- tionen Erode und Dilate mit frei wählbaren Filtergrößen zu behandeln. Bemerkung: Die Grauwert-Dilation wird definiert als Maximum der addierten Werte des Filters und der entsprechenden Bildregion. Umgekehrt entspricht die Grauwert-Erosion dem Minimum der Differenzen.
- Prototyp: out image = erode(in image, filter, iter num);
- Prototyp: out image = dilate(in image, filter, iter num); out image: Ergebnisbild nach der Operation.
- in image: Eingangsbild
- filter: Filtermatrix
- iter num: Anzahl Iterationen

3. Experimentieren und modifizieren Sie mit den Strukturelementen. Welche Effekte treten auf? (Siehe Buch Seite 187 - 189).
