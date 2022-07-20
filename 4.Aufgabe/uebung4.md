# Kantendetektion

In dieser Übung wird der Sobel-Operator zur Kantendetektion implementiert.

**1. Lesen Sie das Kapitel 7 (Kanten und Konturen) aus dem Buch ”Digitale Bildverar- beitung”.**

**2. Beantworten Sie folgende Fragen:**

a) Was ist eine Kante und wie ist sie im Bild, in dessen Ableitung und dessen zweiten Ableitung erkennbar?
- Im Bild: Bereich wo sich die Intensität auf kleinem Raum stark ändert. Je stärker sich die Intensität ändert, umso stärker
ist auch der Hinweis auf eine Kante an dieser Stelle.
- In erste Ableitung: Eine Kante wird durch ein Maximum oder Minimum dargestellt (Stellt eine große Änderung da)
- In zweite Ableitung: Misst die lokale Krümmung. Idee ist, die Positionen der Nulldurchgänge der zweiten Ableitung als Kantenpositionen
zu verwenden.

b) Was sind die partiellen Ableitungen eines Bildes? Was sagen sie aus?
- Sie stellt die Ableitung entlang einer der Koordinatenrichtungen dar.

c) Was ist der Gradientenvektor (kurz: Gradient) eines Bildes? Was kann aus
diesem abgelesen werden?
- Vektor der partiellen Ableitungen.
- Wichtig für die richtungsunabhängige Lokalisierung von Kanten ist der Betrag des Gradienten wegen seiner invarianten Eigenschaft 
unter Bilddrehungen.

d) Wie kann die Kantenstärke berechnet werden?
- Als Betrag des Gradienten.

e) Wie kann die lokale Kantenrichtung berechnet werden?
- Durch den arctangens der Division, der beiden partiellen Ableitungen (y / x) 

**3. Implementieren Sie den Sobel-Operator.**

a) Verwenden Sie Filter in der separierten Form. Das Filterergebnis soll skaliert sein und wählen Sie eine geeignete Randbehandlung.

b) Schreiben Sie hierzu eine Funktion, die die erste Ableitung in horizontaler Richtung zurückgibt.

c) Und eine Funktion, die die erste Ableitung in vertikaler Richtung zurückgibt.

d) Zusätzlich soll eine Funktion implementiert werden, die die Kantenstärke durch den Betrag des Gradienten berechnet.

**4. Beantworten Sie folgende Fragen:**

a) Was sind die Nachteile des Sobel-Operators?
- Die Schätzung der Kantenrichtung ist allerdings mit dem PrewittOperator und auch mit dem ursprünglichen Sobel-Operator relativ ungenau.
- Winkelfehler ist groß.
- Kann ausschließlich auf Intensitätsunterschiede reagieren, die innerhalb seiner Filterregion stattfinden

b) Welche Alternativen gibt es zur Kantendetektion?
- Prewitt-/Robert-/Kompass Operatoren, Canny Filter 