# 3.2 Debugging

## Άσκηση 1

Το παρακάτω πρόγραμμα διαβάζει δύο τυχαίους αριθμούς από το χρήστη και τους διαιρεί. Το πρόγραμμα εμφανίζει ο αποτέλεσμα της διαίρεσης στην οθόνη και στη συνέχεια ζητάει από το χρήστη να πληκτρολογήσει έναν ακόμη τυχαίο αριθμό. Ο τρίτος τυχαίος αριθμός πολλαπλασιάζεται με το αποτέλεσμα της διαίρεσης και το αποτέλεσμα της νέας πράξης εμφανίζεται στην οθόνη.

```python
# Program to divide two numbers and
# multiply the result with a new number

# Read two numbers
number1 = input(First number: )
number2 = input("Second number: '
# Convert numbers to floats
number1 = float(number)
# Divide two numbers
division = number1 // number

# Display the division
# will print value in float
print("The division of " number1, " and ", number2 " is ":, division
)
# Read third number
number3 = input('\nThird number ')
# Convert number to integer
number = int(number3)
# Multiply two numbers
result = int(number3 * number)
# Display the multiplication
print('The multiplication of", number3 "and" division "is' result)
#print('The multiplication of %2d and %5.2f is %2d" % (number3, division, result))
```

Ο κώδικας περιλαμβάνει λάθη τα οποία πρέπει να εντοπιστούνε έτσι ώστε το πρόγραμμα να είναι πλήρως λειτουργικό. Η διαδικασία για την εύρεση λαθών σε κώδικα ονομάζεται αποσφαλμάτωση ή εκσφαλμάτωση (στα αγγλικά καλείται debugging).

```python
# Program to divide two numbers and
# multiply the result with a new number

# Read two numbers
number1 = input("First number: ")
number2 = input("Second number: ")
# Convert numbers to floats
number1 = float(number1)
number2 = float(number2)
# Divide two numbers
division = number1 / number2

# Display the division
# will print value in float
print("The division of ", number1, " and ", number2, " is :", division)
# Read third number
number3 = input('\nThird number: ')
# Convert number to integer
number3 = int(number3)
# Multiply two numbers
result = int(number3 * division)
# Display the multiplication
print("The multiplication of", number3, "and", division, "is", result)
#print("The multiplication of %2d and %5.2f is %.2d" % (number3, division, result))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-03b-exercise-01.py).

## Άσκηση 2

Να γραφεί πρόγραμμα όπου να ρωτάει το χρήστη το όνομα του και να το εκτυπώνει μετά από το "Χάρηκα που σε γνώρισα". Στη συνέχεια θα ζητάει την ηλικία του χρήστη και θα υπολογίζει την ηλικία για το επόμενο έτος, την οποία θα εκτυπώνει. Τέλος θα υπολογίζει πόσα χρόνια χρειάζεται ακόμη για να φτάσει τα 100 και θα τα εμφανίζει με ένα μήνυμα "Θέλεις ακόμη Χ έτη για να φτάσεις τα 100".

```python
name = input("Δώσε το όνομα σου: ")
print("Χάρηκα που σε γνώρισα", name)
age = int(input("Πόσο χρονών είσαι: "))
print("Τον επόμενο χρόνο θα είσαι %d." %(age + 1))
print("Θέλεις ακόμη %d έτη για να φτάσεις τα 100." %(100 - age))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](src/lab-03b-exercise-02.py).
