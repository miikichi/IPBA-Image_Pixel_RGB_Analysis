import tkinter.filedialog as fd
import PIL.Image

def RgbToColorCode(R,G,B):
    color_code = '#%02x%02x%02x' % (R, G, B)
    return color_code

def openImage():
    filePath = fd.askopenfilename()
    loadedFile = PIL.Image.open(filePath)
    return loadedFile

im = openImage()
rate = float(input("画像のサイズの割合を指定してください（例、50％＝0.5、10％＝0.1）"))
print(type(rate))
if not isinstance(rate, float):
    print("入力した数値は少数ではないです！")
else:
    if im:
        print("File loaded!")
    
        output = []
        width, height = im.size
        subWidth = round(width * rate)
        subHeight = round(height * rate)
        rgb_im = im.convert('RGBA')
        resizedIm = rgb_im.resize((subWidth,subHeight))
        print("width:", width)
        print("height:", height)

        for i in range(subWidth):
            for n in range(subHeight):
                r, g, b, a = resizedIm.getpixel((i, n))
                if a >= 0.7:
                    output.append(RgbToColorCode(r, g, b))
                else:
                    output.append("E")
    
        output.append(subHeight)

        f = open('main_output.txt', 'w')
        for x in output:
            f.write(str(x) + "\n")
        f.close()