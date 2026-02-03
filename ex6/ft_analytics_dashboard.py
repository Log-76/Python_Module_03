data = {"alice": {"score": 2300, "actif": True, "achi": 5},
        "bob": {"score": 1800, "actif": True, "achi": 3},
        "charlie": {"score": 2150, "actif": True, "achi": 7},
        "diana": {"score": 2050, "actif": False, "achi": 0}}

score_categorie = {"higth": {"nb": 3},
                   "medium": {"nb": 2},
                   "low": {"nb": 1}}

achivement = {"first_kill", "level_10", "boss_slayer"}
region = {"north", "east", "central"}
print("=== Game Analytics Dashboard ===")

print("=== List Comprehension Examples ===")
score = [joueur for joueur in data if data[joueur]["score"] > 2000]
print("High scorers (>2000)", score)
scoredouble = [data[joueur]["score"] * 2 for joueur in data]
print("Scores doubled:", scoredouble)
actif = [joueur for joueur in data if data[joueur]["actif"]]
print("Active players", actif)
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
print("=== Set Comprehension Examples ===")
player = {joueur for joueur in data}
print("Unique players:", player)
print("Unique achievements", achivement)
print("Active regions:", region)
