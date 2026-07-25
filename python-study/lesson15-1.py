delete_name = input("削除する名前を入力してください：")

answer = input("本当に削除しますか？(y/n)：")

found = False

if answer.lower() == "y":

    for person in people:

        if person["name"] == delete_name:

            people.remove(person)

            found = True

            break

    if found:
        print("削除しました。")
    else:
        print("その名前はありません。")

else:

    print("削除を中止しました。")