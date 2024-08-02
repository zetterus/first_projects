import pickle

with open(r"D:\python\first_projects\mine\tetris\highscores.pkl", "wb+") as file:
    champs_voc = pickle.load(file)
    champs_voc["name"] = "record"
    if len(champs_voc) < 10:
        champs_voc = {k: v for k, v in sorted(champs_voc, key=lambda x: x[1], reverse=True)}
        champs_voc.popitem()
    pickle.dump(champs_voc, file)
    data = pickle.load(file)
    print(data)