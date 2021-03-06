# 10 Υποπρογράμματα

---

## Περιεχόμενα

- 10.1 Υποπρογράμματα
- 10.2 Παραδείγματα
- 10.3 Ασκήσεις

## 10.1 Υποπρογράμματα

---

```python
# Δημιουργία συνάρτησης readAndCheck
def readAndCheck():
  # Αρχικοποίηση μεταβλητής
  good = True
  # Για όσο το good είναι True
  while good:
    # Ζητάμε από το χρήστη να δώσει αριθμό
    num = input("Δώσε αριθμό: ")
    # Κάνουμε έλεγχο ορθότητας
    while not num.isdigit():
      # Ζητάμε από το χρήστη να δώσει σωστά τον αριθμό
      num = input("Δώσε αριθμό: ")
    # Μετατρέπουμε τον αριθμό σε ακέραιο
    num = int(num)
    # Εάν ο αριθμός είναι μεγαλύτερο η ίσος από το 0 ή μικρότερος ή ίσος από το 10
    if 0 <= num <= 10:
      # Το good γίνεται False
      good = False
  # Επιστρέφει το num
  return num
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-10-example-01.py).

## 10.2 Παραδείγματα

---

### Παράδειγμα 1

Να γραφεί μια συνάρτηση η οποία θα δέχεται μια λίστα με αριθμούς και θα την ταξινομεί.

```python
# Δημιουργία συνάρτησης sort
def sort(listaP):
  for i in range(1, len(listaP)):
    for j in range(len(listaP) - 1, 0, -1):
      if listaP[j - 1] > listaP[j]:
        # Swap listaP
        temp = listaP[j - 1]
        listaP[j - 1] = listaP[j]
        listaP[j] = temp
  # Eπιστροφή listaP στη main
  return listaP


# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

x = sort(lista[:])
print(x)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-10-example-02.py).

### Παράδειγμα 2

Να γραφεί ένα πρόγραμμα το οποίο θα διαβάζει (με έλεγχο ορθότητας) τους βαθμούς 10 μαθητών για δέκα μαθήματα και θα εκτυπώνει, για κάθε μάθημα τους βαθμούς ταξινομημένους.

```python
# Δημιουργία συνάρτησης readAndCheck
def readAndCheck():
  # Αρχικοποίηση μεταβλητής
  good = True
  # Για όσο το good είναι True
  while good:
    # Ζητάμε από το χρήστη να δώσει αριθμό
    num = input("Δώσε αριθμό: ")
    # Κάνουμε έλεγχο ορθότητας
    while not num.isdigit():
      # Ζητάμε από το χρήστη να δώσει σωστά τον αριθμό
      num = input("Δώσε αριθμό: ")
    # Μετατρέπουμε τον αριθμό σε ακέραιο
    num = int(num)
    # Εάν ο αριθμός είναι μεγαλύτερο η ίσος από το 0 ή μικρότερος ή ίσος από το 10
    if 0 <= num <= 10:
      # Το good γίνεται False
      good = False
  # Επιστρέφει το num
  return num


# Δημιουργία συνάρτησης sort
def sort(listP):
  """ Αυτή η συνάρτηση ταξινομεί τη λίστα κατά αύξουσα σειρά."""
  for i in range(1, len(listP)):
    for j in range(len(listP) - 1, 0, -1):
      if listP[j - 1] > listP[j]:
        # Swap listP
        temp = listP[j - 1]
        listP[j - 1] = listP[j]
        listP[j] = temp
  # Επιστρέφει το listP
  return listP


# Δημιουργία συνάρτησης readMarks
def readMarks():
  # Δηνιουργία κενής λίστας
  vathmoi = []
  # Για 10 φορές
  for i in range(10):
    # Αποθηκεύουμε στη λίστα vathmoi στα στοιχεία που θα πάρουμε από τη συνάρτησηreadAndCheck
    vathmoi.append(readAndCheck())
  # Επιστρέφει το vathmoi
  return vathmoi


# Αρχικοποίηση μεταβλητής
MAX_ELEMENTS = 10

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
  # Καλούμε τη συνάρτηση readMarks
  vathmoi = readMarks()
  # Εκτύπωση της ταξινομημένης λίστας
  print(sort(vathmoi))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-10-example-03.py).

## 10.3 Ασκήσεις

---

Συνιστάται να τρέξετε όλα τα προγράμματα των ασκήσεων. Όταν κάνετε επικόλληση σε κάποιον editor προσέξτε ότι συχνά τα προγράμματα από ορισμένα αρχεία δεν μεταφέρονται πάντα σωστά.

### Άσκηση 1

Να συμπληρωθεί το παρακάτω πρόγραμμα, ώστε:

- να ζητάει από το χρήστη το πλήθος των ονομάτων που θα
διαβαστούν,
- να υπολογίζει και να εμφανίζει το μήκος του μακρύτερου ονόματος.

```python
# Δημιουργία συνάρτησης readNames
def readNames(plithos):
  # Δημιουργία κενής λίστας
  onomata = []
  # Για όσο είναι το plithos
  for i in range(plithos):
    # Ζητάμε από το χρήστη να δώσει το όνομά του
    onoma = input("Δώσε όνομα:")
    # Αποθηκεύουμε το όνομα στη λίστα onomata
    onomata.append(onoma)
  # Επιστρέφει τη λίστα onomata
  return onomata


# Δημιουργία συνάρτησης longestName
def longestName(list):
  # Αρχικοποίηση μεταβλητής
  maxLength = 0
  # Για κάθε όνομα στη λίστα
  for onoma in list:
    if len(onoma) > maxLength:
      maxLength = len(onoma)
  # Επιστρέφει το maxLength
  return maxLength


# Ζητάμε από το χρήστη να δώσει πλήθος και το μετατρέπουμε σε ακέραιο
plithos = int(input("Δώσε πλήθος: "))
# Καλούμε τη συνάρτηση readNames
onomata = readNames(plithos)
# Καλούμε τη συνάρτηση longestName
x = longestName(onomata)

# Εκτύπωση του μήκους από το μακρύτερο όνομα
print("Το μακρύτερο όνομα έχει μήκος: %d" % x)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-10-exercise-01.py).

### Άσκηση 2

Να γραφεί πρόγραμμα το οποίο:

- Θα έχει μια συνάρτηση η οποία θα παίρνει έναν αριθμό και θα
επιστρέφει το τετράγωνό του.
- Η συνάρτηση θα χρησιμοποιείτε σε ένα for loop για να υπολογίσει το άθροισμα των τετράγωνων όλων των αριθμών μέχρι και αυτόν που δώσατε.

```python
# Δημιουργία συνάρτησης square
def square(number):
  # Πολλαπλασιάσουμε κάθε φορά το number
  number *= number
  # Επιστρέφει το number
  return number


# Ζητάμε από το χρήστη να δώσει αριθμό και το μετατρέπουμε σε ακέραιο
num = int(input("Δώσε αριθμό: "))

# Αρχικοποίηση μεταβλητής
athroisma = 0

for i in range(1, num + 1):
  # Καλούμε τη συνάρτηση square
  number = square(i)
  athroisma += number

# Εκτύπωση του αθροίσματος
print(athroisma)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-10-exercise-02.py).

### Άσκηση 3

Να γραφεί πρόγραμμα το οποίο:

- Θα έχει μια συνάρτηση η οποία θα διαβάζει σε λίστα, Ν βαθμούς
φοιτητών και θα την επιστρεφεί.
- Θα έχει μια συνάρτηση η οποία θα δέχεται μία λίστα και θα
επιστρέφει το μέγιστο στοιχείο της.
- Θα έχει μια συνάρτηση η οποία θα δέχεται μια λίστα και θα
επιστρεφεί τον μέσο όρο των στοιχείων της.
- Θα διαβάζει πόσοι φοιτητές έγραψαν εξετάσεις σε ένα μάθημα.
- Με τη χρήση συνάρτησης θα διαβάζει τους βαθμούς τους.
- Με τη χρήση συνάρτησης θα υπολογιζεί και θα εκτυπώνει τον
μέγιστο βαθμό και τον μέσο όρο.

```python
# Δημιουργία συνάρτησης readMarks
def readMarks(N):
  # Δημιουργία κενής λίστας
  marks = []
  for i in range(N):
    # Ζητάμε από το χρήστη να δώσει βαθμό και το μετατρέπουμε σε ακέραιο
    mark = int(input("Δώσε βαθμό: "))
    # Αποθηκεύουμε το mark στη λίστα marks
    marks.append(mark)
  # Επιστρέφει το marks
  return marks


# Δημιουργία συνάρτησης getMax
def getMax(listaP):
  # Αρχικοποίηση μεταβλητής
  megisto = 0
  for i in listaP:
    # Εάν το στιγμιαίο στοιχείο της λίστας είναι μεγαλύτερο από το megisto
    if i > megisto:
      # Αποθηκεύουμε στο megisto το στιγμιαίο στοιχείο
      megisto = i
  # Επιστρέφει το megisto
  return megisto


# Δημιουργία συνάρτησης getMO
def getMO(listaP):
  # Αρχικοποίηση μεταβλητής
  souma = 0
  # Για κάθε στοιχείο της λίστας
  for i in listaP:
    souma += i
  # Επιστρέφει στη main το souma / len(listaP)
  return souma / len(listaP)


# Ζητάμε από το χρήστη να δώσει τα μαθήματα που δώθηκαν και το μετατρέπουμε σε ακέραιο
plithos = int(input("Πόσοι δώσανε το μάθημα:"))

# Καλούμε τη συνάρτηση readMarks
vathmoi = readMarks(plithos)

# Εκτύπωση του μέγιστου
print("Μέγιστος: %d" % getMax(vathmoi))
# Εκτύπωση του μέσου όρου
print("Mέσος όρος: %d" % getMO(vathmoi))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-10-exercise-03.py).

### Άσκηση 4

Να γραφεί πρόγραμμα το οποίο:

- Με τη χρήση συνάρτησης θα διαβάζει και αποθηκεύει τα ονόματα δέκα
μαθητριών (ένα όνομα μπορεί να επαναλαμβάνεται πολλές φορές).
- Στη συνέχεια με μία νέα συνάρτηση θα δέχεται τη λίστα των ονομάτων και θα επιστρέφει μία νέα λίστα η οποία θα περιέχει μοναδικά στοιχεία (το κάθε όνομα μία μόνο φορά).
- Στο κυρίως πρόγραμμα θα εμφανίζεται η λίστα με τα μοναδικά στοιχεία και στη συνέχεια ο χρήστης θα διαβάζει ένα τυχαίο όνομα.
- Με τη χρήση νέας συνάρτησης θα αναζητά αν το τυχαίο όνομα που δόθηκε περιλαμβάνεται μέσα στη λίστα. Στην περίπτωση που δεν υπάρχει θα εκτυπώνει μήνυμα «Το όνομα που αναζητάς δεν είναι στη λίστα», σε οποιαδήποτε άλλη περίπτωση το μήνυμα θα είναι «Το όνομα `onoma` είναι στη λίστα».

```python
# Δημιουργία συνάρτησης eisagogiStoixeion
def eisagogiStoixeion():
  # Δημιουργία κενής λίστας
  onomata = []
  # Για 10 φορές
  for i in range(10):
    # Ζητάμε από το χρήστη να δώσει το όνομά του
    name = input("Δώσε όνομα: ")
    # Αποθηκεύουμε το όνομα στη λίστα onomata
    onomata.append(name)
  # Επιστρέφει τη λίστα onomata
  return onomata


# Δημιουργία συνάρτησης monadikiLista
def monadikiLista(listaP):
  # Δημιουργία κενής λίστας
  neaLista = []
  # Για κάθε στοιχείο της λίστας
  for i in listaP:
    # Eάν το στοιχείο δεν είναι στη neaLista
    if i not in neaLista:
      # Αποθηκεύουμε το στιγμιαίο στοιχείο στη neaLista
      neaLista.append(i)
  # Επιστρέφει τη neaLista
  return neaLista


# Δημιουργία συνάρτησης anazitisi
def anazitisi(key, listaP):
  # Αρχικοποίηση μεταβλητής
  done = True
  # Για κάθε στοιχείο της λίστας
  for i in listaP:
    # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
    if i == key:
      # Το done γίνεται False
      done = False
  # Επιστρέφει το done
  return done


# Καλούμε τη συνάρτηση eisagogiStoixeion
onomata = eisagogiStoixeion()
# Εκτύπωση της μοναδικής λίστας καλώντας τη συνάρτηση
print(monadikiLista(onomata))

# Ζητάμε από το χρήστη να δώσει το όνομα που αναζητά
stoixeio = input("Δώσε όνομα που αναζητάς: ")

# Καλούμε τη συνάρτηση anazitisi
done = anazitisi(stoixeio, onomata)

# Εάν το done είναι ίσο με True
if done == True:
  print("Το όνομα που αναζητάς δεν είναι στη λίστα.")
else:
  print("Το όνομα %s είναι στη λίστα." % stoixeio)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-10-exercise-04.py).
