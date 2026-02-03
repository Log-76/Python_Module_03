import sys
import math

print("=== Game Coordinate System ===")
if len(sys.argv) == 1:
    print("No scores provided. Usage: "
          "python3 ft_score_analytics.py <score1> <score2> ...")
coord2 = [10, 20, 5]
cordTuple2 = tuple(coord2)
# coordonne de base
cord = [0, 0, 0]
cordTuple = tuple(cord)
# calcul de distance
distance = math.sqrt((cordTuple2[0]-cordTuple[0])**2 +
                     (cordTuple2[1]-cordTuple[1])**2 +
                     (cordTuple2[2]-cordTuple[2])**2)
distance = float(distance)
print("Position created:", cordTuple2)
print(f"Distance betwen:{cordTuple} and {cordTuple2} : {distance}")
print()

# coordone entre par l utilisateur
nombres = sys.argv[1].split(" ")
cord2 = [int(n) for n in nombres]
cordTuple3 = tuple(cord2)

# calcul de distance
distance = math.sqrt((cordTuple3[0]-cordTuple[0])**2 +
                     (cordTuple3[1]-cordTuple[1])**2 +
                     (cordTuple3[2]-cordTuple[2])**2)
print("Parsing coordinates", sys.argv[1])
print("Parsed position:", cordTuple3)
print(f"Distance betwen:{cordTuple} and {cordTuple3} : {distance}")
print()

# coordone entre par l utilisateur

cord2 = "abc,dcd,trd"
nombres = cord2.split(",")
nb = []
# le i prend la valeur a la case du tableaux ou on de de chercher
try:
    for i in nombres:
        nb.append(int(i))
except ValueError:
    print(f"Error parsing coordinates: "
          f"invalid literal for int() with base 10:{i}")
    print(f"Error details - Type: ValueError, Args:"
          f" (invalid literal for int() with base 10: {i},)")
print()
print("Unpacking demonstration:")
x, y, z = cordTuple3
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")
