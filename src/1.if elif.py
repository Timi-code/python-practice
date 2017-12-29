# 0 空字符串 空list

if []:
    print("[]:true")
else:
    print("[]:false")

if 0:
    print("0:true")
else:
    print("0:false")

if "":
    print("'':true")
else:
    print("'':false")


height = input("身高：")
weight = input("体重：")
weight = int(weight)
height = float(height)

bmi = weight/(height*height)
if bmi > 32:
    print("严重肥胖")
elif bmi > 28:
    print("肥胖")
elif bmi > 25:
    print("过重")
elif bmi > 18.5:
    print("正常")
else:
    print("过轻")
