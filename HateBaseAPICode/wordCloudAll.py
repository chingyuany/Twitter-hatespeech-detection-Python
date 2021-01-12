import os
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from random import randint


def random_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):
        h  = randint(180,400)
        s = int(200.0 * 255.0 / 255.0)
        l = int(100.0 * float(randint(60, 120)) / 255.0)

        return "hsl({}, {}%, {}%)".format(h, s, l)


hateDict = {}
for root, dirs, files in os.walk("./resultCSV/", topdown=False):
    for name in files:
        if(name.find("Only") != -1):
            readFile = open(os.path.join(root, name))
            for line in readFile:
                hateWord = line.strip().split(",")[0]
                count = float(line.strip().split(",")[1])
                if hateWord not in hateDict:
                    hateDict[hateWord] = count
                else:                    
                    for key in hateDict:
                        if(key == hateWord):
                            hateDict[hateWord] = hateDict[hateWord] + count

# print (hateDict)
backgroundmask = np.array(Image.open("./wordCloud/backGround/usa.jpg"))
wordcloud = WordCloud(
        scale=20,
        # 设置背景色
        background_color='white',
        # margin=2,
        # 设置背景宽
        width=1920,
        # 设置背景高
        height=1080,
        # 最大字体
        max_font_size=20,
        # 最小字体
        min_font_size=2,
        mode='RGBA',
        # line up text with image
        mask=backgroundmask
    )
wordcloud = wordcloud.generate_from_frequencies(hateDict)

wordcloud.recolor(color_func = random_color_func) 

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
# wordcloud.to_file('wordcloud.png')