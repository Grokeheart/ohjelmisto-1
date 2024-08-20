leiviskat = input("Anna leiviskät: ")
naulat = input("Anna naulat: ")
luodit = input("Anna luodit: ")

leiviskat = float(leiviskat)
naulat = float(naulat)
luodit = float(luodit)

luodit_total = luodit * 13.3
naulat_total = naulat * (32 * 13.3)
leiviskat_total = leiviskat * (20 * 32 * 13.3)

yht = luodit_total + naulat_total + leiviskat_total

kilot = yht // 1000
grammat = yht % 1000

print("Massa nykymittojen mukaan: ")
print(f"{kilot} kilogrammaa ja {grammat:.2f} grammaa.")