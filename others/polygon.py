import fiona # pip install Fiona
from shapely.geometry import mapping, Polygon
# from shapely.geometry import Polygon # https://gis.stackexchange.com/questions/90055/finding-if-two-polygons-intersect-in-python
from shapely.geometry import shape # https://gis.stackexchange.com/questions/251812/returning-percentage-of-area-of-polygon-intersecting-another-polygon-using-shape

from PIL import Image, ImageDraw
im = Image.open("2020-01-24,15:42:26.tiff.jpg")
d = ImageDraw.Draw(im)

# line satu
l1_top_left = (120, 200)
l1_bottom_left = (845, 1074)
l1_top_right = (140, 188)
l1_bottom_right = (1260, 1076)
line1 = Polygon([l1_bottom_left, l1_bottom_right, l1_top_right, l1_top_left]) # line1

line_color = (0, 0, 255)

d.line([l1_top_left, l1_bottom_left, l1_bottom_right, l1_top_right, l1_top_left], fill=line_color, width=2)

# line kedua
l2_top_left = (140, 188)
l2_bottom_left = (1260, 1076)
l2_top_right = (162, 191)
l2_bottom_right = (1668, 1052)
line2 = Polygon([l2_bottom_left, l2_bottom_right, l2_top_right, l2_top_left]) # line2

line_color = (0, 255, 255)

d.line([l2_top_left, l2_bottom_left, l2_bottom_right, l2_top_right, l2_top_left], fill=line_color, width=2)

# line ketiga`
l3_top_left = (162, 191)
l3_bottom_left = (1668, 1052)
l3_top_right = (193, 195)
l3_bottom_right = (1914, 970)
line3 = Polygon([l3_bottom_left, l3_bottom_right, l3_top_right, l3_top_left]) # line3

line_color = (250, 200, 155)

d.line([l3_top_left, l3_bottom_left, l3_bottom_right, l3_top_right, l3_top_left], fill=line_color, width=2)

# Dumy mobil
c1_top_left = (450, 460)
c1_bottom_left = (460, 535)
c1_top_right = (535, 460)
c1_bottom_right = (535, 540)
car = Polygon([c1_bottom_left, c1_bottom_right, c1_top_right, c1_top_left]) # car

line_color = (100, 155, 255)

d.line([c1_top_left, c1_bottom_left, c1_bottom_right, c1_top_right, c1_top_left], fill=line_color, width=2)

# try calculate the intersection
def percentage_intersection(car, lines):
    for i in range(len(lines)):
        if car.intersects(lines[i]):
            intersect_percent = (car.intersection(lines[i]).area/car.area)*100
            # intersect = lines[i].intersection(car)
            # print(intersect)
            # print(intersect.area)
            print(" >>> car intersects Line ", (i+1), " -->> percent = ", intersect_percent)
        else:
            print(" >>> car NOT intersects Line ", (i+1))

percentage_intersection(car, [line1, line2, line3])

im.save("drawn_grid.png")
