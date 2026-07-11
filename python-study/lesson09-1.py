person = {}

person["name"] = input("名前：")
person["age"] = int(input("年齢："))

print()

if person["age"] >= 20:
    print(person["name"], "さんは成人です。")
else:
    print(person["name"], "さんは未成年です。")