import cv2
import numpy as np
from scipy.spatial import distance
import matplotlib as plt
import math


def plot_corners(corners, img):
    for corner in corners:
        # corner = np.array(corner).astype(int)
        img = cv2.circle(img,tuple(corner), 3, (0, 255, 255), -1)
    return img

def get_corners_in_homo_corrdinates(corners):
    corner_HC = [[1,1,1]]
    for corner in corners:
        corner = np.append(corner, [1])

        corner_HC = np.append(corner_HC, [corner], axis=0)
    return corner_HC[1:]

def arrange_corner_points(clustered_corners, O_frame, n_corners):
    Corners = np.array(clustered_corners) #except last corner
    Arranged_corners = np.array([Corners[0]])
    # Arranged_corners = np.append(Arranged_corners, [[2,3]], axis=0)
    Corners = np.delete(Corners, 0, axis = 0)
    for i in range(5):
        last_corner = Arranged_corners[-1]
        p_dist = 1000
        for index in range(len(Corners)):
            dist = get_eucledian_dist(last_corner, Corners[index])
            if dist < p_dist:
                p_dist = dist
                p_index = index
        # print(Corners[p_index])
        Arranged_corners = np.append(Arranged_corners, [Corners[p_index]],axis=0)
        Corners = np.delete(Corners, p_index, axis = 0)
    # for index in range(len(Arranged_corners)-1):
    #     cv2.line(O_frame, tuple(Arranged_corners[index]), tuple(Arranged_corners[index+1]), (0, 255, 0), 2)
    # cv2.line(O_frame, tuple(Arranged_corners[-1]), tuple(Arranged_corners[0]), (0, 255, 0), 2)
    # cv2.imshow("Cluster Center Reconstructed box", O_frame)
    return Arranged_corners

def get_eucledian_dist(point1 , point2):
    dst = distance.euclidean(point1, point2)
    return dst

def draw_boundry(boundry_lines, O_frame):
    for line in boundry_lines:
        cv2.line(O_frame, tuple([line[0], line[1]]), tuple([line[2],line[3]]), (0, 255, 0), 2)
    return O_frame

def corners_to_lines(arranged_corner_points):
    lines = np.empty((0,4), int)
    for index in range(len(arranged_corner_points)-1):
        line = np.append([arranged_corner_points[index]], [arranged_corner_points[index + 1]], axis=1 )
        lines = np.append(lines, line, axis=0)
    lines = np.append(lines, np.append([arranged_corner_points[-2]], [arranged_corner_points[0]], axis=1), axis=0)
    lines = np.append(lines, np.append([arranged_corner_points[1]], [arranged_corner_points[6]], axis=1), axis=0)
    lines = np.append(lines, np.append([arranged_corner_points[3]], [arranged_corner_points[6]], axis=1), axis=0)

    return lines

def draw_boundry(boundry_lines, O_frame):
    for line in boundry_lines:
        cv2.line(O_frame, tuple([line[0], line[1]]), tuple([line[2],line[3]]), (200, 255, 0), 2)
    return O_frame


def get_slope_of_lines(boundry_lines):
    slopes = np.array([])
    for line in boundry_lines:
        if np.abs(line[0]-line[2]):
            slope = (line[1]-line[3]) / (line[0]-line[2])
            slopes = np.append(slopes, slope)
        else:
            slopes = np.append(slopes, [100]) #very high slope
    return slopes

def draw_paired_boundry_lines(paired_boundry_lines, O_frame):
    for side_boundry_pair in paired_boundry_lines[6:9]:
        cv2.line(O_frame, tuple(side_boundry_pair[0:2]), tuple(side_boundry_pair[2:4]), (0, 0, 255), 2)
    for front_back_face_boundry_pair in paired_boundry_lines[3:6]:
        cv2.line(O_frame, tuple(front_back_face_boundry_pair[0:2]), tuple(front_back_face_boundry_pair[2:4]), (255, 150, 0), 2)
    for longitudnal_face_boundry_pair in paired_boundry_lines[0:3]:
        cv2.line(O_frame, tuple(longitudnal_face_boundry_pair[0:2]), tuple(longitudnal_face_boundry_pair[2:4]),(150, 200, 200), 2)
    return O_frame


corners = np.array([[731 , 314], [847 , 332], [832 , 449], [672 , 550], [573 , 468], [557 , 337], [672 , 374]])
O_img = cv2.imread('pictures/CapBoxImg/Picture1.png')
img = plot_corners(corners, O_img)
cv2.imshow('Image', img)
corners_HC = get_corners_in_homo_corrdinates(corners)
arranged_corner_points = arrange_corner_points(corners[0:6], O_img, 6)
arranged_corner_points = np.append(arranged_corner_points, [corners[-1]], axis=0)
boundry_lines = corners_to_lines(arranged_corner_points)
img_with_reconstructed_boundires = draw_boundry(boundry_lines, O_img)
cv2.imshow("Reconstructed Boundry lines", img_with_reconstructed_boundires)
slope_of_lines = get_slope_of_lines(boundry_lines)
slope_sorted_boundry_lines_index = np.argsort(slope_of_lines)
paired_boundry_lines = np.empty((0,4), int)
for sorted_index in slope_sorted_boundry_lines_index:
    paired_boundry_lines = np.append(paired_boundry_lines, [boundry_lines[sorted_index]], axis=0)
frame_with_paied_bondries = draw_paired_boundry_lines(paired_boundry_lines, O_img)
print(paired_boundry_lines)
cv2.imshow("Boundry pairs color coded", frame_with_paied_bondries)


# draw_boundry(boundry_lines, O_frame)
# lines = corners_to_lines(corners)
cv2.waitKey(0)
cv2.destroyAllWindows()
