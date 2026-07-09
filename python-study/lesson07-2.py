def check_age(age):
    if age >= 60:
        print("シニアです。！")
    elif age >= 20:
        print("大人です。！")
    else:
        print("子供です。。")

age = int(input("年齢を入力してください："))

check_age(age)