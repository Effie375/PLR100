# Αρχικοποίηση μεταβλητών
sum = num = 0
key = 55555

# Για όσο ο αριθμός είναι διάφορος από το 55555
while num != key:
    # Αύξανουμε κάθε φορά το sum όσο είναι το num
    sum += num
    # Ζητάμε από το χρήστη να δώσει αριθμό και το μετατρέπουμε σε ακέραιο
    num = int(input("Δώσε έναν αριθμό: "))


# Εκτύπωση του αθροίσματος
print("Το άθροισμα είναι %d" % sum)
