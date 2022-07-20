# Histogrammanpassung

In dieser Übung werden Sie das kumulative Histogramm eines Bildes berechnen.
Mithilfe dieses Histogramms werden Sie dann ein Bild an das kumulative Histogramm eines anderen Bildes anpassen.

1. Lesen Sie die Kapitel 5 (Punktoperationen - 5.2 Punktoperationen und Histogramme) und Kapitel 6 (Filter 6.1 - 6.3) aus dem Buch ”Digitale Bildverarbeitung”.

2. Implementieren Sie eine Funktion, die aus einem 8-Bit-Graustufenbild das zugehörige kumulative Histogramm berechnet.
• Prototyp: cumHisto = compute cumHisto(image, binSize)
• Das image ist ein 8-Bit-Grauwert Bild.

3. Beantworten Sie folgende Fragen:
a) Was ist eine homogene und was eine nicht-homogene Punktoperation?
• Eine homogene Punktoperation ist zum Beispiel: Änderung von Kontrast und Helligkeit, Invertieren von Bildern oder Gammakorrektur, etc... (Buch S. 55, PDF S. 70)
• Eine nicht-homogene Punktoperation berücksichtigt zusätzlich die Bildkoordinaten (u, v) (Buch S. 55, PDF S. 70)
b) Was ist der Unterschied zwischen Punktoperationen und Filteroperationen?
• Bei der Punktoperation wird nur ein Pixel verwendet
• Bei der Filteroperation wird das Ergebnis nicht aus einem einzelnen Pixel berechnet, sondern aus einer Menge von Pixeln
4. Implementieren Sie eine Funktion, die das Bild01 an das Bild02 mittels Histogrammanpassung angleicht.
Hierzu soll das kumulative Histogramm von Bild02 als Referenzverteilung dienen und das Bild01 so verändert werden, dass sein kumulatives Histogramm an die Referenzverteilung angeglichen wird.
Schließlich soll das Referenzbild (02) und das verarbeitete Bild (01) und deren kumulativen Histogramme angezeigt werden.
• Prototyp: LUT = match Histo(img histo, ref histo)
• img histo: Histogramm des anzupassenden Bildes.
• ref histo: Histogramm des Referenzbildes.
• LUT: Die Lookup Tabelle, welche auf das anzupassende Bild angewendet, die Histogrammanpassung durchführt.

Wieso müssen die beiden Histogramme des Referenz- und des Orginalbildes normiert sein? (Denken Sie an den Histogrammausgleich)

