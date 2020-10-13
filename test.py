import pandas as pd 
import cv2

img_path = 'photo2.jpg'
csv_path = 'colors.csv'

index = ['Color', 'Color-Name', 'Hex-Code', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names = index, header = None)
print(df.head(2))

print(len(df))
print(df.loc[1 , 'B'])