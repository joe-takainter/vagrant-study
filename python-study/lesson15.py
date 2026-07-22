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

delete_name = input("削除する名前を入力してください：")

found = False

for person in people:

    if person["name"] == delete_name:

        people.remove(person)

        found = True

        break

if found:
    print("削除しました。")
else:
    print("その名前はありません。")

file = open("people.txt", "w")

for person in people:

    file.write(person["name"] + ",")
    file.write(person["age"] + ",")
    file.write(person["hobby"] + "\n")

file.close()

print()

print("=== 登録一覧 ===")

for person in people:

    print("----------------")
    print("名前:", person["name"])
    print("年齢:", person["age"])
    print("趣味:", person["hobby"])