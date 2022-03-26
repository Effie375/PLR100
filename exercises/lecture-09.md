[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Feffie375.github.io%2FTPTE-AEGEAN&count_bg=%23E3802B&title_bg=%2307359E&icon=internetarchive.svg&icon_color=%23E7E7E7&title=%CE%A0%CF%81%CE%BF%CE%B2%CE%BF%CE%BB%CE%AD%CF%82&edge_flat=false)](https://hits.seeyoufarm.com)

# 9.1 Ασκήσεις

---

Εδώ θα βρείτε ένα σύνολο με ασκήσεις που βασίζονται στην ύλη του κεφαλαίου και αναδεικνύουν τις ιδιαιτερότητες του. Οι λύσεις των ασκήσεων βρίσκονται ακριβώς κάτω από κάθε εκφωνήση.

## 9.1.1 Άσκηση 1

---

Αρχικά ζητάμε από το χρήστη να δώσει αριθμό για διαίρεση με το 5. Στη συνέχεια καλούμε τη συνάρτηση `foo` και παίρνει σαν παράμετρο τον αριθμό που δήλωσε ο χρήστης προηγουμένος. Τέλος εμφανίζουμε το αποτέλεσμα της διάιρεσης της παραμέτρου με το 5 στην οθόνη του χρήστη.

```python
# Δημιουργία συνάρτησης foo
def foo(x):
  # Επιστρέφει τη διάιρεση της παραμέτρου με το 5
  return x / 5


# Ζητάμε από το χρήστη να δώσει αριθμό για διαίρεση με το 5
x = int(input("Δώσε αριθμό για διαίρεση με το 5: "))

# Καλούμε τη συνάρτηση foo και εκτύπωνουμε
print(foo(x))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-09-exercise-01.py).

## 9.1.2 Άσκηση 2

---

Τι θα εµφανιστεί αν δώσουµε ως τιµή εισόδου στο πρόγραµµα την τιµή 5 και τι την τιµή 10.

```python
def apot(x):
  return x % 2


def foo(n):
  apot1 = n * 2
  n = apot1 * 2
  return n, apot1


a = int(input("Δώσε αριθμό: "))

if apot(a) == 0:
  a, n = foo(a)
  print(a, n)
else:
  print(apot(a))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-09-exercise-02.py).

## 9.1.3 Άσκηση 3

---

Να γραφεί µια συνάρτηση η οποία θα δέχεται µια λίστα µε αριθµούς και θα την ταξινοµεί.

```python
# Δημιουργία συνάρτησης sort
def sort(pList):
  """ Αυτή η συνάρτηση ταξινομεί τη λίστα κατά αύξουσα σειρά."""
  for i in range(1, len(pList)):
    for j in range(len(pList) - 1, i - 1, -1):
      if pList[j - 1] > pList[j]:
        # Swap pList
        temp = pList[j - 1]
        pList[j - 1] = pList[j]
        pList[j] = temp
  # Επιστρέφει τη pList
  return pList


# Δημιουργία λίστας
lista = [1, 6, 2, 5, 3, 7, 4]

# Καλούμε τη συνάρτηση sort και εκτύπωνουμε
print(sort(lista[:]))
```

Για να δείτε τη **ΛΥΣΗ** πατήστε [εδώ](src/lecture-09-exercise-03.py).

## 9.1.4 Άσκηση 4

---

Ένας μεταπτυχιακός φοιτητής για να μπορέσει να πάρει πτυχίο πρέπει να περάσει συγκεκριμένο αριθμό μαθημάτων ανάλογα με το Τμήμα που φοιτά. Στο παρακάτω πρόγραμμα ένας φοιτητής δίνει τον αριθμό των μαθημάτων που χρειάζεται για να πάρει πτυχίο και στη συνέχεια καταχωρεί τη βαθμολογία των μαθημάτων σε μία λίστα με τη χρήση συνάρτησης. Το πρόγραμμα με τη χρήση συνάρτησης υπολογίζει το μέσο όρο. Ο μέσος όρος εμφανίζεται στην οθόνη και έπειτα χρησιμοποιώντας εκ νέου μία συνάρτηση εμφανίζει αν ο φοιτητής πέρασε ή κόπηκε. Βρείτε όλα τα λάθη (συντακτικά ή λογικά) που υπάρχουν στον παρακάτω κώδικα.

```python
def readNums(x):
lista = []
for numbers in range():
arithmos = float(input("Δώσε αριθμό: "))
lista.append(arithmos)
return list

def mesosOros(y):
athroisma = 0
for stoixeio in x:
athroisma = stoixeio
mo = athroisma / len(x)
return mo

def vathmologia(a):
if a >= 5:
print("Πέρασες")
else
print("Κόπηκες")


stoixeio = int(input("Δώσε στοιχεία που περιέχει η λίστα: ")
numbers = readNums()
mesosoros = mesosOros(numbers)
print("Ο μέσος όρος είναι", mesooros)
vatmologia(mesosoros)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-09-exercise-04.py).
