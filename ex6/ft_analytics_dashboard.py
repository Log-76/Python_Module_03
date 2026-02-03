data = {"alice": {"score": 2300, "actif": True, "achi": 5, "achive":
                  ["first_kill", "level_10", "boss_slayer", "colecteur",
                   "champoin"]},
        "bob": {"score": 1800, "actif": True, "achi": 3, "achive":
                ["level_10", "first_blood", "explorer"]},
        "charlie": {"score": 2150, "actif": True, "achi": 7, "achive":
                    ["level_10", "hundred_kills", "warrior", "berserker",
                     "flawless_victory", "first_kill",
                     "critical_striker",]},
        "diana": {"score": 2050, "actif": False, "achi": 2, "achive":
                  ["level_10", "first_kill"]}}

score_categorie = {"higth": {"nb": 3},
                   "medium": {"nb": 2},
                   "low": {"nb": 1}}

achivement = {"first_kill", "level_10", "boss_slayer"}
region = {"north", "east", "central"}
print("=== Game Analytics Dashboard ===")
print()
print("=== List Comprehension Examples ===")
score = [joueur for joueur in data if data[joueur]["score"] > 2000]
print("High scorers (>2000)", score)
scoredouble = [data[joueur]["score"] * 2 for joueur in data]
print("Scores doubled:", scoredouble)
actif = [joueur for joueur in data if data[joueur]["actif"]]
print("Active players", actif)
print()
print("=== Dict Comprehension Examples ===")
playScore = [f"{joueur} : {data[joueur]['score']}"
             for joueur in data if data[joueur]["actif"]]
print("Player scores:", playScore)
cate = [f"{joueur} : {score_categorie[joueur]['nb']}"
        for joueur in score_categorie]
print("Score categories:", cate)
achiv = [f"{joueur} : {data[joueur]['achi']}"
         for joueur in data if data[joueur]["actif"]]
print("Achievement counts:", achiv)
print()
print("=== Set Comprehension Examples ===")
player = {joueur for joueur in data}
print("Unique players:", player)
print("Unique achievements", achivement)
print("Active regions:", region)
print()
print("=== Combined Analysis ===")
max_player = 0
for _ in data:
    max_player += 1
print("Total players:", max_player)
unique_achi = {achi
               for joueur in data
               for achi in data[joueur]["achive"]}
print("Total unique achievements:", len(unique_achi))

score_mid = 0
for joueur in data:
    score_mid += data[joueur]["score"]
score_mid = score_mid / max_player
print("Average score:", score_mid)
top_performer = max(data, key=lambda joueur: data[joueur]["score"])
perf = (max(data[joueur]["score"] for joueur in data),
        max(data[joueur]["achi"] for joueur in data))
print(f"Top performer: {top_performer} ({perf[0]} points,"
      f" {data[top_performer]['achi']} achievements)")
