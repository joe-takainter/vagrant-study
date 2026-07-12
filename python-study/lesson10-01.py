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

print("登録完了！")

print(people)