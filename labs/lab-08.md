[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Feffie375.github.io%2FTPTE-AEGEAN&count_bg=%23E3802B&title_bg=%2307359E&icon=internetarchive.svg&icon_color=%23E7E7E7&title=%CE%A0%CF%81%CE%BF%CE%B2%CE%BF%CE%BB%CE%AD%CF%82&edge_flat=false)](https://hits.seeyoufarm.com)

# 8 Αναζήτηση - Ταξινόμηση σε Λίστα

---

## Περιεχόμενα

---

- 8.1 Αναζήτηση στοιχείων
- 8.2 Ταξινόμηση
- 8.3 Παράδειγμα ταξινόμησης
- 8.4 Ασκήσεις

## 8.1 Αναζήτηση στοιχείων

---

```python
# Δημιουργία λίστας
lista = [1, 6, 3, 5, 4, 6]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά στη λίστα και το μετατρεπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
done = True
thesi = 0

# Για κάθε στοιχείο της λίστας
for arithmos in lista:
  # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
  if arithmos == key:
    # Εκτύπωση της θέσης όπου βρίσκεται το key
    print("To %d βρίσκεται στην θέση %d της λίστας." % (key, thesi))
    # Το done γίνεται False
    done = False
  # Αυξάνουμε τη μεταβλητή thesi κατά 1
  thesi += 1

# Εάν το done παραμείνει True
if done == True:
  print("Το στοιχείο που αναζητάς δεν είναι στη λίστα.")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-08-example-01.py).

## 8.2 Ταξινόμηση

---

```python
# Δημιουργία λίστας
lista = [9, 3, 7, 5, 2]

# Εκτύπωση της μη ταξινομημένης λίστας
print("H μη ταξινομημένη λίστα είναι: %s" % lista)

for i in range(1, 5):
  for j in range(4, i - 1, -1):
    if lista[j - 1] > lista[j]:
      # Swap lista
      temp = lista[j - 1]
      lista[j - 1] = lista[j]
      lista[j] = temp

# Εκτύπωση της ταξινομημένης λίστας
print("H ταξινομημένη λίστα είναι: %s" % lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-08-example-02.py).

## 8.3 Παράδειγμα ταξινόμησης

---

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται πέντε αριθμούς, θα τους ταξινομεί σε αύξουσα σειρά και θα τους εμφανίζει.

```python
# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 5
lista = []

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
  # Ζητάμε από το χρήστη να δώσει ένα στοιχείο και το μετατρεπουμε σε ακέραιο
  num = int(input("Δώσε στοιχείο: "))
  # Αποθηκεύουμε το στοιχείο στη λίστα
  lista.append(num)

# Εκτύπωση της μη ταξινομημένης λίστας
print("H μη ταξινομημένη λίστα είναι: %s" % lista)

for i in range(1, 5):
  for j in range(4, i - 1, -1):
    if lista[j - 1] > lista[j]:
      # Swap lista
      temp = lista[j - 1]
      lista[j - 1] = lista[j]
      lista[j] = temp

# Εκτύπωση της ταξινομημένης λίστας
print("H ταξινομημένη λίστα είναι: %s" % lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-08-example-03.py).

## 8.4 Ασκήσεις

---

Συνιστάται να τρέξετε όλα τα προγράμματα των ασκήσεων. Όταν κάνετε επικόλληση σε κάποιον editor προσέξτε ότι συχνά τα προγράμματα από ορισμένα αρχεία δεν μεταφέρονται πάντα σωστά.

### Άσκηση 1

Να γραφεί πρόγραμμα το οποίο θα διαβάζει 10 ακεραίους αριθμούς και έπειτα θα ζητά έναν ακέραιο τον οποίο θα αναζητά και αν υπάρχει θα εμφανίζει τη θέση του αλλιώς θα εμφανίζει μήνυμα ότι δεν υπάρχει το στοιχείο στον πίνακα.

Οι αριθμοί είναι μοναδικοί στον πίνακα.

**1ος τρόπος με την εντολή for:**

```python
# Aρχικοποίηση μεταβλητών
MAX_ELEMENTS = 10
lista = []

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
  # Ζητάμε από το χρήστη να δώσει στοιχείο και τα μετατρεπουμε σε ακέραια
  num = int(input("Δώσε στοιχείο: "))
  # Αποθηκεύουμε το στοιχείο στη λίστα
  lista.append(num)

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά στη λίστα
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
done = True
thesi = 0

# Για κάθε στοιχείο της λίστας
for i in lista:
  # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
  if i == key:
    # Εκτύπωση της θέσης όπου βρίσκεται το key
    print("To %d βρίσκεται στην θέση %d της λίστας." % (key, thesi))
    # Το done γίνεται False
    done = False
  # Αυξάνουμε τη μεταβλητή thesi κατά 1
  thesi += 1

# Εάν το done παραμείνει True
if done == True:
  print("To στοιχείο που αναζητάς δεν είναι στη λίστα.")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-08-exercise-01a.py).

**2ος τρόπος με την εντολή while:**

```python
# Aρχικοποίηση μεταβλητών
MAX_ELEMENTS = 10
lista = []

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
  # Ζητάμε από το χρήστη να δώσει στοιχείο και τα μετατρεπουμε σε ακέραια
  num = int(input("Δώσε στοιχείο: "))
  # Αποθηκεύουμε το στοιχείο στη λίστα
  lista.append(num)

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά στη λίστα
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
done = True
thesi = 0

while(thesi < len(lista)) and done:
  if lista[thesi] == key:
    print("Το στοιχείο είναι στη θέση:", thesi)
    # Το done γίνεται False
    done = False
  # Αυξάνουμε τη μεταβλητή thesi κατά 1
  thesi += 1

# Εάν το done παραμείνει True
if done == True:
  print("To στοιχείο που αναζητάς δεν είναι στη λίστα.")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-08-exercise-01b.py).

### Άσκηση 2

Έστω ότι δημιουργείτε ένα πρόγραμμα το οποίο κρατά το όνομα επτά παικτών.

Να δημιουργηθεί πίνακας players στον οποίο θα αποθηκεύονται τα ονόματα των 7 παικτών. Θα ταξινομεί τα ονόματα σε φθίνουσα σειρά και θα εμφανίζει τα ονόματα των παικτών ταξινομημένα.

```python
# Αρχικοποίηση μεταβλητών
MAX_PLAYERS = 7
players = []

# Για MAX_PLAYERS
for i in range(MAX_PLAYERS):
  # Ζητάμε από το χρήστη να δώσει το όνομά του
  player = input("Δώσε όνομα παίκτη: ")
  # Αποθηκεύουμε το όνομα στη λίστα players
  players.append(player)

# Εκτύπωση της μη ταξινομημένης λίστας με τα ονόματα
print("Μη ταξινομημένοι παίκτες: %s" % players)

for i in range(1, MAX_PLAYERS):
  for j in range(MAX_PLAYERS - 1, i - 1, -1):
    if players[j - 1] < players[j]:
      # Swap players
      temp = players[j - 1]
      players[j - 1] = players[j]
      players[j] = temp

# Εκτύπωση της ταξινομημένης λίστας με τα ονόματα
print("Ταξινομημένοι παίκτες: %s" % players)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-08-exercise-02.py).

### Άσκηση 3

Έστω ότι δημιουργείτε ένα πρόγραμμα το οποίο κρατά το σκορ για κάποιο παιχνίδι. Στο παιχνίδι συμμετέχουν πέντε παίκτες. Να δημιουργηθεί πίνακας players στον οποίο θα αποθηκεύονται τα ονόματα των 5 παικτών. Επίσης να δημιουργηθεί πίνακας scores στον οποίο θα αποθηκεύονται τα σκορ των παικτών. Θα ταξινομεί τα σκορ σε αύξουσα σειρά και θα εμφανίζει τα ονόματα των παικτών με τα αντίστοιχα σκορ τους βάσει της ταξινόμησης. Βρείτε το μέσο όρο του πίνακα scores και υπολογίστε/εμφανίστε ποια είναι η διαφορά του σκορ του κάθε παίκτη από το μέσο όρο.

```python
players = []
scores = []

for i in range(5):
  name = input("Dose onoma paikti: ")
  players.append(name)

for i in range(5):
  name = int(input("Dose score paixnidiou: "))
  scores.append(name)

for i in range(1,5):
  for j in range(4, i-1, -1):
    if scores[j-1] > scores[j]:
      temp = scores[j-1]
      scores[j-1] = scores[j]
      scores[j] = temp
      temp2 = players[j-1]
      players[j-1] = players[j]
      players[j] = temp2

print(players)
print(scores)

sum = 0

for i in scores:
  sum = sum + i

mo = sum / 5

for i in range(5):
  print("H diafora tou score tou paikti ", players[i], " apo ton meso oro einai: ", mo - scores[i])
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-08-exercise-03.py).
