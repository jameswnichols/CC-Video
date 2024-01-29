from PIL import Image
from PIL import ImageFilter
CC_CONV = list("0123456789abcdef")
CC_COLOR = ["white","orange","magenta","lightBlue","yellow","lime","pink","gray","lightGray","cyan","purple","blue","brown","green","red","black"]
def getPalette(paletteData):
    actualPalette = []
    currentRGB = []
    for value in paletteData:
        currentRGB.append(value)
        if len(currentRGB) != 3:
            continue
        if currentRGB in actualPalette:
            currentRGB = []
            continue
        actualPalette.append(currentRGB)
        currentRGB = []
    return actualPalette
SCREEN_SIZE = (143, 67)
frame = Image.open("tree.jpg").convert("RGB")
frame = frame.resize(SCREEN_SIZE, Image.Resampling.BICUBIC)
frameSharpened = frame.filter(ImageFilter.SHARPEN)
frame = frame.convert('P',palette=Image.Palette.ADAPTIVE, colors=16)
frameSharpened = frameSharpened.convert("P",palette=Image.Palette.ADAPTIVE, colors=16)
frameSharpened.putpalette(frame.getpalette())
frame.save("output.png","png")
frameSharpened.save("sharp.png","png")
colors = getPalette(frame.getpalette())[:-1]
renderLines = []
for y in range(SCREEN_SIZE[1]):
    renderLines.append("")
    for x in range(SCREEN_SIZE[0]):
        renderLines[y] += CC_CONV[frameSharpened.getpixel((x, y))]

print("".join(renderLines))

# for i, color in enumerate(colors):
#     print(f"monitor.setPaletteColor(colors.{CC_COLOR[i]}, {', '.join([str(round(x/255,3)) for x in color])})")
