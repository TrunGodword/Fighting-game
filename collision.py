import pygame
import settings

screen = settings.pygame.display.get_surface()

maxWidth, maxHeight = screen.get_width(), screen.get_height()

width = maxWidth // 8
height = maxHeight// 8
array1= []
array2= []
array3= []
array4= []
array5= []
array6= []
array7= []
array8= []

line1 = []
line2 = []
line3 = []
line4 = []
line5 = []
line6 = []
line7 = []
line8 = []
lines = [line1, line2, line3, line4, line5, line6, line7, line8]

array1.append([0, 0])
array2.append([width, 0])
array3.append([width*2, 0])
array4.append([width*3, 0])
array5.append([width*4, 0])
array6.append([width*5, 0])
array7.append([width*6, 0])
array8.append([width*7, 0])
arrays= [array1, array2, array3, array4, array5, array6, array7, array8]

for value in range(1, 9):
    value2 = value - 1
    array1.append([array1[value2][0], array1[value2][1]+height])
    array2.append([array2[value2][0], array2[value2][1]+height])
    array3.append([array3[value2][0], array3[value2][1]+height])
    array4.append([array4[value2][0], array4[value2][1]+height])
    array5.append([array5[value2][0], array5[value2][1]+height])
    array6.append([array6[value2][0], array6[value2][1]+height])
    array7.append([array7[value2][0], array7[value2][1]+height])
    array8.append([array8[value2][0], array8[value2][1]+height])

# for value in range(0, len(arrays)):
    # print(arrays[value])

surface = pygame.Surface((width, height))