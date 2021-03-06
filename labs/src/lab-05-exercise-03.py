# Αρχικοποίηση μεταβλητών
consonantsCounter = 0
vowelCounter = 0
otherCounter = 0
letter = 0
consonants = "bcdfgjklmnpqrstvwxz"
vowels = "aehyuio"

# Ζητάμε από το χρήστη να δώσει μια λέξη
word = input("Δώσε λέξη με λατινικούς χαρακτήρες: ").lower()

# Για κάθε γράμμα της λέξης
while letter < len(word):
    # Εάν το γράμμα είναι φωνήεν
    if word[letter] in vowels:
        # Κάθε φορά προσθέτουμε στη μεταβλητη vowelCounter 1
        vowelCounter += 1
    # Αλλιώς εάν το γράμμα είναι σύμφωνο
    elif word[letter] in consonants:
        # Κάθε φορά προσθέτουμε στη μεταβλητη consonantsCounter 1
        consonantsCounter += 1
    # Αλλιώς είναι κάποιο σύμβολο
    else:
        # Κάθε φορά προσθέτουμε στη μεταβλητη otherCounter 1
        otherCounter += 1
    # Αυξάνουμε την μεταβλητή letter κατά 1
    letter += 1

# Εκτύπωση αποτελεσμάτων
print("Τα φωνήεντα είναι %d." % vowelCounter)
print("Τα σύμφωνα είναι %d." % consonantsCounter)
print("Τα σύμβολα είναι %d." % otherCounter)
