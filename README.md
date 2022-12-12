# StockLight
This is my Stock Light Project
******************************
Einleitung
******************************
Das Programm erlaubt die Eingabe einer Aktien-Kennzeichnung und gibt auf Grundlage von 3 Kennzahlen eine Kaufentscheidung in Form einer Ampel aus.
Rot bedeutet, dass die Aktie nicht gekauft werden sollte bzw. verkauft werden sollte.
Grün bedeutet, dass die Aktie gekauft werden sollte.
Gelb bedeutet, dass die Kennzahlen kein eindeutiges Ergebnis liefern

*Warnung! Das Programm sollte nicht alleine herangezogen werden, um Handelsentschiedungen zu treffen. Das Programm ist sehr vereinfacht und nur auf 3 Kennzahlen begrenzt.


*******************************
Funktionsweise
*******************************
Zuerst wird die Eingabe einer Aktien-Kennzeichnung benötigt, wie z.B. "googl" für Google oder "dte.de" für die Telekom AG. Die Kennzeichnungen findet man über die Suche bei Yahoo Finance
Für die Berechnungen werden die Geschäftszahlen der letzten 3 Jahre herangezogen. Aus diesen wird ein Durchschnitt gebildet, indem die jeweiligen Zahlen der einzelnen Perioden addiert und mit 3 dividiert werden.
Anschließend werden durch festgelegte Bedingungen bestimmt, welche Farbe angezeigt werden soll.
  Rot: Return on Investment < 5% ; Eigenkapitalquote < 50% ; Liquidität 2. Grades < 80%
  Gelb: Return on Investment  5% <= X <= 7.5% ; Eigenkapitalquote  50% <= X <= 65% ; Liquidität 2. Grades  80% <= X <= 100%
  Grün: Return on Investment > 7.5% ; Eigenkapitalquote > 65% ; Liquidität 2. Grades > 100%
  
 Die Ampel zeigt rot, wenn 2 Kennzahlen rot und 1 Kennzahl gelb ist oder bei 3 roten kennzahlen.
 Die Ampel zeigt grün, wenn 2 Kennzahlen grün sind und 1 Kennzahl gelb ist oder bei 3 grünen Kennzahlen.
 Die Ampel zeigt gelb, wenn 2 oder 3 Kennzahlen gelb sind
 
 ********************************
 Allgemeine Informationen
 *********************************
 Das Programm wurde zu 100% mit Python programmiert.
 Für das GUI wurde Tkinter verwendet.
 Für die Abfrage der Daten wurde die Library yfinance verwendet, die die Daten von Yahoo Finance nutzbar machen soll.
 Das Programm dient für mich als erste Übung, um mit APIs zu arbeiten.
