# Ζητάμε από το χρήστη να δώσει κύκλους και το μετατρεπουμε σε ακέραιο
seasons = int(input("Δώσε κύκλους: "))
# Ζητάμε από το χρήστη να δώσει κύκλους ανα επεισόδια και το μετατρεπουμε σε ακέραιο
episodes = int(input("Δώσε επεισόδια άνα κύκλο: "))

# Δημιουργία κενής λίστας
thle8eash = []

# Για κάθε seasons
for i in range(seasons):
    # Δημιουργία κενής λίστας
    thlSeason = []
    # Για κάθε episodes
    for j in range(episodes):
        # Ζητάμε από το χρήστη να δώσει τηλεθέαση και το μετατρεπουμε σε πραγματικό
        thl = float(input("Δώσε τηλεθέαση %dx%d: " % ((i + 1), (j + 1))))
        # Αποθηκεύουμε την τηλεθέαση στην υπολίστα thlSeason
        thlSeason.append(thl)
    # Αποθηκεύουμε στη λίστα thle8eash την υπολίστα thlSeason
    thle8eash.append(thlSeason)

# Έστω ότι το max και το min τηλεθέασης των season και επεισοδίων είναι η θέση 0
maxThlSeason = 0
maxThlEpi = 0
minThlSeason = 0
minThlEpi = 0

# Έστω ότι ο max μέσος όρος είναι 0
maxMO = 0

# Για κάθε seasons
for i in range(seasons):
    # Αρχικοποίηση μεταβλητής
    soumaSeason = 0
    # Για κάθε episodes
    for j in range(episodes):
        if thle8eash[i][j] > thle8eash[maxThlSeason][maxThlEpi]:
            maxThlSeason = i
            maxThlEpi = j
        if thle8eash[i][j] < thle8eash[minThlSeason][minThlEpi]:
            minThlSeason = i
            minThlEpi = j
        soumaSeason += thle8eash[i][j]

    if maxMO < soumaSeason:
        maxMO = soumaSeason
        maxMOSeason = i

# Εκτύπωση επεισοδίων με μέγιστη τηλεθέαση
print("Eπεισόδιο με μέγιστη τηλεθέαση: %dx%d" % ((maxThlSeason + 1), (maxThlEpi + 1)))
# Εκτύπωση επεισοδίων με ελάχιστη τηλεθέαση
print("Eπεισόδιο με ελάχιστη τηλεθέαση: %dx%d" % ((minThlSeason + 1), (minThlEpi + 1)))
# Εκτύπωση σεζόν με μεγαλύτερο μέσο όρο τηλεθέασης
print("Σεζόν με μεγαλύτερο μέσο όρο τηλεθέασης: %d" % (maxMOSeason + 1))
