def judge(score):
    if score >= 90:
        print("優秀です！")
    elif score >= 80:
        print("合格です！")
    elif score >= 60:
        print("再試験です。")
    else:
        print("不合格です。")

score = int(input("点数を入力してください："))

judge(score)