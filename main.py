import math

# Skapar alla variabler som kommar att användas under programmets gång
belopp = float(0)
totalsumma = float(0)
antal500 = 0
antal100 = 0
antal50 = 0
antal20 = 0
antal10 = 0
antal5 = 0
antal2 = 0
antal1 = 0

# Kollar så att användaren måste ange ett giltigt tal
while (totalsumma <= 0):
    totalsumma = float(input("Please enter the total sum of the purchase: "))

while (belopp < totalsumma) and (belopp <= 0):
    belopp = float(input("Please enter the amout you wish to pay with: "))

# Avrundar köpsumman till ett jämt värde och räknar ut hur mycket användaren ska ha tillbaka
roundedSum = round(totalsumma)
tillbaka = (belopp - roundedSum)

# Kollar om beloppen är giltiga och om inte så ger vi ett felmeddelande och avslutar programmet
if totalsumma < 0:
    print("Totalsumman kan inte vara mindre än 0... ")
    print("Tryck 'ENTER' för att stänga ner programmet... ")
    input()
    quit()
if roundedSum > belopp:
    print("Summan kan inte vara större än beloppet...")
    print("Tryck 'ENTER' för att stänga ner programmet... ")
    input()
    quit()

# Printa ut kvittot med erhållet belopp samt totalsumman
print("\nKVITTO")
print("--------------------------------------------------------------")
print("Totalt           :   " + str(totalsumma), end="\t kr")
print()
print("Öresavrundning   :   " +
      str(round((roundedSum - totalsumma), 2)), end="\t kr")
print()
print("Att betala       :   " + str(roundedSum), end="\t\t kr")
print()
print("Kontant          :   " + str(belopp), end="\t kr")
print()
print("Tillbaka         :   " + str((belopp - roundedSum)), end="\t kr")
print()
print("--------------------------------------------------------------")

# Kolla hur många av alla sedlar som ska ges tillbaka
while tillbaka > 0:
    if tillbaka >= 500:
        antal500 = math.floor((tillbaka // 500))
        tillbaka = tillbaka - (antal500 * 500)
    if tillbaka >= 100:
        antal100 = math.floor((tillbaka // 100))
        tillbaka = tillbaka - (antal100 * 100)
    if tillbaka >= 50:
        antal50 = math.floor((tillbaka // 50))
        tillbaka = tillbaka - (antal50 * 50)
    if tillbaka >= 20:
        antal20 = math.floor((tillbaka // 20))
        tillbaka = tillbaka - (antal20 * 20)
    if tillbaka >= 10:
        antal10 = math.floor((tillbaka // 10))
        tillbaka = tillbaka - (antal10 * 10)
    if tillbaka >= 5:
        antal5 = math.floor((tillbaka // 5))
        tillbaka = tillbaka - (antal5 * 5)
    if tillbaka >= 2:
        antal2 = math.floor((tillbaka // 2))
        tillbaka = tillbaka - (antal2 * 2)
    if tillbaka >= 1:
        antal1 = math.floor((tillbaka // 1))
        tillbaka = tillbaka - (antal1 * 1)

# Printa ut hur många av varje sedel som användaren får tillbaka
print("500 lappar : " + str(antal500))
print("100 lappar : " + str(antal100))
print("50 lappar  : " + str(antal50))
print("20 lappar  : " + str(antal20))
print("10 kronor  : " + str(antal10))
print("5 kronor   : " + str(antal5))
print("2 kronor   : " + str(antal2))
print("1 kronor   : " + str(antal1))

input()
