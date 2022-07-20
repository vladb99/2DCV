# Hough-Transformation
In dieser  Übung werden Sie die Hough-Transformation implementieren und damit die Parameterder dominierenden Geraden (Kanten) in einem Bild feststellen können.

1. Lesen Sie die Kapitel 7, 8 und 9 (Detektion einfacher Kurven) aus dem Buch ”Digitale Bildverarbeitung”.

2. Implementieren Sie die Hough-Transformation für Geraden. Verwenden Sie die Hesse’sche Normalform (HNF) und orientieren Sie sich bezüglich des Programmieransatzes an die Vorlesungsunterlagen (bzw. Buch Seite 162).
- Prototyp: houghArray = linearHT(im edge, angle steps, angle steps)
- houghArray: Ergebnisbild nach Hough-Transformation (int)
- im edge: Eingangsbild in Bin ̈arform (bool)
- angle steps: Filtermatrix (int)
- radius steps: Filtermatrix (int)
- Beispielaufruf: linearHT(image, 100, 100);

3. Erweitern Sie Ihre Funktion mit einer Schwelloperation (Threshold), um die Maximalwerte im HoughArray zu ermitteln. Welche Schwellwerte sind sinnvoll?
- Sinnvoll ist die 50% des Maximalwerts

4. Beantworten Sie folgende Fragen, indem Sie das Output Bildes nach der Schwelloperation interpretieren.
a) Wie können die Kanten im ursprünglichem Bild mit dieser Schwelloperation ermit-
telt werden?
- Die verbleibenden Regionen könnte man mit einer morphologischen Closing-Operation bereinigen.
- Danach können aus den Regionen die Schwerpunkte berechnet werden. Die Koordinaten der Schwerpunkten können als Parameter der gefunden Geraden genommen werden.

b) Welches sind die dominierendsten (längsten) Kanten?
- Das sind die Kanten, deren Akkumulator-Werte innerhalb einer Region sehr groß sind.

c) Anstelle der Schwelloperation könnte auch die Methode der Non-Maximum Suppression verwendet werden, um die Punkte im HoughArray detektieren zu können. Beschreiben Sie diese Methode kurz.
- Für jede Zelle im Akkumulator-Array wird überprüft ob ihr Wert höher ist als der der Nachbarzellen. Wenn höher dann kann man den Wert behalten, ansonsten wird er auf Null gesetzt. Die Koordinaten der verbleibenden Regionen sind potentielle Geradenparameter. Dabei kann eine zusätzlich eine Schwellenwertoperation durchgeführt werden, um die Kandidatenpunkte einzuschräcken.
