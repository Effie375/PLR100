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
