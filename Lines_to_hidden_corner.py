import cv2
import numpy as np


box = "box1"

if box is 'box1':
    boundry_pairs_1 = np.array([[731, 314, 847, 332],[672, 550, 573, 468], [557, 337, 672, 374]])
    boundry_pairs_2 = np.array([[557, 337, 731, 314], [832, 449, 672, 550],[847, 332, 672, 374]])
    boundry_pairs_3 = np.array([[672, 550, 672, 374], [573, 468, 557, 337],[847, 332, 832, 449]])
    opposite_point_2 = np.array([573, 468])
    opposite_point_3 = np.array([731, 314])
    opposite_point_1 = np.array([832, 449])

if box is 'box2':
    boundry_pairs_1 = np.array([[864 , 289, 507 , 277], [824 , 333, 395 , 317], [820 , 578, 408 , 538]])
    boundry_pairs_2 = np.array([[394 , 316, 408 , 539], [825 , 331, 821 , 578], [865 , 289, 859 , 495]])
    boundry_pairs_3 = np.array([[396 , 316, 504 , 276], [824 , 332, 865 , 289], [820 , 576, 860 , 496]])
    opposite_point_2 = np.array([507 , 275])
    opposite_point_3 = np.array([407 , 540])
    opposite_point_1 = np.array([862 , 498])

if box is 'box3':
    boundry_pairs_1 = np.array([[928 , 697, 748 , 603],[947 , 616, 760 , 527], [1055 , 551, 883 , 475]])
    boundry_pairs_2 = np.array([[927 , 696, 1037 , 622], [947 , 615, 1054 , 552],[760 , 527, 884 , 476]])
    boundry_pairs_3 = np.array([[759 , 525, 745 , 604], [946 , 617, 927 , 697],[1054 , 552, 1036 , 623]])
    opposite_point_2 = np.array([745 , 603])
    opposite_point_3 = np.array([883 , 476])
    opposite_point_1 = np.array([1036 , 621])

if box is 'pallet1':
    boundry_pairs_1 = np.array([[796 , 619, 1206 , 450], [797 , 717, 1195 , 535], [499 , 419, 874 , 315]])
    boundry_pairs_2 = np.array([[796 , 719, 508 , 502], [796 , 619, 499 , 419], [1207 , 451, 873 , 315]])
    boundry_pairs_3 = np.array([[498 , 418, 510 , 501], [800 , 618, 801 , 719], [1205 , 451, 1196 , 535]])
    opposite_point_2 = np.array([1196 , 533])
    opposite_point_3 = np.array([873 , 316])
    opposite_point_1 = np.array([508 , 502])

if box is 'pallet2':
    boundry_pairs_1 = np.array([[844 , 482, 1123 , 287], [845 , 535, 1123 , 329], [600 , 371, 891 , 202]])
    boundry_pairs_2 = np.array([[844 , 535, 603 , 420], [844 , 483, 600 , 371], [1123 , 285, 892 , 201]])
    boundry_pairs_3 = np.array([[599 , 372, 601 , 419], [846 , 483, 845 , 534], [1124 , 286, 1122 , 326]])
    opposite_point_2 = np.array([1123 , 330])
    opposite_point_3 = np.array([893 , 199])
    opposite_point_1 = np.array([602 , 419])

color_1 = (255,102,0)#blue
color_2 = (51,153,0)#green
color_3 = (0,50,255)#red

def draw_lines( O_frame, boundry_lines, color, thickness=2):
    for line in boundry_lines:
        cv2.line(O_frame, tuple([line[0], line[1]]), tuple([line[2],line[3]]), color, thickness)
    return O_frame

def draw_line(O_frame, points , color, thickness=1):
    cv2.line(O_frame, tuple([points[0], points[1]]), tuple([points[2], points[3]]), color, thickness)
    return O_frame


def draw_point(O_frame, point, color, thickness=2, radius=6):
    point = point.astype(int)
    O_frame = cv2.circle(O_frame, tuple(point), radius, color, thickness)
    return O_frame

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c

def get_intersection_point(O_img, boundry_pairs, color=(255,0,0), detail_draw= True):
    line_equs = [[0, 0,0]]
    intersection_points = [[0,0]]
    for line in boundry_pairs:
        p1 = np.float64(cart2homo_cordinates(line[0:2]))
        p2 = np.float64(cart2homo_cordinates(line[2:4]))
        line = np.cross(p1,p2)

        line_equs = np.append(line_equs, [line], axis=0)
    line_equs = np.float64(line_equs[1:4])
    print(line_equs)
    # print(cross(line_equs[0], line_equs[1]))
    intersection_points = np.append(intersection_points, [homo2cart_coordinates(np.cross(line_equs[0], line_equs[1]))], axis=0)
    intersection_points = np.append(intersection_points, [homo2cart_coordinates(np.cross(line_equs[0], line_equs[2]))], axis=0)
    intersection_points = np.append(intersection_points, [homo2cart_coordinates(np.cross(line_equs[1], line_equs[2]))], axis=0)
    intersection_points =intersection_points[1:]
    print(intersection_points)
    avg_intersection_point = np.average(intersection_points, axis=0)
    if detail_draw is True:
        img = draw_point(O_img, intersection_points[0], color, 1)
        img = draw_point(O_img, intersection_points[1], color, 1)
        img = draw_point(O_img, intersection_points[2], color, 1)
        img = draw_point(O_img, avg_intersection_point, color, 2)
    else:
        img = draw_point(O_img, avg_intersection_point, color, -1, 3)
    return avg_intersection_point
    # cv2.imshow('Image111', img)


def cart2homo_cordinates(point):
    point = np.append(point, [[1]])
    return point

def homo2cart_coordinates(point):
    point = np.array([point[0]/point[2], point[1]/point[2]])
    return point


if box is 'box1':
    O_img = cv2.imread('pictures/box3.png')
if box is 'box2':
    O_img = cv2.imread('pictures/box4.png')
if box is 'box3':
    O_img = cv2.imread('pictures/box5.png')
if box is 'pallet1':
    O_img = cv2.imread('pictures/pallet1.png')
if box is 'pallet2':
    O_img = cv2.imread('pictures/pallet2.png')

img = draw_lines( O_img, boundry_pairs_1, color_1) #Blue
img = draw_lines( O_img, boundry_pairs_2, color_2) # Green
img = draw_lines( O_img, boundry_pairs_3, color_3) # Red
img = draw_point(O_img, opposite_point_1, color_1)
img = draw_point(O_img, opposite_point_2, color_2)
img = draw_point(O_img, opposite_point_3, color_3)

intersection_point_1 = np.float64(get_intersection_point(O_img, boundry_pairs_1, color_1))
intersection_point_2 = np.float64(get_intersection_point(O_img, boundry_pairs_2, color_2))
intersection_point_3 = np.float64(get_intersection_point(O_img, boundry_pairs_3, color_3))

# print(np.append(opposite_point_1, intersection_point_1).astype(int))
target_lines = [np.append(opposite_point_1, intersection_point_1, axis=0).astype(int)]
target_lines = np.append(target_lines, [np.append(opposite_point_2, intersection_point_2, axis=0).astype(int)], axis=0)
target_lines = np.append(target_lines, [np.append(opposite_point_3, intersection_point_3, axis=0).astype(int)], axis=0)
draw_line(img, target_lines[0] , color_1, 1)
draw_line(img, target_lines[1] , color_2, 1)
draw_line(img, target_lines[2] , color_3, 1)

final_hidden_point = get_intersection_point(O_img, target_lines, (66, 66, 245), True)
draw_line(img, np.append(final_hidden_point, opposite_point_1, axis=0).astype(int), color_1,2)
draw_line(img, np.append(final_hidden_point, opposite_point_2, axis=0).astype(int), color_2,2)
draw_line(img, np.append(final_hidden_point, opposite_point_3, axis=0).astype(int), color_3,2)


cv2.imshow('Boundry lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()