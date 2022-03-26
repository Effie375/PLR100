# Αρχικοποίηση μεταβλητής
alfabito = "abcdefghijklmnopqrstuvwxyz"

# Ζητάμε από το χρήστη να δώσει μια λέξη
leksi = input("Δώσε λέξη με λατινικούς χαρακτήρες: ").lower()

# Για κάθε γράμμα του λατινικού αλφαβήτου
for gramma in alfabito:
    # Αρχικοποιήση του μετρητή
    counter = 0
    # Για κάθε γράμμα της λέξης
    for grammaLeksis in leksi:
        # Εάν το γράμμα της λέξης είναι ίσο με το στιγμιαίο γράμμα
        if grammaLeksis == gramma:
            # Αυξάνουμε το μετρητή κατά 1
            counter += 1
    # Εάν ο μετρητής είναι 1
    if counter == 1:
        print("To γράμμα '%s' εμφανίστηκε %d φορά." % (gramma, counter))
    # Αλλιώς εάν ο μετρητής δεν είναι ούτε 0 αλλά ούτε 1
    elif counter != 0:
        print("To γράμμα '%s' εμφανίστηκε %d φορές." % (gramma, counter))
