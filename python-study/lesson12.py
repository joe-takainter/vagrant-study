people = [
    {"name": "Takeshi", "age": "30", "hobby": "ボウリング"},
    {"name": "Yamada", "age": "25", "hobby": "野球"},
    {"name": "Suzuki", "age": "40", "hobby": "ゴルフ"}
]

person = {}

print("新しい人を登録します。")

person["name"] = input("名前：")
person["age"] = input("年齢：")
person["hobby"] = input("趣味：")

people.append(person)

print()

print("=== 登録一覧 ===")

for person in people:

    print("----------------")
    print("名前：", person["name"])
    print("年齢：", person["age"])
    print("趣味：", person["hobby"])