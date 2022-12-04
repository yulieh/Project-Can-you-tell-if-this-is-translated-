from matplotlib import pyplot as plt
import json

try:
    with open("databse.json", "r") as f:
        database = json.load(f)
except Exception as e:
    print(f"Failed to load database. Error {e}")

native_score = []
nonnative_score = []

for id in database.keys():
    if database[id]["native count"] and database[id]["nonnative count"]:
        if database[id]["native positive"]:
            native_score.append(
                database[id]["native positive"] / database[id]["native count"]
            )
        else:
            native_score.append(0)

        if database[id]["nonnative positive"]:
            nonnative_score.append(
                database[id]["nonnative positive"] / database[id]["nonnative count"]
            )
        else:
            nonnative_score.append(0)

plt.scatter([i for i in range(len(native_score))], native_score)
plt.scatter([i for i in range(len(nonnative_score))], nonnative_score)
plt.legend(["Native Score", "Non-native Score"])
plt.xlabel("Tweets with responses")
plt.ylabel("Score")
plt.title("Average scores of each tweet")
plt.show()
