# Lineare Nachbarschaftsfilter

In dieser Übung werden Sie einen linearen Nachbarschaftsfilter auf einem Bild anwenden und die Rahmenbedingungen eines Filters kennenlernen. Wenden Sie die linearen Filter auf das Bild Lena.jpg an.

1. Lesen Sie das Kapitel 6 (Filter) aus dem Buch ”Digitale Bildverarbeitung”.

2. Implementieren Sie eine Funktion, die es erlaubt ein Bild (im sinnvollen Rahmen) mit
frei wählbaren Filtermasken zu falten.

- Prototyp: [ out image ] = filter(in image, filter, off)
- out image: Ergebnisbild (int) nach Faltung von in image mit filter
- filter: Filtermatrix (float)
- off: Offset (int)
- 8-Bit Graustufenbilder als Eingangs- und Ausgangsdaten.
- Filtermatrix der Gr ̈oße (NxN) mit N = (2K + 1), K = 1, 2, ... – Beispielaufruf: filter(image, [1 1 1; 1 3 1; 1 1 1]./11)

3. Erweitern Sie die Funktion filter() aus Aufgabe 2 um folgende Rahmenbedingungen:
- min: Setzt Bildpunkte auf den minimalen Wert (0)
- max: Setzt Bildpunkte auf den maximalen Wert (255)
- continue: Setzt das Bild außerhalb mit dem gleichen Pixelwert, wie das entsprechende am n ̈achsten liegende Randpixel, fort.
- UntersuchenSiedieRandbehandlungenaufihrVerhaltenbeiBenutzungverschiedener Filter.
- Prototyp: [ out image ] = filter(in image, filter, off, edge);
- edge: Parameter zur Auswahl der Randbehandlung (’min’) - String

4. Beantworten Sie folgende Fragen:
a) Nennen Sie die Arten und Eigenschaften von linearen Filtern.
- Glättungsfilter (positive Koeffizienten), Differenzfilter (mit negativen Koeffizienten)
- Kommutativität (kein Unterschied ob man Bild mit Filterkern faltet oder umgekehrt)
- Linearität (Beim Multiplizieren mit einer Konstante oder Falterung der Addition von zwei Bilder)
- Assoziativität (Beliebige Reihenfolge bei mehrere nacheinander Filteroperationen)

b) Was ist der Unterschied zwischen linearen und nichtlinearen Filtern?
- Bei linearen Filtern wird der Wert des Zielpixels wird als gewichtete (lineare) Summe der Quellpixel berechnet. Dafür wird eine Filtermaske verwendet.
- Bei nichtlinearen Filtern wird der Wert des Zielpixels durch den Sortierungsmechanismus gesetzt.

# Nichtlineare Nachbarschaftsfilter
In dieser Übung werden Sie die Auswirkung nichtlinearer Filter auf ein mit Salt and Pepper verrauschtes Bild untersuchen.

1. Lesen Sie die Kapitel 6.4 (Nichtlineare Filter) und Kapitel 7 (Kanten und Konturen) aus dem Buch ”Digitale Bildverarbeitung”.

2. Implementieren Sie den Medianfilter.
- Prototyp: out image = medianFilter(in image, filter, offset)
out image: Ergebnisbild nach Faltung von in image mit filter
in image: Eingangbild (int); 8-Bit Graustufenbilder
filter: Filtermatrix (float); Größe (NxN) mit N = (2K + 1), K = 1, 2, ... offset Offset (int)
Beispielaufruf: medianFilter(image, np.array([[1,1,1], [1,3,1], [1,1,1]])/11, 0) Benutzung Sie für die Sortierung wenn möglich Heap Sort.

3. Beantworten Sie folgende Fragen:
a) Vergleichen Sie die Ergebnisse der verschiedenen Filter miteinander und begründen Sie diese.

b) Warum ist es beim Medianfilter sinnvoll für die Sortierung Heap Sort zu verwenden?
- Wegen memory usage und laufzeit immer O(nlogn)
- Sortierung ist schneller bei gleichen Werten?

c) Untersuchen Sie, welche Effekte bei mehrmaligem Anwenden eines Filters auf das jeweilige Ergebnisbild auftreten.
- Das Bild wird unschärfer

d) Welche Effekte treten bei großen und bei kleinen Filtermasken auf?
- Kleine Filtermasken glätten nicht richtig. Große Filtermasken machen das Bild unschärfer (Weil der Median von mehr Pixelwerten genommen wird und dieser dadurch mehr schwanken kann). 
- Bei großen Filtermasken verschwindet auch der Kontrast, sodass man die Tiefe der Objekte im Bild nicht mehr erkennen kann.
