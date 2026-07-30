from PIL import Image

def make_flawless_transparent(in_path, out_path):
    img = Image.open(in_path).convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for R, G, B, A in datas:
        # Calculate alpha based on the Blue channel
        # White has B=255, Yellow has B=~7
        alpha = 255 - min(255, max(0, int((B - 7) * (255 / (255 - 7)))))
        
        # Output pure yellow with the calculated alpha
        newData.append((254, 183, 7, alpha))

    img.putdata(newData)
    img.save(out_path, "PNG")

make_flawless_transparent("assets/Symbol.png", "assets/opt/Symbol.png")
