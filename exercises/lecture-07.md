# 7.1 Ασκήσεις

---

Εδώ θα βρείτε ένα σύνολο με ασκήσεις που βασίζονται στην ύλη του κεφαλαίου και αναδεικνύουν τις ιδιαιτερότητες του. Οι λύσεις των ασκήσεων βρίσκονται ακριβώς κάτω από κάθε εκφωνήση.

## 7.1.1 Άσκηση 1

---

Να γραφεί πρόγραµµα που να διαβάζει 100 ακεραίους αριθµούς και να εµφανίζει τον µέγιστο και τον ελάχιστο µε χρήση ταξινόµησης.

```python
# Δημιουργία συνάρτησης sortFunction
def sortFunction(pList):
  try:
    for index in range(len(pList) - 1):
      for j in range(len(pList) - 1, index, -1):
        if pList[j - 1] > pList[j]:
          # Swap pList
          temp = pList[j - 1]
          pList[j - 1] = pList[j]
          pList[j] = temp
  except:
    # Εκτύπωση κάτι πήγε στραβά
    print("Κάτι πήγε στραβά!")
    # Επιστρέφει 1
    return 1
  else:
    # Επιστρέφει 0
    return 0


# Αρχικοποίηση μεταβλητών
MAX_NUMBERS = 100
lista = []

# Για MAX_NUMBERS
for i in range(MAX_NUMBERS):
  # Ζητάμε από το χρήστη να δώσει αριθμό
  num = input("Δώσε αριθμό: ")
  # Έλεγχος ορθότητας
  while not num.isdigit():
    # Ξανά ζητάμε από το χρήστη να δώσει αριθμό
    num = input("Είπα δώσε αριθμό: ")
  # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
  num = int(num)
  # Αποθηκεύουμε τον αριθμό στη λίστα
  lista.append(num)

if not sortFunction(lista):
  # Εκτύπωση του μεγαλύτερου αριθμού της λίστας
  print("\nΟ μεγαλύτερος αριθμός είναι το %d." % (lista[len(lista) - 1]))
  # Εκτύπωση του μικρότερου αριθμού της λίστας
  print("Ο μικρότερος αριθμός είναι το %d." % lista[0])
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-07-exercise-01.py).

## 7.1.2 Άσκηση 2

---

Ένα σχολείο έχει 200 µαθητές στην Γ’ τάξη λυκείου. Να γίνει πρόγραµµα το οποίο θα διαβάζει τα ονόµατα και τους βαθµούς απολυτηρίου των µαθητών και θα εµφανίζει τα ονόµατα των τριών καλύτερων µαθητών.

```python
# Δημιουργία συνάρτησης sortFunction
def sortFunction(pNames, pVathmoi):
  try:
    for i in range(len(pVathmoi) - 1):
      for j in range(len(pVathmoi) - 1, i, -1):
        if pVathmoi[j - 1] < pVathmoi[j]:
          # Swap pVathmoi
          temp1 = pVathmoi[j - 1]
          pVathmoi[j - 1] = pVathmoi[j]
          pVathmoi[j] = temp1
          # Swap pNames
          temp2 = pNames[j - 1]
          pNames[j - 1] = pNames[j]
          pNames[j] = temp2
  except:
    # Eκτύπωση κάτι πήγε στραβά
    print("Κάτι πήγε στραβά!")
    # Επιστρέφει 1
    return 1
  else:
    # Επιστρέφει 0
    return 0


# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 200
BEST_FOITITES = 3
counter = 0
vathmoi = []
names = []

# Για όσο ο counter είναι μικρότερος από το MAX_ELEMENTS
while counter < MAX_ELEMENTS:
  # Ζητάμε από το φοιτητή να δώσει το όνομά του
  name = input("Δώσε όνομα μαθητή: ")
  # Ζητάμε από το φοιτητή να δώσει το βαθμό του
  vathmos = input("Δώσε βαθμό: ")
  # Έλεγχος ορθότητας
  while not vathmos.isdigit():
    # Ξανά ζητάμε από το φοιτητή να δώσει το βαθμό του:
    vathmos = input("Είπα δώσε βαθμό: ")
  # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
  vathmos = int(vathmos)
  # Αποθηκεύουμε το όνομα στη λίστα names
  names.append(name)
  # Αποθηκεύουμε το βαθμό στη λίστα vathmoi
  vathmoi.append(vathmos)
  # Αυξάνουμε τον counter κατά 1
  counter += 1


if not sortFunction(names, vathmoi):
  try:
    # Για BEST_FOITITES
    for i in range(BEST_FOITITES):
      # Εκτύπωση του καλύτερου φοιτητή
      print("Ο %dος καλύτερος είναι ο/η %s." % ((i + 1), names[i]))
  except:
    # Εκτύπωση δεν υπάρχει άλλος φοιτητής στη λίστα
    print("Δεν υπάρχει άλλος φοιτητής στη λίστα!")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-07-exercise-02.py).
