[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Feffie375.github.io%2FTPTE-AEGEAN&count_bg=%23E3802B&title_bg=%2307359E&icon=internetarchive.svg&icon_color=%23E7E7E7&title=%CE%A0%CF%81%CE%BF%CE%B2%CE%BF%CE%BB%CE%AD%CF%82&edge_flat=false)](https://hits.seeyoufarm.com)

# 1 Εισαγωγή στην Python - Βασικές έννοιες

---

## Περιεχόμενα

---

- 1.1 Ιστορική Αναδρομή της Python
- 1.2 Η Python σήμερα
- 1.3 Τα βασικά χαρακτηριστικά της Python
- 1.4 Γιατί επιλέξαμε να μάθουμε Python
- 1.5 Μερικές από τις περιοχές εφαρμογών της Python
- 1.6 Περιβάλλον εργασίας

## 1.1 Ιστορική Αναδρομή της Python

---

Ξεκίνησε να αναπτύσσεται το Δεκέμβριο του 1989 από τον Guido van Rossum στο ερευνητικό κέντρο CWI (Centrum voor Wiskunde en Informatica) της Ολλανδίας. Η έκδοση 2.0 δημοσιεύτηκε στις 16 Οκτωβρίου 2000 και η έκδοση 3.0, η οποία δεν είναι, εν γένει, σύμφωνη (compatible) με τις προηγούμενες εκδόσεις, στις 3 Δεκεμβρίου 2008.

Το όνομα της γλώσσας προέρχεται από την τηλεοπτική σειρά του BBC `Monty Python's Flying Circus` (1969-74) της οποίας ο Guido van Rossum υπήρξε φανατικός οπαδός.

## 1.2 Η Python σήμερα

---

- Σύμφωνα με την εταιρία αξιολόγησης λογισμικού TIOBE είναι η 3η δημοφιλέστερη γλώσσα με 11.3% των προγραμμάτων να γράφονται σε αύτη.
- Λόγω της φύσης της είναι πιο παραγωγική από συνηθισμένες γλώσσες (C, Java, κτλ.).
- Χρησιμοποιείται σε ευρεία κλίμακα για επιστημονικές εφαρμογές, από αστροφυσική (Astropy) έως βιολογία (Biopy).

![Python](../images/top_companies_using_python.jpg)

## 1.3 Τα βασικά χαρακτηριστικά της Python

---

Η **Python** μπορεί να χρησιμοποιηθεί για πολλούς σκοπούς και σε διάφορες περιοχές ενδιαφέροντος. Έχει την δυνατότητα να τρέξει στις περισσότερες πλατφόρμες υλικού υπολογιστών και Λειτουργικών Συστημάτων (OS), όπως για παράδειγμα **Windows**, **Linux** και **Mac**. Διαθέτει πάρα πολλές βιβλιοθήκες που μπορούν να χρησιμοποιηθούν εύκολα και άμεσα. Μπορεί να δημιουργήσει και ένας προγραμματιστής δικές του βιβλιοθήκες, ώστε να τις χρησιμοποιεί κατάλληλα σε διαφορετικά προγράμματά του, αποφεύγοντας να γράφει, κάθε φορά, κώδικα από την αρχή. Τα προγράμματα σε **Python** είναι ευανάγνωστα και γράφονται γρηγορότερα σε σχέση με άλλες γλώσσες προγραμματισμού όπως οι C, C++ και Java.

Τα πιο βασικά χαρακτηριστικά της γλώσσας Python είναι:

- Χρησιμοποιεί διερμηνευτή (Interpreter). Το πρόγραμμα διερμηνεύεται και εκτελείται γραμμή-προς-γραμμή.
- Δεν υπάρχει δήλωση μεταβλητών και παραμέτρων.
- Είναι case-sensitive. Αυτό σημαίνει ότι η μεταβλητή name είναι διαφορετική από την Name. Όπως επίσης ότι η τιμή μιας Boolean μεταβλητής είναι True και όχι true.
- Είναι φτιαγμένη για να επεκτείνεται εύκολα. Για αυτό η βασική έκδοση της γλώσσας είναι ιδιαίτερα μικρή.
- Ως δυναμική γλώσσα είναι ιδιαίτερα αργή, αλλά επιτρέπει την εκτέλεση χρονοβόρων κομματιών σε C.
- Είναι Αντικειμενοστρεφής (object oriented). Τα πάντα στην Python είναι αντικείμενα (με ιδιότητες και μεθόδους).
- Τρέχει σχεδόν σε όλα τα λειτουργικά συστήματα.

## 1.4 Γιατί επιλέξαμε να μάθουμε Python

Η **Python** είναι μια εξαιρετικά αποδοτική γλώσσα. Αυτό σημαίνει ότι τα προγράμματα που θα γράψουμε στη συνέχεια θα μπορούν να κάνουν περισσότερα σε λιγότερες γραμμές κώδικα από άλλες γλώσσες προγραμματισμού.

Για παράδειγμα στη **Python** εαν θέλουμε να εμφανίσουμε στην οθόνη ένα κείμενο `Hello World!` θα γράψουμε:

```python
print("Hello World!")
```

Ενώ στη γλώσσα **C** θα πρέπει να γράψουμε:

```c
#include <stdio.h>

int main(){
    printf("Hello World!");
    return 0;
}
```

Η σύνταξη της **Python** μας βοηθάει να γράψουμε έναν "καθαρό" κώδικα. Ο κώδικας είναι σε πολύ μεγάλο βαθμό ευανάγνωστος, με εύκολη αποσφαλμάτωση και εύκολη επέκταση και ανάπτυξη σε σύγκριση με άλλες γλώσσες.

Έχουμε επιλέξει την **Python** για να μάθουμε προγραμματισμό διότι:

- έχει απλή σύνταξη - άμεσα κατανοητός κώδικας.
- είναι κατάλληλη για αρχάριους και για έμπειρους προγραμματιστές.
- είναι γλώσσα ανοικτού κώδικα (διαθέσιμη στη διεύθυνση [http://python.org](http://python.org)).
- είναι γενικής χρήσης, υψηλού επιπέδου γλώσσα προγραμματισμού.
- έχει σημαντικές δυνατότητες προς διάφορες κατευθύνσεις (ισχυρή γλώσσα προγραμματισμού).
- είναι αντικειμενοστραφής.
- έχει τεράστιο αριθμό από βιβλιοθήκες συναρτήσεων για κάθε χρήση NumPy, matplotlib, Tkinter, Pandas, PyGame ...

## 1.5 Μερικές από τις περιοχές εφαρμογών της Python

---

- Επιστημονικός προγραμματισμός / Αριθμητική ανάλυση (Scientific /Numeric Computing)
- Επιστήμη Δεδομένων και Μηχανική Μάθηση (Data Science & Machine Learning)
- Ανάπτυξη εφαρμογών Web (Web Application Development)
- Ανάπτυξη διεπαφής χρήστη-υπολογιστή (GUI Programming)
- Ανάπτυξη παιχνιδιών (Game programming)

## 1.6 Περιβάλλον εργασίας

---

Υπάρχουν πολλοί τρόποι για να εγγραφεί κανείς στο [Repl.it](repl.it). Καταρχάς μπορούμε να δημιουργήσουμε ένα λογαριασμό δίνοντας ένα username, ένα E-mail και ένα password. Έπειτα δηλώνουμε ότι ήμαστε εκπαιδευτικοί επιλέγοντας το πλαίσιο που λέει : “I’m a teacher” και τέλος πατάμε το κουμπί “Sign up”. Μπορούμε να εγγραφούμε και με έναν ήδη υπάρχων λογαριασμό από το Google (gmail), το Github ή το Facebook. Στη συνέχεια μας καλωσορίζει στην πλατφόρμα, όπου στην περίπτωση που έχουμε εγγραφεί με τον πρώτο τρόπο πρέπει να επικυρώσουμε τη διεύθυνση email πηγαίνοντας στο αντίστοιχο email που μας έχει σταλεί αυτόματα στη διεύθυνση που δώσαμε κατά την εγγραφή. Μετά την εγγραφή μας καλωσορίζει στην αρχική σελίδα του [Repl.it](repl.it).

Στο "Home" βρίσκουμε την αρχική σελίδα και αριστερά βλέπουμε ένα panel για την περιήγηση στη σελίδα. Στο "My Repls" μπορούμε να δούμε όλα τα προγράμματα που έχουμε δημιουργήσει και μπορούμε να οργανώσουμε καλύτερα τα προγράμματά μας σε φακέλους, σαν να ήμασταν στον υπολογιστή μας. Με το "new repl" μπορούμε να δημιουργήσουμε ένα καινούριο πρόγραμμα και με το "new folder" ένα νέο κενό φάκελο. Τέλος, μπορούμε να σβήσουμε ή να μετονομάσουμε ένα αρχείο ή ένα φάκελο πατώντας τις τρεις κάθετες τελείες που εμφανίζονται δεξιά από το όνομα του αρχείου ή του φακέλου (για να διαγραφεί ένας φάκελος μας λέει να γράψουμε το όνομα του φακέλου που θέλουμε να διαγράψουμε σαν δικλείδα ασφαλείας για να μη χάσουμε κάποιο αρχείο κατά λάθος).

![Repl.it](../images/Replit.PNG)

ΠΡΟΣΟΧΗ! Στις ρυθμίσεις στο πεδίο indent type πρέπει να είναι πάντα επιλεγμένο το `spaces` και ΌΧΙ το `tabs`.

---