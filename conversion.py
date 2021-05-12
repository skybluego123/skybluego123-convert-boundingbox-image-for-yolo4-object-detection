import os
import json


def convert(left, top, width, height):
    dw = 1.0/640 # divison to make it between (0,1)
    dh = 1.0/640 

    x = left + width/2.0
    y = top + height/2.0

    x = x * dw
    width = width * dw
    y = y * dh
    height = height * dh

    return (x, y, width, height)

classes = ['Manhole', 'Inlet']
with open('test.json') as f:
    d = json.load(f)

    for img in d:
        img_id = img.split('.')[0]
        bboxes = d[img]
        out_file = './labels/' + img_id + '.txt'
        with open(out_file, 'w') as txtfile:
            for bbox in bboxes:
                left, top, width, height, label = bbox['left'], bbox['top'], bbox['width'], bbox['height'], bbox['label']
                class_id = classes.index(label)
                bb = convert(left, top, width, height)
                txtfile.write(str(class_id) + " " + " ".join(str(a) for a in bb) + '\n')

    imgs = list(d.keys())
    # train_imgs = imgs[:-200]
    # val_imgs = imgs[-200:]

    # location = os.getcwd()
    with open('test.txt', 'w') as trainfile:
        for im in imgs:
            trainfile.write('data/obj/' + im + '\n')

    # with open('val.txt', 'w') as valfile:
    #     for im in val_imgs:
    #         valfile.write('data/obj/' + im + '\n')     
    

