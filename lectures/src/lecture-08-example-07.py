# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

# Για κάθε υπολίστα της λίστας
for ypolista in lista:
    # Έστω ότι το μέγιστο γραμμής είναι το στοιχείο της υπολίστας που βρίσκεται στη θέση 0
    megistoGrammhs = ypolista[0]
    # Για κάθε στοιχείο της υπολίστας
    for i in ypolista:
        # Εάν το μέγιστο γραμμής είναι μικρότερο από το στιγμιαίο στοιχείο της υπολίστας
        if megistoGrammhs < i:
            # Εκχωρούμε στο megistoGrammhs το i
            megistoGrammhs = i

    # Εκτύπωση το μέγιστο γραμμής
    print("Μέγιστο γραμμής: %d" % megistoGrammhs)
