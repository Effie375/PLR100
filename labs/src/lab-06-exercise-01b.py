# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 7
athroisma = 0

for i in range(5, 36, 5):
    # Διαβάζουμε από το χρήστη το βαθμό του και το μετατρεπουμε σε ακέραιο
    vathmos = int(input("Δώσε βαθμολογία για αγώνισμα: "))
    athroisma = athroisma + i * vathmos

# Υπολογισμός του μέσου όρου
mo = athroisma / MAX_ELEMENTS

# Εκτύπωση μέσου όρου
print("Ο μέσος όρος είναι %.1f." % mo)
