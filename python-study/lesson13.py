people = [
    {"name": "Takeshi", "age": "30", "hobby": "ボウリング"},
    {"name": "Yamada", "age": "25", "hobby": "野球"},
    {"name": "Suzuki", "age": "40", "hobby": "ゴルフ"}
]

file = open("people.txt", "w")

for person in people:

    file.write(person["name"] + ",")

    file.write(person["age"] + ",")

    file.write(person["hobby"] + "\n")



print("保存しました。")

person = {}

print("新しい人を登録します。")

person["name"] = input("名前：")
person["age"] = input("年齢：")
person["hobby"] = input("趣味：")

people.append(person)

print()

file.write(person["name"] + ",")

file.write(person["age"] + ",")

file.write(person["hobby"] + "\n")

file.close()

print("新たに1名保存しました。")
