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
    # Αυξάνουμε τη thesi κατά 1
    thesi += 1
