people = []

for i in range(2):

    person = {}

    print()

    print(i + 1, "人目")

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