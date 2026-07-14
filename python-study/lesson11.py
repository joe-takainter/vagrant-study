people = [
    {"name": "Takeshi", "age": "30", "hobby": "ボウリング"},
    {"name": "Yamada", "age": "25", "hobby": "野球"},
    {"name": "Suzuki", "age": "40", "hobby": "ゴルフ"}
]

search_name = input("検索する名前を入力してください：")

found = False

for person in people:

    if person["name"] == search_name:

        print()
        print("見つかりました！")
        print("名前:", person["name"])
        print("年齢:", person["age"])
        print("趣味は" + person["hobby"] + "です。")
        found = True

if found == False:
    print("その名前は登録されていません。")