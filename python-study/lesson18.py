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

print("===== 住所録 =====")
print("1. 一覧表示")
print("2. 検索")
print("3. 追加")
print("4. 更新")
print("5. 削除")
print("6. 終了")

menu = input("番号を入力してください：")

if menu == "1":

    print()
    print("=== 登録一覧 ===")

    for person in people:

        print("----------------")
        print("名前：", person["name"])
        print("年齢：", person["age"])
        print("趣味：", person["hobby"])

elif menu == "2":

    print("検索を実行します。")

elif menu == "3":

    print("追加を実行します。")

elif menu == "4":

    print("更新を実行します。")

elif menu == "5":

    print("削除を実行します。")

elif menu == "6":

    print("終了します。")

else:

    print("正しい番号を入力してください。")