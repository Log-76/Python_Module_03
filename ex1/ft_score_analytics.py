import sys

if len(sys.argv) == 1:
    print("No scores provided. Usage: "
          "python3 ft_score_analytics.py <score1> <score2> ...")
else:
    list_score = []
    i = 1
    while i < len(sys.argv):
        list_score.append(int(sys.argv[i]))
        i += 1
    print("=== Player Score Analytics ===")
    print(f"Scores processed: {list_score}")
    print(f"Total players: {len(sys.argv)-1}")
    print(f"Total score: {sum(list_score)}")
    print(f"Average score: {sum(list_score)/(len(sys.argv)-1)}")
    print(f"High score: {max(list_score)}")
    print(f"Low score: {min(list_score)}")
    print(f"Score range: {max(list_score)-min(list_score)}")
