# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

# Αρχικοποίηση μεταβλητής
athroisma = 0

# Για κάθε υπολίστα της λίστας
for ypolista in lista:
    # Για κάθε στοιχείο της υπολίστας
    for i in ypolista:
        # Αυξάνουμε το άθροισμα κατά i
        athroisma += i

# Εκτύπωση του αθροίσματος
print(athroisma)
