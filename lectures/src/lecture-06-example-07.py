# Δημιουργία λίστας
lista = [8, 7, 8, 9, 3]

# Αρχικοποίηση μεταβλητής
counter = 0

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Για κάθε στοιχείο της λίστας
for k in lista:
    # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
    if k == key:
        # Αυξάνουμε τον counter κατά 1
        counter += 1

# Εκτύπωση το πόσες φορές εισήχθη το key
print("Ο αριθμός %d έχει εισαχθεί %d φορές." % (key, counter))
