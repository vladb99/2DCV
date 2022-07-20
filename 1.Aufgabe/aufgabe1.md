# Farbbilder und Spiegelung:
1. Starten Sie die IDE und legen Sie ein neues Projekt auf dem Z-Laufwerk an.

2. Lesen Sie ein Bild mit Hilfe von scikit-image ein und lassen Sie sich das Bild anzeigen.
3. Untersuchen Sie den Datentyp des eingelesenen Bildes. Wie ist ein Numpy Array aufgebaut?
- <class 'numpy.ndarray'>
- (333, 500, 3)
- Drei dimensionales Array (3 Farbkanälen) mit Breite von 500 Pixel und Höhe von 333 Pixel. 

4. Lassen Sie sich die drei Farbkanäale eines Bildes getrennt anzeigen.

5. Implementieren Sie eine Funktion, die ein eingelesenes Bild wahlweise horizontal oder vertikal spiegelt. (Verwenden Sie hierfür keine Numpy Funktionen.)

# Histogramme, Binning und Lookup-Tabellen

4. Berechnen Sie das Histogramm von den Bildern 01 bis 05. Sie werden zum einen Auf- nahmefehler (Belichtungsfehler) in deren Histogrammen erkennen k ̈onnen. Zum anderen werden Sie die Bearbeitungsschritte in zwei bearbeiteten Bild anhand des Histogramms erkennen k ̈onnen.
a) Welche Aufnahmefehler sind in 01 und 03 zu erkennen? Woran ist dies im Histogramm erkennbar?
Bild 1:
- Unterbelichet. Das sieht man im Histogramm wo ganz links eine Häufung von Pixel ist, während die Intensitätsbereiche ganz rechts ungenutzt ist.
- Hoher Kontrast. Im Histogramm großer Abstand zwischen maximal und minimal Wert.

Bild 3:
- überbelichtet, weil die Pixels rechts gehäuft sind und die Intensitätsbereiche ganz links ungenutzt sind.

b) Bild01 ist das aufgenommene Bild. Bild02 wurde nachbearbeitet. Die Helligkeit wurde erh ̈oht. Woran ist dies im Histogramm erkennbar? Welche Daten gehen dabei verloren?
- Das sieht man anhand der Verschiebung der meisten Pixel von links nach rechts im Histogramm.
- Manche Grauwerte werden so stark belichtet, dass sie verschwinden. Zum Beispiel die Wolken.

c) Bild04 ist das aufgenommene Bild. Bild05 wurde einem Bearbeitungsschritt un- terzogen. Was wurde in Bild05 ver ̈andert? Woran kann man dies in seinem His- togramm erkennen?
- Kontrast
- Ausdehnung des Histogramms. Dunkle Stellen werden dunkler und helle Stellen heller.

5. Implementieren Sie eine Funktion, die eine Punktoperation mithilfe einer Lookup-Tabelle zum Aufhellen eines Bildes durchfu ̈hrt.
a) In Aufgabe (4b) gingen Daten beim Aufhellen eines Bildes verloren. Wie könnte dies vermieden werden?
- Indem man ab einem bestimmten Schwellenwert aufhört die Intensität zu erhöhen. Dies kann durch die Anwendung der Gammafunktion erreicht werden.

b) Damit beim Aufhellen von Bild01 keine Daten verloren gehen, soll eine Lookup- Tabelle verwendet werden. Versuchen Sie mit der Lookup-Tabelle die dunklen Bildbereiche des Bildes aufzuhellen ohne die hellen Bereiche zu stark zu verändern.
