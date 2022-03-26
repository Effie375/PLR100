[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Feffie375.github.io%2FTPTE-AEGEAN&count_bg=%23E3802B&title_bg=%2307359E&icon=internetarchive.svg&icon_color=%23E7E7E7&title=%CE%A0%CF%81%CE%BF%CE%B2%CE%BF%CE%BB%CE%AD%CF%82&edge_flat=false)](https://hits.seeyoufarm.com)

# 7 Αναζήτηση και ταξινόμηση μονοδιάστατων λιστών

---

## Περιεχόμενα

---

- 7.1 Αναζήτηση στοιχείων I
- 7.2 Αναζήτηση στοιχείων II
- 7.3 Αναζήτηση στοιχείων III
- 7.4 Ταξινόμηση - Bubble Sort
- 7.5 Ταξινόμηση - Διπλή αντιμετάθεση
- 7.6 Διπλή ταξινόμηση

## 7.1 Αναζήτηση στοιχείων I

---

**1ος τρόπος:**

```python
# Δημιουργία λίστας
lista = [9, 7, 8, 9, 3]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητής
thesi = 0

# Για κάθε στοιχείο της λίστας
for i in lista:
  # Εάν το στιγμιαίο στοιχείο είναι ίσο με το key
  if i == key:
    # Εκτύπωση σε ποια θέση βρίσκεται το key
    print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
  # Αυξάνουμε τη thesi κατα 1
  thesi += 1
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-07-example-01a.py).

**2ος τρόπος:**

```python
# Δημιουργία λίστας
lista = [9, 7, 8, 9, 3]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητής
k = 0

# Για κάθε στοιχείο της λίστας
for i in lista:
  # Εάν το στιγμιαίο στοιχείο είναι ίσο με το key
  if i == key:
    # Αυξάνουμε το k κατά 1
    k += 1

# Εκτύπωση το πόσες φορές εισήχθη ο αριθμός
print("Το %d έχει εισαχθεί %d φορές." % (key, k))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-07-example-01b.py).

## 7.2 Αναζήτηση στοιχείων II

---

```python
# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
found = False
i = 0

# Για όσο το i είναι μικρότερο του 5 και ταυτόχρονα το found είναι ίσο με False
while (i < 5) and (found == False):
  # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
  if lista[i] == key:
    # Εκχωρούμε στη thesi το i
    thesi = i
    # Το found γίνεται True
    found = True
  # Αλλιώς σε οποιαδήποτε άλλη περίπτωση
  else:
    i += 1

# Εάν το found είναι ίσο με True
if found == True:
  # Εκτύπωση τη θέση που βρίσκεται το key
  print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
# Αλλιώς σε οποιαδήποτε άλλη περίπτωση
else:
  # Εκτύπωση ότι το key δε βρίσκεται στη λίστα
  print("Το %d δε βρίσκεται στη λίστα %d." % (key, thesi))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-07-example-02.py).

## 7.3 Αναζήτηση στοιχείων III

---

```python
# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
found = False
i = 0

# Για όσο το i είναι μικρότερο του 5 και ταυτόχρονα το found είναι ίσο με False
while (i < 5) and (found == False):
  # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
  if lista[i] == key:
    # Εκχωρούμε στη thesi το i
    thesi = i
    # Το found γίνεται True
    found = True
  # Αυξάνουμε το i κατά 1
  i += 1

# Εάν το found είναι ίσο με True
if found == True:
  # Εκτύπωση τη θέση που βρίσκεται το key
  print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
# Αλλιώς σε οποιαδήποτε άλλη περίπτωση
else:
  # Εκτύπωση ότι το key δε βρίσκεται στη λίστα
  print("Το %d δε βρίσκεται στη λίστα %s." % (key, lista))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-07-example-03.py).

## 7.4 Ταξινόμηση - Bubble Sort

---

```python
# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

# Εκτύπωση της λίστας πριν την ταξινόμηση
print("Η λίστα μας πριν την ταξινόμηση είναι: %s" % lista)

for i in range(len(lista)):
  for j in range(len(lista) - 1, i, -1):
    if lista[j - 1] > lista[j]:
      # Swap lista
      temp = lista[j - 1]
      lista[j - 1] = lista[j]
      lista[j] = temp

# Εκτύπωση της λίστας πριν την ταξινόμηση
print("Η λίστα μας μετά την ταξινόμηση είναι: %s" % lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-07-example-04.py).

## 7.5 Ταξινόμηση - Διπλή αντιμετάθεση

---

```python
# Δημιουργία λιστών
names = ["Γεωργίου", "Πέτρου", "Παπαδόπουλος", "Αθανασίου", "Τσακογιάννης"]
grades = [1, 2, 5, 7, 9]

for i in range(1, 5):
  for j in range(4, i - 1, -1):
    if grades[j - 1] > grades[j]:
      # Swap grades
      temp = grades[j - 1]
      grades[j - 1] = grades[j]
      grades[j] = temp
      # Swap names
      temp2 = names[j - 1]
      names[j - 1] = names[j]
      names[j] = temp2

# Εκτύπωση της ταξινομημένης λίστας names
print(names)
# Εκτύπωση της ταξινομημένης λίστας grades
print(grades)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-07-example-05.py).

## 7.6 Διπλή ταξινόμηση

---

```python
# Δημιουργία λιστών
names = ["Γεωργίου", "Πέτρου", "Παπαδόπουλος", "Αθανασίου", "Τσακογιάννης"]
grades = [1, 2, 5, 7, 9]

for i in range(1, 5):
  for j in range(4, i - 1, -1):
    if grades[j - 1] > grades[j]:
      # Swap grades
      temp = grades[j - 1]
      grades[j - 1] = grades[j]
      grades[j] = temp
      # Swap names
      temp2 = names[j - 1]
      names[j - 1] = names[j]
      names[j] = temp2
    if grades[j - 1] == grades[j]:
      if names[j - 1] > names[j]:
        # Swap names
        temp3 = names[j - 1]
        names[j - 1] = names[j]
        names[j] = temp3

# Εκτύπωση της ταξινομημένης λίστας names
print(names)
# Εκτύπωση της ταξινομημένης λίστας grades
print(grades)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lecture-07-example-06.py).
