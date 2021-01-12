import matplotlib.pyplot as plt
from wordcloud import WordCloud
import csv
from os import path
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_gradient_magnitude
hateTypes = ["classOnly", "disabilityOnly", "ethnicityOnly",
             "genderOnly", "nationalityOnly", "religionOnly", "sexualOnly"]
for hateType in hateTypes:
    # read csv file
    reader = csv.reader(open('resultCSV/'+hateType+'2015-2020_output.csv', 'r', newline='\n'))
    d = {}
    # exclude the first row
    headers = next(reader)
    # store to Dict
    for k, v in reader:
        d[k] = float(v)

    # current path
    dirctory = path.dirname(__file__)+'/wordCloud/backGround'
    # backgroundmask = np.array(Image.open(path.join(dirctory, "penguin.png")))
    backgroundmask = np.array(Image.open(path.join(dirctory, "usa.jpg")))

    # set word cloud parameters
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
    wordcloud = wordcloud.generate_from_frequencies(d)
    # save to file
    outputDirctory = path.dirname(__file__) + "/wordCloud/trialImage/USA/"
    wordcloud.to_file(outputDirctory+hateType+'wordcloud.png')
    # # below are show image immediately after execution
    # # set image title
    # plt.figure(hateType+"Term word cloud")
    # # show image
    # plt.imshow(wordcloud)
    # # 关闭图像坐标系
    # plt.axis("off")
    # plt.show()
