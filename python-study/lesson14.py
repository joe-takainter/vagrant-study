people = []

file = open("people.txt", "r")

for line in file:

    line = line.strip()

    data = line.split(",")

    person = {}

    person["name"] = data[0]
    person["age"] = data[1]
    person["hobby"] = data[2]

    people.append(person)

file.close()

print("=== 登録一覧 ===")

for person in people:

    print("----------------")
    print("名前：", person["name"])
    print("年齢：", person["age"])
    print("趣味：", person["hobby"])