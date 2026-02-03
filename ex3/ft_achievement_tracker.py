alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
           'perfectionist'}
print("=== Achievement Tracker System ===")
print()
print("Player alice achievements", alice)
print("Player bob achievements", bob)
print("Player charlie achievements", charlie)
print()
print("=== Achievement Analytics ===")
"""
UNION : Combine tous les éléments (sans doublons)
    Méthode : A.union(B)
INTERSECTION : Garde seulement les éléments communs
    Méthode : A.intersection(B)
DIFFERENCE : Retire les éléments du second ensemble
    Méthode : A.difference(B)
"""
result = alice.intersection(bob)
res = alice.union(charlie)
res2 = bob.difference(charlie)
res = res.union(res2)
result = result.union(res)
result = set(result)
print("All unique achievements:", result)
print("Total unique achievements: ", len(result))

print()
res = alice.intersection(bob)
res = res.intersection(charlie)
print("Common to all players: ", res)

res = bob.union(charlie)
res = res.difference(alice)
res2 = res.intersection(bob)
res2 = res2.intersection(charlie)
res = res.difference(res2)
print("Rare achievements (1 player):", res)
print()
print("Alice vs Bob common: ", alice.intersection(bob))
print("Alice unique: ", alice.difference(bob))
print("Bob unique: ", bob.difference(alice))
