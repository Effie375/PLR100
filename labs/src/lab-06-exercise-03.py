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
