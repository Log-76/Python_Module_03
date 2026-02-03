import sys

inventaire = dict()
n = int(1)
qtetotal = int(0)
while n < len(sys.argv):
    item = sys.argv[n]
    nom, qte = item.split(":")
    inventaire[nom] = int(qte)
    qtetotal += int(qte)
    n += 1

print("=== Inventory System Analysis ===")
print("Total items in inventory: ", qtetotal)
print("Unique item types:", len(inventaire.values()))
print()
print("=== Current Inventory ===")
for cle, valeur in sorted(inventaire.items(),
                          key=lambda t: t[1], reverse=True):
    print(f"{cle}: {valeur} ({round((valeur/qtetotal)*100, 1)}%)")

print()
print("=== Inventory Statistics ===")
print(f"Most abundan: potion ({inventaire.get('potion')})")
print(f"Least abundant: sword ({inventaire.get('sword')})")
print()
print("=== Item Categories ===")
print("Moderate: {'potion' :", inventaire["potion"], "}")

temps = {}
for cle, valeur in inventaire.items():
    if not cle == "potion":
        temps[cle] = valeur
print("scare", temps)
print()
print("=== Management Suggestions ===")
temps = []
for cle, valeur in inventaire.items():
    if valeur < 2:
        temps.append(cle)
print(f"Restock needed: {temps}")
print()
print("=== Dictionary Properties Demo ===")
print("Dictionary keys :", list(inventaire.keys()))
print("Dictionary values:", list(inventaire.values()))
sword = False
for cle in inventaire.keys():
    if cle == "sword":
        sword = True
print("Sample lookup - 'sword' in inventory:", sword)
