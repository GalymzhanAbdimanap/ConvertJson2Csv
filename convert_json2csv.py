#{'4c255e74648107e7': {'filename': '4c255e74648107e7.jpg', 'class': 'calculator', 'bbox': [0.6328125, 0.971875, 0.21875, 0.88125]}}  

import json, shutil
import cv2

json_arr=['/home/manapov/dataset_calc_phone/ann_train_phone.json','/home/manapov/dataset_calc_phone/ann_train_calc.json']
folder=['train/','test/','val/']
classes = ['cellphone/', 'calculator/']
dataset=[]
for ind, el in enumerate(json_arr):
	with open(el, 'r', encoding='utf-8') as f: #открыли файл
	    text = json.load(f) #загнали все из файла в переменную	



	
	values = text.values()
	#count=0
	#path/to/image.jpg,x1,y1,x2,y2,class_name
	
	for i in values:
		line=[]
		#img_path = '/home/manapov/dataset_calc_phone/'+folder[ind]+i['filename']
		img_path = '/home/manapov/dataset_calc_phone/train/'+classes[ind]+i['filename']
		print(img_path)
		image = cv2.imread(img_path)
		w = image.shape[1]
		h = image.shape[0]
		x1 = round(i['bbox'][0]*w)
		y1 = round(i['bbox'][2]*h)
		x2 = round(i['bbox'][1]*w)
		y2 = round(i['bbox'][3]*h)

		line.append(img_path)
		line.append(x1)
		line.append(y1)
		line.append(x2)
		line.append(y2)
		line.append(i['class'])
		dataset.append(line)
		line=[]

	

import csv
 
FILENAME = "annotations.csv"
 

 
with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(dataset)
     
 
'''with open(FILENAME, "a", newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)'''
