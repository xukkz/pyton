import math
belopp = float(0)

totalsumma = float(input("Please enter the total sum of the purchase: "))
while (belopp < totalsumma) and (belopp <= 0):
    belopp = float(input("Please enter the amout you wish to pay with: "))

roundedSum = round(totalsumma)
tillbaka = (belopp - roundedSum)

print("KVITTO")
print("--------------------------")
print("Totalt           :   " + str(totalsumma) + "     kr")
print("Öresavrundning   :   " +
      str(round((roundedSum - totalsumma), 2)) + "     kr")
print("Att betala       :   " + str(roundedSum) + "     kr")
print("Kontant          :   " + str(belopp) + "     kr")
print("Tillbaka         :   " + str((belopp - roundedSum)) + "     kr")
print("--------------------------")

antal500 = 0
antal100 = 0
antal50 = 0
antal20 = 0
antal10 = 0
antal5 = 0
antal2 = 0
antal1 = 0

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


print("500 lappar : " + str(antal500))
print("100 lappar : " + str(antal100))
print("50 lappar  : " + str(antal50))
print("20 lappar  : " + str(antal20))
print("10 kronor  : " + str(antal10))
print("5 kronor   : " + str(antal5))
print("2 kronor   : " + str(antal2))
print("1 kronor   : " + str(antal1))
