import pandas as pd
import cv2

img_path = 'color1.jpg'
dataset_path = 'colors.csv'

index = ['Color', 'Color-Name', 'Hex-Code', 'R', 'G', 'B']
df = pd.read_csv(dataset_path, names = index, header = None)

image = cv2.imread(img_path)
image = cv2.resize(image, (900, 700))

clicked = False 
r = g = b = xposition = yposition = 0

print(type(b))
print(type(g))
print(type(r))

def get_color_name_function(R, G, B):
	minimum = 1000
	for i in range (len(df)):
		d = abs(R - int(df.loc [i, 'R'])) + abs(R - int(df.loc [i, 'G'])) + abs(R - int(df.loc [i, 'B']))
		if d <= minimum:
			minimum = d
			cname = df.loc [i, 'Color-Name']

	return cname

def get_color_name_function_1(R, G, B):
	minimum = 1000
	for i in range (len(df)):
		d = abs(R - int(df.loc [i, 'R'])) + abs(R - int(df.loc [i, 'G'])) + abs(R - int(df.loc [i, 'B']))
		if d <= minimum:
			minimum = d
			ename = df.loc [i, 'Hex-Code']

	return ename

def draw_function(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		global clicked, r, g, b, xposition , yposition
		clicked = True
		xposition = x
		yposition = y
		b, g, r = image[y, x]
		b = int(b)
		g = int(g)
		r = int(r)

cv2.namedWindow('Image-Window')
cv2.setMouseCallback('Image-Window', draw_function)

while True:
	cv2.imshow('Image-Window', image)
	if clicked:
		
		cv2.rectangle(image, (825, 36), (145, 90), (b, g, r), -1)

		text = get_color_name_function(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
		text_1 = get_color_name_function_1(r, g, b)
	
		cv2.putText(image, text, (325, 65), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
		cv2.putText(image, text_1, (180, 65), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

		if r+g+b >= 600:
			cv2.putText(image, text, (325, 65), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
			cv2.putText(image, text_1, (180, 65), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()