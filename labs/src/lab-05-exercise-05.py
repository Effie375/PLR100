# Αρχικοποίηση μεταβλητών
megisto = 0
lista = []

# Ζητάμε από το χρήστη να δώσει έναν αριθμό
number = int(input("Δώσε αριθμό: "))

# Όσο ο αριθμός είναι διάφορος του μηδενός
while number != 0:
    # Αποθηκεύουμε τον αριθμό στη λίστα
    lista.append(number)
    # Εάν βρούμε αριθμό μεγαλύτερο απο αυτό που έχουμε μέχρι στιγμής
    if number > megisto:
        # Αποθηκεύουμε τον αριθμό σαν megisto
        megisto = number
    # Ζητάμε από το χρήστη να ξαναδώσει αριθμό
    number = int(input("Δώσε αριθμό: "))
    i = 1

# Όσο το i είναι μικρότερο ή ίσο του μέγιστου αριθμού
while i <= megisto:
    # Αρχικοποίηση μεταβλητών
    j = 0
    counter = 0
    # Όσο το j είναι μικρότερο του μήκους της λίστας
    while j < len(lista):
        # Εάν το στοιχείο της λίστας είναι ίσο με i
        if lista[j] == i:
            # Κάθε φορά αυξάνουμε το μετρητή κατά 1
            counter += 1
        # Αυξάνουμε την μεταβλητή j κατά 1
        j += 1
    # Εάν ο counter είναι 1
    if counter == 1:
        print("Ο αριθμός %d εισήχθη %d φορά." % (i, counter))
    # Αλλιώς εάν ο counter είναι διάφορος του μηδενός
    elif counter != 0:
        print("Ο αριθμός %d εισήχθη %d φορές." % (i, counter))
    # Αυξάνουμε την μεταβλητή i κατά 1
    i += 1
