import sys
import math

if len(sys.argv) == 1:
    print("No scores provided. Usage: "
          "python3 ft_score_analytics.py <score1> <score2> ...")

cord = [-5, 50, 25]
cord2 = [100, 36, 0]
cordTuple = tuple(cord)
cordTuple2 = tuple(cord2)
# calcul de distance
distance = math.sqrt((cordTuple2[0]-cordTuple2[0])**2 +
                     (cordTuple2[1]-cordTuple[1])**2 +
                     (cordTuple2[2]-cordTuple[2])**2)
print(cordTuple)
print(distance)
