# 6 Δομή Επανάληψης - Η εντολή for

---

## Περιεχόμενα

---

- 6.1 Η εντολή for
- 6.2 Παραδείγματα
- 6.3 Ασκήσεις

## 6.1 Η εντολή for

---

```python
for i in list:
    ...E1
    ...E2
```

Η μεταβλητή i, σε κάθε επανάληψη, θα παίρνει την επομένη τιμήτης λίστας list.

```python
for i in range([start], stop, [step]):
  ...E1
  ...E2
```

- start, ο αριθμός εκκίνησης (Προαιρετικό,ΑρχικήΤιμή = 0)
- stop, δημιούργησε αριθμούς μέχρι (αλλά χωρίς) τον stop
- step, η διαφορά μεταξύ δύο αριθμών (Προαιρετικό, Αρχική Τιμή = 1)

## 6.2 Παραδείγματα

---

### Παράδειγμα 1

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται έναν αριθμό και θα τυπώνει το άθροισμα όλων των ακεραίων μέχρι και αυτόν τον αριθμό.

```python
# Αρχικοποίηση μεταβλητής
athroisma = 0

# Ζητάμε από το χρήστη να δώσει έναν αριθμό
number = int(input("Δώσε αριθμό: "))

# Για number φορές
for i in range(number + 1):
  # Προσθέτουμε τον αριθμό στη μεταβλητή athroisma
  # και το εκχωρούμε στην ίδια μεταβλητή athroisma
  athroisma = athroisma + i

# Εκτύπωση αθροίσματος
print("Άθροισμα: %d" % athroisma)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-06-example-01.py).

### Παράδειγμα 2

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται έναν αριθμό και θα ελέγχει εάν είναι πρώτος.(Πρώτος είναι ένας αριθμός που διαιρείται μόνο από το 1 και τον εαυτό του). Να μην γίνει έλεγχος ορθότητας του φυσικού αριθμού.

```python
# Αρχικοποίηση μεταβλητών
prime = True

# Ζητάμε από το χρήστη να δώσει έναν φυσικό αριθμό
number = int(input("Δώσε έναν φυσικό αριθμό: "))

if number == 1:
  prime = False
else:
  # Για κάθε αριθμό απο το 2 εως και τον αριθμό αυτόν
  for i in range(2, number // 2 + 1):
    # Εάν βρεθεί διαιρέτης που να διαιρεί τον αριθμό
    if number % i == 0:
      # Τότε ο αριθμός δεν είναι πρώτος
      prime = False

# Εκτύπωση αποτελέσματος
if prime == True:
  print("\nO αριθμός %d είναι πρώτος αριθμός." % number)
else:
  print("\nO αριθμός %d δεν είναι πρώτος αριθμός." % number)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-06-example-02.py).

### Παράδειγμα 3

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται μία λέξη και θα μετράει πόσες φορές περιέχει το γράμμα 'e'.

```python
# Αρχικοποίηση μεταβλητών
counter = 0

# Ζητάμε από το χρήστη να δώσει μια λέξη
leksi = input("Δώσε λέξη με λατινικούς χαρακτήρες: ")

# Για κάθε γράμμα της λέξης
for gramma in leksi:
  # Εάν το γράμμα είναι το 'e'
  if gramma == 'e':
    # Αυξάνουμε το μετρητή κατά 1
    counter += 1

# Eάν ο μετρητής είναι 1
if counter == 1:
  print("Το γράμμα 'e' εισήχθη %d φορά." % counter)
# Αλλιώς εάν ο μετρητής δεν είναι ουτε 0 ούτε 1
elif counter != 0:
  print("Το γράμμα 'e' εισήχθη %d φορές." % counter)
# Αλλιώς το γράμμα 'e' δεν εισήχθη
else:
  print("Το γράμμα 'e' δεν εισήχθη.")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-06-example-03.py).

## 6.3 Ασκήσεις

---

Συνιστάται να τρέξετε όλα τα προγράμματα των ασκήσεων. Όταν κάνετε επικόλληση σε κάποιον editor προσέξτε ότι συχνά τα προγράμματα από ορισμένα αρχεία δεν μεταφέρονται πάντα σωστά.

### Άσκηση 1

Μία αθλήτρια του στίβου αγωνίστηκε στο έπταθλο. Να γραφεί πρόγραμμα που θα διαβάζει τη βαθμολογία σε κάθε ένα από τα 7 αθλήματα που συμμετείχε (ο βαθμός είναι ακέραιος αριθμός μεταξύ 0- 20). Για να βγει η τελική βαθμολογία κάθε αθλήματος, η βαθμολογία του πρώτου αθλήματος πολλαπλασιάζεται με το 5, του δεύτερου αθλήματος με το 10, του τρίτου με το 15, του τετάρτου με το 20, του πέμπτου με το 25, του έκτου με το 30 και του έβδομου με το 35. Ο τελικός βαθμός είναι ο μέσος όρος της τελικής βαθμολογίας των επτά αθλημάτων. Το πρόγραμμα να εμφανίζει τον τελικό βαθμό.

**1ος τρόπος:**

```python
# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 7
lista = []

# Για κάθε MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
  # Διαβάζουμε από το χρήστη το βαθμό του και το μετατρεπουμε σε ακέραιο
  vathmos = int(input("Δώσε βαθμό: "))
  # Αποθηκεύουμε το βαθμό στη λίστα
  lista.append(vathmos)

# Αρχικοποίηση μεταβλητών
athroisma = 0
k = 1

# Για κάθε στοιχείο της λίστας
for agwnisma in lista:
  # Κάθε φορά πενταπλασιάζουμε το κάθε αγώνισμα
  agwnisma *= 5 * k
  # Αυξάνουμε τη μεταβλητή k κατά 1
  k += 1
  # Αυξάνουμε το άθροισμα κατα agwnisma
  athroisma += agwnisma

# Υπολογισμός του μέσου όρου
mo = athroisma / MAX_ELEMENTS

# Εκτύπωση μέσου όρου
print("Ο μέσος όρος είναι %.1f." % mo)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-06-exercise-01a.py).

**2ος τρόπος:**

```python
# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 7
athroisma = 0

for i in range(5, 36, 5):
  # Διαβάζουμε από το χρήστη το βαθμό του και το μετατρεπουμε σε ακέραιο
  vathmos = int(input("Δώσε βαθμολογία για αγώνισμα: "))
  athroisma = athroisma + i * vathmos

# Υπολογισμός του μέσου όρου
mo = athroisma / MAX_ELEMENTS

# Εκτύπωση μέσου όρου
print("Ο μέσος όρος είναι %.1f." % mo)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-06-exercise-01b.py).

### Άσκηση 2

Να γραφεί πρόγραμμα το οποίο θα διαβάζει 10 αριθμούς. Μετά θα δέχεται έναν αριθμό και θα εμφανίζει στο χρήστη ποιοι από τους αριθμούς που εισήχθησαν διαιρούνται από αυτόν.

```python
# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 10
lista = []

# Για κάθε MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
  # Ζητάμε από το χρήστη να δώσει έναν αριθμό και τον αποθηκεύουμε στη λίστα
  lista.append(int(input("Δώσε αριθμό: ")))

# Ζητάμε απο το χρήστη να δώσει αριθμό για έλεγχο διαιρετέων
num = int(input("Δώσε αριθμό για έλεγχο διαιρετέων: "))

# Για κάθε αριθμό στη λίστα
for arithmos in lista:
  # Εάν ο αριθμός διαιρείται
  if arithmos % num == 0:
    # Εμφανίζουμε τον αριθμό
    print(arithmos)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-06-exercise-02.py).

### Άσκηση 3

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται από το χρήστη έναν αριθμό ν και θα εμφανίζει τους πρώτους αριθμούς μεταξύ 1 – ν.

```python
# Ζητάμε από το χρήστη να δώσει έναν αριθμό
number = int(input("Δώσε αριθμό: "))

# Για κάθε αριθμό από το 2 εώς και το number
for i in range(2, number + 1):
  prime = True
  # Για κάθε αριθμό απο το 2 εως και το number
  for j in range(2, i // 2 + 1):
    # Εάν βρεθεί διαιρέτης που να διαιρεί το i
    if i % j == 0:
      # Τότε ο αριθμός δεν είναι πρώτος
      prime = False
  # Εάν ο αριθμός είναι πρώτος
  if prime:
    # Εμφανίζουμε τον πρώτο αριθμό i
    print(i)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-06-exercise-03.py).

### Άσκηση 4

Να γραφεί ένα πρόγραμμα που θα δέχεται από το χρήστη μια λέξη και θα εμφανίζει πόσες φορές εμφανίστηκε το κάθε γράμμα.

```python
# Αρχικοποίηση μεταβλητής
alfabito = "abcdefghijklmnopqrstuvwxyz"

# Ζητάμε από το χρήστη να δώσει μια λέξη
leksi = input("Δώσε λέξη με λατινικούς χαρακτήρες: ").lower()

# Για κάθε γράμμα του λατινικού αλφαβήτου
for gramma in alfabito:
  # Αρχικοποιήση του μετρητή
  counter = 0
  # Για κάθε γράμμα της λέξης
  for grammaLeksis in leksi:
    # Εάν το γράμμα της λέξης είναι ίσο με το στιγμιαίο γράμμα
    if grammaLeksis == gramma:
      # Αυξάνουμε το μετρητή κατά 1
      counter += 1
  # Εάν ο μετρητής είναι 1
  if counter == 1:
    print("To γράμμα '%s' εμφανίστηκε %d φορά." % (gramma, counter))
  # Αλλιώς εάν ο μετρητής δεν είναι ούτε 0 αλλά ούτε 1
  elif counter != 0:
    print("To γράμμα '%s' εμφανίστηκε %d φορές." % (gramma, counter))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-06-exercise-04.py).

### Άσκηση 5

Να γραφεί ένα πρόγραμμα που θα δέχεται έναν νιοστό όρο και θα επιστρέφει τον νιοστό αριθμό Fibonacci. Στον παρακάτω πίνακα μπορείτε να δείτε τον αριθμό που επιστρέφει η ακολουθία Fibonacci ανάλογα τον αριθμό που δίνουμε.

![Fibonacci 1](../images/fibonacci_1.PNG)

Ένας αριθμός Fibonacci υπολογίζεται από τον τύπο:

![Fibonacci 2](../images/fibonacci_2.PNG)

```python
# Ζητάμε από το χρήστη να δώσει τον νιοστό όρο Fibonacci
fibNo = input("Δώσε νιοστό όρο Fibonacci (int): ")

# Όσο ο νιοστός όρος δεν είναι αριθμός
while not fibNo.isdigit():
  # Ζητάμε από το χρήστη να δώσει σωστό νιοστό όρο Fibonacci
  fibNo = input("Δώσε έναν ακέραιο νιοστό όρο Fibonacci: ")

# Μετατρέπουμε τον νιοστό όρο σε ακέραιο αριθμό
fibNo = int(fibNo)

# Αρχικοποίηση μεταβλητών
fibMinus2 = 0
fibMinus1 = 1

# Εάν ο νιοστός όρος Fibonacci είναι 1
if fibNo == 1:
  fib = 1
# Αλλιώς εάν ο νιοστός όρος Fibonacci είναι 0
elif fibNo == 0:
  fib = 0
# Αλλιώς εάν ο νιοστός όρος Fibonacci δεν είναι ούτε 0 ούτε 1
else:
  # Για κάθε νιοστό αριθμό - 1
  for i in range(fibNo - 1):
    # Ο αριθμός Fibonacci προκύπτει από το άθροισμα του ν-1 και ν-2
    fib = fibMinus1 + fibMinus2
    # Ο ν-2 όρος είναι ο ν-1
    fibMinus2 = fibMinus1
    # Ο ν-1 είναι ο αριθμός Fibonacci
    fibMinus1 = fib

# Εκτύπωση νιοστού αριθμού Fibonacci
print(fib)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-06-exercise-05.py).
