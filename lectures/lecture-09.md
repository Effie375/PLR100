# 9 Υποπρογράμματα

Σε αυτό το κεφάλαιο θα αναφερθόυμε στη χρήση των συναρτήσεων στη Python. Θα δούμε αναλυτικά πως μπορούμε να ορίσουμε και να καλέσουμε συναρτήσεις αλλά και το πώς μια τέτοια συνάρτηση επιστρέφει τιμές πίσω στο πρόγραμμα μας.

---

## Περιεχόμενα

---

- 9.1 Εισαγωγή
- 9.2 Ορισμός συνάρτησης
- 9.3 Συναρτήσεις χωρίς παραμέτρους
- 9.4 Συναρτήσεις με παραμέτρους
- 9.5 Συναρτήσεις που επιστρέφουν τιμή
- 9.6 Συναρτήσεις που δεν επιστρέφουν τιμή
- 9.7 Κλήση συνάρτησης
- 9.8 Λυμένα Παραδείγματα

## 9.1 Εισαγωγή

---

Οι συναρτήσεις μας βοηθούν να "σπάσουμε" μεγάλα προγράμματα σε μικρότερες ομάδες, οι οποίες επιτελούν και μια συγκεκριμένη λειτουργία.

Οι συναρτήσεις στον προγραμματισμό είναι επαναχρησιμοποιήσιμα μέρη προγραμμάτων. Μια συνάρτηση μπορεί να δεχθεί τιμές και να επιστρέψει τιμές. Μια νέα συνάρτηση δημιουργεί μικρότερα προγράμματα, απομακρύνοντας τμήματα κώδικα που μπορεί να επαναλαμβάνονται.

## 9.2 Ορισμός συνάρτησης

---

Η πρώτη γραμμή του ορισμού μιας συνάρτησης είναι η επικεφαλίδα της συνάρτησης. Η επικεφαλίδα ξεκινάει με τη δεσμευμένη λέξη `def` ακολουθούμενη από το όνομα της συνάρτησης, ένα ζευγάρι παρενθέσεων που προαιρετικά περικλείει μια διαχωριζόμενη με κόμματα λίστα παραμέτρων (parameters) και τελειώνει με μια άνω κάτω τελεία. Κάτω από την επικεφαλίδα ακολουθεί το σώμα της συνάρτησης (οι εντολές της συνάρτησης) σε εσοχή.

Τα ονόματα των συναρτήσεων δίνονται με βάση τους ίδιους κανόνες που είδαμε και για τα ονόματα των μεταβλητών. Καλό είναι να δίνουμε ονόματα σχετικά με τη λειτουργία που επιτελούν οι συναρτήσεις. Οι συναρτήσεις ορίζονται συνήθως στην αρχή των προγραμμάτων. Είναι προφανές όμως ότι μια συνάρτηση πρέπει να οριστεί πρώτα πριν χρησιμοποιηθεί (κληθεί). Μπορούμε να καλούμε μία συνάρτηση όσες φορές απαιτούνται για τη λύση του προβλήματος που αντιμετωπίζει το πρόγραμμά μας. Μάλιστα κάτι τέτοιο είναι πολύ συνηθισμένο και χρήσιμο.

## 9.3 Συναρτήσεις χωρίς παραμέτρους

---

Οι πιο απλές συναρτήσεις στη Python δεν έχουν παραμέτρους. Σε αυτήν την περίπτωση όταν τις καλούμε δεν μπορούμε να τους μεταβιβάσουμε πληροφορίες. Μια τέτοια συνάρτηση μπορούμε να την παρομοιάσουμε σαν ένα κλειστό κουτί το οποίο επιτελεί μια συγκεκριμένη λειτουργία και δεν μπορούμε με κανέναν τρόπο αυτήν την λειτουργία να την τροποποιήσουμε.

Ας δούμε ένα απλό παράδειγμα στο οποίο δεν έχουμε παραμέτρους. Η παρακάτω συνάρτηση περιέχει μόνο μία εντολή για την εκτύπωση ενός μηνύματος `Goodbye!`:

```python
def say_goodbye():
    print("Goodbye!")
```

Από τη στιγμή που στη συνάρτηση δεν έχουμε μεταβιβάσει παραμέτρους, δεν μπορεί να επηρεαστεί η λειτουργία της.

## 9.4 Συναρτήσεις με παραμέτρους

---

<!-- *** -->
Οι παράμετροι είναι ένας τρόπος με τον οποίο ένα τμήμα προγράμματος μεταβιβάζει πληροφορίες σε μια συνάρτηση.

Μπορούμε να παρομοιάσουμε μια τέτοια συνάρτηση σαν ένα κουτί το οποίο διαθέτει οπές, μέσω των οποίων μπορούμε να μεταβιβάζουμε πληροφορίες.

Αν στο σώμα της συνάρτησης δεν υπάρχει η εντολή `return`, η συνάρτηση επιστρέφει στο κυρίως πρόγραμμα μόλις εκτελέσει την τελευταία πρόταση της συνάρτησης, χωρίς όμως να επιστρέψει κάποια συγκεκριμένη τιμή.
<!-- /*** -->

## 9.5 Συναρτήσεις που επιστρέφουν τιμή

---

Μια συνάρτηση μπορεί να επιστρέψει μια τιμή στο κυρίως πρόγραμμα μέσω της εντολής `return`.

Ας δούμε το παράδειγμα μιας συνάρτησης που δέχεται ως όρισμα έναν αριθμό και επιστρέφει το διπλάσιο του:

```python
def diplasio(x):
    return 2 * x

print(diplasio(3))
```

## 9.6 Συναρτήσεις που δεν επιστρέφουν τιμή

---

<!-- *** -->
Μια συνάρτηση μπορεί να μην επιστρέφει τιμή, αλλά απλώς να εκτελεί μια συγκεκριμένη λειτουργία. Η συνάρτηση που ακολουθεί δεν επιστρέφει καμία τιμή, και επιστρέφει στο κυρίως πρόγραμμα αφού εκτελέσει και την τελευταία πρόταση.
<!-- /*** -->

```python
def diplasio(x):
    print(2 * x)

diplasio(3)
```

## 9.7 Κλήση συνάρτησης

---

Κατά την κλήση μιας συνάρτησης οι τιμές που παίρνουν οι παράμετροι ονομάζονται **ορίσματα** (actual arguments ή απλά arguments). Με απλά λόγια, για να μην μπερδευόμαστε, στον ορισμό μιας συνάρτησης έχουμε **παραμέτρους** (ονομασίες μεταβλητών) και στην κλήση μιας συνάρτησης έχουμε ορίσματα (τιμές ή μεταβλητές στις οποίες έχουν εκχωρηθεί τιμές).

Ας δούμε ένα παράδειγμα στο οποίο ορίζουμε και καλούμε μία συνάρτηση:

```python
def multiple(num1, num2): # ορισμός της συνάρτησης multiple με παραμέτρους num1 και num2
    mul = num1 * num2

multiple(2,3) # κλήση συνάρτησης με ορίσματα απευθείας τιμές
x = 4
y = 5
multiple(x,y) # κλήση συνάρτησης με ορίσματα μεταβλητές
multiple(x, 3) # κλήση συνάρτησης με ορίσματα μεταβλητή και τιμή
```

<!-- *** -->
**Συχνό λάθος**: Νομίζουμε ότι μέσα από μια συνάρτηση μπορούμε να έχουμε πρόσβαση σε μεταβλητές που δηλώνονται μέσα σε άλλες συναρτήσεις. Αυτό δεν είναι δυνατό, επειδή οι μεταβλητές που δηλωνονται μέσα σε μια συνάρτηση έχουν τοπική εμβέλεια, μόνο μέσα στη συνάρτηση όπου δηλώθηκαν.
<!-- /*** -->

## 9.8 Λυμένα Παραδείγματα

---

### 9.8.1 Παράδειγμα 1

---

```python
# Δημιουργία συνάρτησης sunolo
def sunolo(x, y):
  # Υπολογίζουμε το άθροισμα των δύο παραμέτρων
  athroisma = x + y
  # Επιστρέφει το άθροισμα
  return athroisma


# Δημιουργία συνάρτησης sayHello
def sayHello():
  # Εκτύπωση Hello
  print("Hello")
# Δεν επιστρέφει κάτι άρα δε χρειάζεται return


# -------main--------
# Αρχικοποίηση μεταβλητών
x = 3
y = 4

# Καλόυμε τη συνάρτηση sunolo
athroisma = sunolo(x, y)
# Εκτύπωση το άθροισμα
print(athroisma)

# Καλόυμε τη συνάρτηση sayHello
sayHello()
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-09-example-01.py).

### 9.8.2 Παράδειγμα 2

---

```python
# Δημιουργία συνάρτησης sayHello
def sayHello(onoma="Human"):
  # Εκτύπωση Hello και όνομα
  print("Hello %s" % onoma)


# Δημιουργία συνάρτησης modDiv
def modDiv(x, y):
  # Υπολόγίζουμε το ακέραιο υπόλοιπο της διαίρεσης
  mod = x % y
  # Υπολογίζουμε το ακέραιο πηλίκο της διαίρεσης
  div = x // y
  # Επιστρέφει το mod και το div
  return mod, div


# -------main--------
# Καλούμε τις συναρτήσεις
sayHello()
sayHello("Chris")
a, b = modDiv(10, 3)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-09-example-02.py).

### 9.8.3 Παράδειγμα 3

---

```python
# Δημιουργία συνάρτησης searchFunction
def searchFunction(pLista, key):
  # Αρχικοποίηση συνάρτησης
  counter = 0
  # Για κάθε στοιχείο της λίστας
  for i in pLista:
    # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
    if i == key:
      # Αυξάνουμε τον counter κατά 1
      counter += 1
  # Επιστρέφει τον counter
  return counter


# Δημιουργία λιστών
lista = [[1, 2, 3, 1],
         [6, 6, 7, 8],
         [9, 1, 1, 2],
         [9, 3, 3, 6]]
searchKey = [1, 3, 6, 9]
# Δημιουργία κενής λίστας
results = []

# Για κάθε στοιχείο της λίστας searchKey
for key in searchKey:
  # Αρχικοποίηση μεταβλητής
  s = 0
  # Για κάθε υπολίστα της λίστας
  for ypolista in lista:
    # Καλούμε τη συνάρτηση searchFunction
    k = searchFunction(ypolista, key)
    # Αυξάνουμε το s κατά k
    s += k
  # Αποθηκεύουμε το s στη λίστα results
  results.append(s)

# Εκτύπωση της λίστας results
print(results)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-09-example-03.py).

### 9.8.4 Παράδειγμα 4

---

```python
# Δημιουργία συνάρτησης athroisma
def athroisma(listaNew):
  # Για κάθε στοιχείο της λίστας
  for item in listaNew:
    item.sort(reverse=True)


# Δημιουργία λίστας
lista = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 1, 1, 2],
         [3, 4, 5, 6]]

# Για κάθε στοιχείο της λίστας
for item in lista:
  # Εκτύπωση το στιγμιαίο στοιχείο της λίστας
  print(item)

# Καλούμε τη συνάρτηση lista
athroisma(lista)

# Εκτύπωση διαχωριστικό ....
print("...........")

# Για κάθε στοιχείο της λίστας
for item in lista:
  # Εκτύπωση το στιγμιαίο στοιχείο της λίστας
  print(item)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-09-example-04.py).

### 9.8.5 Παράδειγμα 5

---

```python
# Δημιουργία συνάρτησης showList
def showList(lista2):
  # Για όσο είναι το μήκος της λίστας
  for i in range(len(lista2)):
    # Πολλαπλασιάζουμε το στιγμιαίο στοιχείο της λίστας κατά 2
    lista2[i] = lista2[i] * 2


# Δημιουργία λίστας
lista = [1, 4, 3, 5, 6]

# Καλούμε τη συνάρτηση showList
showList(lista)

# Εκτύπωση λίστας
print(lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-09-example-05.py).

---
