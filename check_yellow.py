from PIL import Image
img = Image.open("assets/Symbol.png")
datas = img.getdata()
yellows = [p for p in datas if p[0] > 200 and p[1] > 150 and p[2] < 100]
if yellows:
    print(yellows[0])
