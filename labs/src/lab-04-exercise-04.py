# Διαβάζουμε από το χρήστη έναν αριθμό
num = int(input("Γράψε έναν ακέραιο αριθμό: "))

# Όσο ο αριθμός είναι διάφορος του 0
while(num != 0):
    # Εκτύπωσε το διπλάσιο του
    print(2 * num)
    # Ξαναζήτα απο το χρήστη για αριθμό
    num = int(input("Γράψε έναν ακέραιο αριθμό: "))

print("Τέλος")
