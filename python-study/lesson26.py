def save_people(people):

    file = open("people.txt", "w")

    for person in people:

        file.write(person["name"] + ",")
        file.write(person["age"] + ",")
        file.write(person["hobby"] + "\n")

    file.close()

    print("住所録を保存しました。")

def show_people(people):

    print("=== 登録一覧 ===")

    for person in people:

        print("----------------")
        print(f"名前：{person['name']}")
        print(f"年齢：{person['age']}")
        print(f"趣味：{person['hobby']}")
        print()

def search_people(people):

    search_name = input("検索する名前：")

    found = False

    for person in people:

        if person["name"] == search_name:

            print()
            print("検索成功！")
            print("----------------")
            print("名前：", person["name"])
            print("年齢：", person["age"])
            print("趣味：", person["hobby"])

            found = True

            break

    if not found:

        print("その名前は登録されていません。")

def add_people(people):

    person = {}

    print("新しい人を登録します。")

    person["name"] = input("名前：")
    person["age"] = input("年齢：")
    person["hobby"] = input("趣味：")

    people.append(person)

    save_people(people)

    print("追加しました。")

def update_people(people):

    update_name = input("変更する名前：")

    found = False

    for person in people:

        if person["name"] == update_name:

            print("現在の情報")
            print("年齢：", person["age"])
            print("趣味：", person["hobby"])

            new_name = input("新しい名前（変更しない場合はEnter）：").strip()

            if new_name != "":
                person["name"] = new_name

            new_age = input("新しい年齢（変更しない場合はEnter）：").strip()

            if new_age != "":
                person["age"] = new_age

            new_hobby = input("新しい趣味（変更しない場合はEnter）：").strip()

            if new_hobby != "":
                person["hobby"] = new_hobby

            found = True

            break

    if found:

        save_people(people)

        print("更新しました。")

    else:

        print("その名前は登録されていません。")

def delete_people(people):

    delete_name = input("削除する名前：")

    found = False

    for person in people:

        if person["name"] == delete_name:

            answer = input("本当に削除しますか？（y/n）：")

            if answer.lower() == "y":

                people.remove(person)

                save_people(people)

                print("削除しました。")

                found = True

            else:

                print("削除を中止しました。")

            break

    if not found:

        print("その名前は登録されていません。")

    person = {}

    print("新しい人を登録します。")

    person["name"] = input("名前：")
    person["age"] = input("年齢：")
    person["hobby"] = input("趣味：")

    people.append(person)

    save_people(people)

    print("追加しました。")
def load_people():

    people = []

    file = open("people.txt", "r")

    for line in file:

        line = line.strip()

        data = line.split(",")

        person = {}

        person["name"] = data[0]
        person["age"] = data[1]
        person["hobby"] = data[2]

        pee =ople.append(person)

    file.close()

    return people


people = load_people()

while True:

    print("登録人数：", len(people), "人")
    print("===== 住所録 =====")
    print("1. 一覧表示")
    print("2. 検索")
    print("3. 追加")
    print("4. 更新")
    print("5. 削除")
    print("6. 終了")

    menu = input("番号を入力してください：")

    if menu == "1":

        show_people(people)

    elif menu == "2":

        search_people(people)

    elif menu == "3":

        add_people(people)

    elif menu == "4":

        update_people(people)

    elif menu == "5":

        delete_people(people)

    elif menu == "6":

        print("終了します。")

        break

    else:

        print("正しい番号を入力してください。")

    print()