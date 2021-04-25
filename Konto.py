class Account:
    def __init__(self, accountnumber, balance, dispo):
        self.accountnumber = accountnumber
        self.balance = balance
        self.dispo = dispo

    def print(self):
        print(self.balance)

    def deposit(self, x):
        self.balance = self.balance + x
        print("Der neuer Kontostand von " + str(self.accountnumber) + " beträgt: " + str(self.balance) + "€\n")

    def withdraw(self, x):
        if self.balance + self.dispo >= x:
            self.balance = self.balance - x
            print("Der neuer Kontostand von " + str(self.accountnumber) + " beträgt: " + str(self.balance) + "€\n")
            return True
        else:
            print("Das Konto ist nicht gedeckt, die Aktion konnte nicht augeführt werden.")
            return False

    def transaction(self, zielkonto, betrag):
        if self.withdraw(betrag) == True:
            zielkonto.deposit(betrag)


mein_Konto = Account("12345", 5000, 500)


mein_Zweitkonto = Account("67890", 500, 1500)


Konten = {
    "67890": mein_Zweitkonto,
    "12345": mein_Konto,

}


kunde = ""


def login():
    print("(Anmerkung: Kontonummern sind \"12345\" und \"67890\".)")
    kontonummer = input("Bitte geben Sie Ihre Kontonummer ein: ")
    while Konten.get(kontonummer) == None:
        print("Kontonummer ist ungültig.")
        kontonummer = input("Bitte versuchen Sie es erneut: ")
    return Konten.get(kontonummer)


def input_valid_account():
    print("(Anmerkung: Kontonummern sind \"12345\" und \"67890\".)")
    nummer = input()
    while Konten.get(nummer) == None:
        print("Kontonummer ungültig. Versuchen Sie es erneut.")
        nummer = input()

    return Konten.get(nummer)


def menue():
    global kunde
    print("\nBitte geben Sie für den gewünschten Menüpunkt die Zahl ein:")
    print("1. Betrag abbuchen")
    print("2. Betrag einzahlen")
    print("3. Betrag überweisen")
    print("4. Kontoinfo anzeigen")
    print("5. Konto wechseln")
    eingabe = input("Eingabe: ")
    if eingabe == "1":
        print("Geben Sie den abzubuchenden Betrag an:")
        betrag_abbuchen = input()
        try:
            betrag_abbuchen = float(betrag_abbuchen)
            if betrag_abbuchen <= 0:
                print("Der Betrag muss über 0 liegen. Sie werden zurück zum Menü geleitet.")
                menue()
            else:
                kunde.withdraw(betrag_abbuchen)
        except ValueError:
            print("Ihre Eingabe war ungültig. Sie werden zurück zum Menü geleitet.")
        menue()
    elif eingabe == "2":
        print("Geben Sie den einzuzahlenden Betrag an:")
        betrag_einzahlen = input()
        try:
            betrag_einzahlen = float(betrag_einzahlen)
            if betrag_einzahlen <= 0:
                print("Der Betrag muss über 0 liegen. Sie werden zurück zum Menü geleitet.")
                menue()
            else:
                kunde.deposit(betrag_einzahlen)
        except ValueError:
            print("Ihre Eingabe war ungültig. Sie werden zurück zum Menü geleitet.")
        menue()
    elif eingabe == "3":
        print("Geben sie den zu überweisenden Betrag ein:")
        betrag_ueberweisen = input()
        try:
            betrag_ueberweisen = float(betrag_ueberweisen)
            if betrag_ueberweisen <= 0:
                print("Der Betrag muss über 0 liegen. Sie werden zurück zum Menü geleitet.")
                menue()
        except ValueError:
            print("Ihre Eingabe war ungültig. Sie werden zurück zum Menü geleitet.")
            menue()
        print("Geben Sie das Zielkonto ein:")
        zielkonto = input_valid_account()
        kunde.transaction(zielkonto, betrag_ueberweisen)
        menue()
    elif eingabe == "4":
        print("\nKontonummer: " + str(kunde.accountnumber))
        print("Kontostand: " + str(kunde.balance) + "€")
        print("Dispo: " + str(kunde.dispo) + "€\n")
        menue()
    elif eingabe == "5":
        kunde = login()
        menue()
    else:
        print("Ihre Eingabe ist ungültig. Bitte versuchen Sie es erneut.")
        menue()


kunde = login()
menue()
