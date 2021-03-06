# Διαβάζουμε από το χρήστη τους πόντους της 1ης ομάδας
omada1 = input("Δώσε τους τελικούς πόντους της ομάδας 1: ")
# Διαβάζουμε από το χρήστη τους πόντους της 2ης ομάδας
omada2 = input("Δώσε τους τελικούς πόντους της ομάδας 2: ")

# Ελέγχουμε αν είναι αριθμός
if not(omada1.isdigit() and omada2.isdigit()):
    # Ζητάμε για τελευταία φορά να διαβάσουμε αριθμό για την 1η ομάδα
    omada1 = input("Δώσε σωστά τους πόντους της ομάδας 1: ")
    # Ζητάμε για τελευταία φορά να διαβάσουμε αριθμό για την 2η ομάδα
    omada2 = input("Δώσε σωστά τους πόντους της ομάδας 2: ")

# Αφού ξέρουμε ότι είναι αριθμός το μετατρέπουμε σε ακέραια τιμή
omada1 = int(omada1)
omada2 = int(omada2)

# Ελέγχουμε αν η ομάδα 1 συγκέντρωσε 25 βαθμούς
if omada1 == 25:
    print("Η ομάδα 1 κέρδισε!")
else:
    print("Η ομάδα 2 κέρδισε!")
