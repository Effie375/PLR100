# 5 Εισαγωγή στις Λίστες

---

## Περιεχόμενα

---

- 5.1 Μονοδιάστατη Λίστα
- 5.2 Αποθήκευση στοιχείων
- 5.3 Άθροισμα στοιχείων
- 5.4 Έυρεση MAX
- 5.5 Έυρεση MIN
- 5.6 Έυρεση MAX με θέση
- 5.7 Αναζήτηση στοιχείων I
- 5.8 Αναζήτηση στοιχείων II
- 5.9 Αναζήτηση αριθμού στοιχείων

## 5.1 Μονοδιάστατη Λίστα

---

- Δυναμική δομή δεδομένων για διατεταγμένη συλλογή στοιχείων.
- Όχι απαραίτητα του ίδιου τύπου.
- Τα στοιχεία μέσα σε [ ].
- Χρησιμοποιούμε λίστες στην python για την αναπαράσταση πινάκων.

**Χαρακτηριστικά:**

- Ένα Όνομα
- Πολλές Θέσεις
- Μια Δομή

```python
# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

# Στη θέση 2 της λίστας βάζουμε τον αριθμό 4
lista[2] = 4
# Ζητάμε από το χρήστη να δώσει τιμή και το βάζουμε στη θέση 0 της λίστας
lista[0] = input("Δώσε τιμή: ")
```

## 5.2 Αποθήκευση στοιχείων

---

```python
# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 5
lista = []
i = 0

# Για όσο το i είναι μικρότερο από το MAX_ELEMENTS
while i < MAX_ELEMENTS:
  # Ζητάμε από το χρήστη να δώσει στοιχείο και το μετατρέπουμε σε ακέραιο
  num = int(input("Δώσε στοιχείο για την θέση %d: " % i))
  # Προσθέτουμε το στοιχείο στη lista
  lista.append(num)
  # Αυξάνουμε το i κατά 1
  i += 1

# Εκτύπωση της λίστας
print("Η λίστα μας είναι: %s" % lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-05-example-01.py).

## 5.3 Άθροισμα στοιχείων

---

```python
# Αρχικοποίηση μεταβλητών
lista = [5, 7, 8, 9, 3]
athroisma = 0
i = 0

# Για όσο το i είναι μικρότερο από το μήκος της λίστας
while i < len(lista):
  # Αυξάνουμε το άθροισμα κατά το στιγμιαίο στοιχείο της λίστας
  athroisma += lista[i]
  # Αυξάνουμε το i κατά 1
  i += 1

# Εκτύπωση αθροίσματος
print("Άθροισμα: %d" % athroisma)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-05-example-02.py).

## 5.4 Έυρεση MAX

---

```python
# Αρχικοποίηση μεταβλητών
lista = [5, 7, 8, 9, 3]
elaxisto = lista[0]
megisto = lista[0]
i = 0

# Για όσο το i είναι μικρότερο από το μήκος της λίστας
while i < len(lista):
  # Για όσο το στιγμιαίο στοιχείο της λίστας είναι μεγαλύτερο από το megisto που ορίσαμε
  if lista[i] > megisto:
    # Εκχωρούμε στο megisto το στιγμιαίο στοιχείο της λίστας
    megisto = lista[i]
  # Αυξάνουμε το i κατά 1
  i += 1

# Εκτύπωση του μέγιστου αριθμού
print("Ο μέγιστος αριθμός είναι το: %d" % megisto)

# Αρχικοποίηση της μεταβλητής
i = 0

# Για όσο το i είναι μικρότερο από το μήκος της λίστας
while i < len(lista):
  # Εάν το στιγμιαίο στοιχείο της λίστας είναι μικρότερο από το elaxisto που ορίσαμε
  if lista[i] < elaxisto:
    # Εκχωρούμε στο elaxisto το στιγμιαίο στοιχείο της λίστας
    elaxisto = lista[i]
  i += 1

# Εκτύπωση του ελάχιστου αριθμού
print("Ο ελάχιστος αριθμός είναι το: %d" % elaxisto)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-05-example-03.py).

## 5.5 Έυρεση MIN

---

```python
# Αρχικοποίηση μεταβλητών
lista = [3, 4, 1, 9, 7, 2]
elaxisto = lista[0]
i = 0

# Για όσο το i είναι μικρότερο από το μήκος της λίστας
while i < len(lista):
  # Εάν το στιγμιαίο στοιχείο της λίστας είναι μικρότερο από το ελάχιστο που ορίσαμε
  if lista[i] < elaxisto:
    # Εκχωρούμε στο elaxisto το στιγμιαίο στοιχείο της λίστας
    elaxisto = lista[i]
  # Αυξάνουμε το i κατά 1
  i += 1

# Εκτύπωση του ελάχιστου
print("Ελάχιστο:", elaxisto)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-05-example-04.py).

## 5.6 Έυρεση MAX με θέση

---

```python
# Αρχικοποίηση μεταβλητών
lista = [3, 4, 1, 9, 4, 2]
maxThesi = 0
i = 0

# Για όσο το i είναι μικρότερο από το μήκος της λίστας
while i < len(lista):
  if lista[i] > lista[maxThesi]:
    # Εκχωρούμε στο maxThesi το στιγμιαίο i
    maxThesi = i
  # Αυξάνουμε το i κατά 1
  i += 1

# Εκτύπωση της μέγιστης θέσης
print("Μέγιστη θέση:", maxThesi)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-05-example-05.py).

## 5.7 Αναζήτηση στοιχείων I

---

```python
# Δημιουργία λίστας
lista = [3, 4, 1, 9, 4, 2]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητής
i = 0

# Για όσο το i είναι μικρότερο από το μήκος της λίστας
while i < len(lista):
  # Εάν το key είναι ίσο με το στιγμιαίο στοιχείο της λίστας
  if key == lista[i]:
    # Εκχωρούμε στη thesi το στιγμιαίο i
    thesi = i
  # Αυξάνουμε το i κατά 1
  i += 1

# Εκτύπωση της θέσης από το στοιχείο που αναζητάει ο χρήστης
print("Το στοιχείο που αναζητάς βρίσκεται στη θέση:", thesi)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-05-example-06.py).

## 5.8 Αναζήτηση στοιχείων II

---

```python
# Δημιουργία λίστας
lista = [3, 4, 1, 9, 7, 2]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
found = False
i = 0

# Για όσο το i είναι μικρότερο από το μήκος της λίστας και ταυτόχρονα το found δεν είναι False
while (i < len(lista)) and (not found):
  # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
  if lista[i] == key:
    # Εκχωρούμε στη thesi το στιγμιαίο i
    thesi = i
    # Το found γίνεται True
    found = True
  # Αυξάνουμε το i κατά 1
  i += 1

# Εκτύπωση της θέσης από το στοιχείο που αναζητάει ο χρήστης
print("Το στοιχείο που αναζητάς βρίσκεται στη θέση:", thesi)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-05-example-07.py).

## 5.9 Αναζήτηση αριθμού στοιχείων

---

```python
# Δημιουργία λίστας
lista = [3, 4, 1, 9, 7, 2, 1, 4, 5, 1]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
counter = 0
i = 0

# Για όσο το i είναι μικρότερο από το μήκος της λίστας
while i < len(lista):
  # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
  if lista[i] == key:
    # Αυξάνουμε το counter κατά 1
    counter += 1
  # Αυξάνουμε το i κατά 1
  i += 1

# Εκτύπωση των φορών που εμφανίζεται το στοιχείο
print("Το στοιχείο που αναζητάς εμφανίζεται %d φορές στη λίστα." % counter)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-05-example-08.py).
