import pygame
import settings
import bisect

screen = settings.pygame.display.get_surface()

maxWidth, maxHeight = screen.get_width(), screen.get_height()

width = maxWidth // 6; height = maxHeight// 6
array1= []; array2= []; array3= []; array4= []; array5= []; array6= []; array7= []; array8= []

array1.append([0, 0]); array2.append([width, 0]); array3.append([width*2, 0]); array4.append([width*3, 0]); array5.append([width*4, 0]); array6.append([width*5, 0]); array7.append([width*6, 0]); array8.append([width*7, 0])
arrays= [array1, array2, array3, array4, array5, array6, array7, array8]

line1 = []; line2 = []; line3 = []; line4 = [];  line5 = [];  line6 = [];  line7 = [];  line8 = []
lines = [line1, line2, line3, line4, line5, line6, line7, line8]

for value in range(0, 8):
    array1.append([array1[value][0], array1[value][1]+height]); array2.append([array2[value][0], array2[value][1]+height]); array3.append([array3[value][0], array3[value][1]+height]); array4.append([array4[value][0], array4[value][1]+height]); array5.append([array5[value][0], array5[value][1]+height]); array6.append([array6[value][0], array6[value][1]+height]); array7.append([array7[value][0], array7[value][1]+height]); array8.append([array8[value][0], array8[value][1]+height])
# print(arrays)
xlines = [array1[0][0], array2[0][0], array3[0][0], array4[0][0], array5[0][0], array6[0][0], array7[0][0], array8[0][0]]
ylines = [array1[0][1], array1[1][1], array1[2][1], array1[3][1], array1[4][1], array1[5][1], array1[6][1], array1[7][1]]

surface = pygame.Surface((width, height))

def position(array, number):
    index = bisect.bisect_right(array, number)
    return index

def checkCollision(object):
    positions = []
    for value in range(0, len(object)):
        positions.append(position(xlines, object[value].rect.x)-1)
        positions.append(position(ylines, object[value].rect.y)-1)
        positions.append(position(xlines, object[value].rect.x + object[value].sizex)-1)        
        positions.append(position(ylines, object[value].rect.y + object[value].sizey)-1)
        
    return positions