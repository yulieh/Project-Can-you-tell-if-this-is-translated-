import json
import random

valid_positive = ["1", "y", "Y", "yes", "Yes", "YES"]
valid_negative = ["0", "n", "N", "no", "No", "NO"]


def get_answer(input_text: str):
    answer = -1
    while answer not in valid_positive and answer not in valid_negative:
        answer = input(input_text)
    return answer


try:
    with open("databse.json", "r") as f:
        database = json.load(f)
except Exception as e:
    print(f"Failed to load database. Error {e}")
last_id = int(list(database.keys())[-1])

print("Welcome. Please answer the following questions.")

native_answer = get_answer(input_text="Are you a native English speaker?\n")
if native_answer in valid_positive:
    native = 1
else:
    native = 0

print("Please answer if the following tweets are written by a human (not bots)\n")
print(
    "Give a positive answer if you think the tweet was written by a human, a negative answer if you think"
    " it was computer generated"
)

for _ in range(20):
    random_id = random.randint(0, last_id)
    print(database[str(random_id)]["text"])
    human_answer = get_answer(input_text="")
    if native:
        if human_answer in valid_positive:
            database[str(random_id)]["native positive"] += 1
        database[str(random_id)]["native count"] += 1
    else:
        if human_answer in valid_positive:
            database[str(random_id)]["nonnative positive"] += 1
        database[str(random_id)]["nonnative count"] += 1


with open("databse.json", "w") as f:
    json.dump(database, f, indent=4, separators=(", ", ": "))
