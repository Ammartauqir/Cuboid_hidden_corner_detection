import cv2
import numpy as np
from argparse import ArgumentParser


parser = ArgumentParser(description='Demo: import images')
parser.add_argument('-i', '--image',
                    nargs='?',
                    required=False,
                    help='path to images directory',
                    default= 'pictures/Box1/Picture1.png')
args = parser.parse_args()

print("Image Path:", args.image)


O_img = cv2.imread(args.image)

point_count = 1
C_points = np.array([])
def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY,point_count, C_points
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(O_img,(x,y),2,(255,0,0),-1)
        mouseX,mouseY = x,y
        print (str(mouseX)+' , '+str(mouseY))
        C_points = np.append([C_points],[mouseX, mouseY])
        point_count = point_count + 1

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while(1):
    cv2.imshow('image',O_img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27 or point_count>7:
        C_points = C_points.astype(int)
        print(C_points)
        cv2.destroyAllWindows()
        break
    elif k == ord('a'):
        print(str(mouseX) + str(mouseY))

p1 = np.array([C_points[0], C_points[1]])
p2 = np.array([C_points[2], C_points[3]])
p3 = np.array([C_points[4], C_points[5]])
p4 = np.array([C_points[6], C_points[7]])
p5 = np.array([C_points[8], C_points[9]])
p6 = np.array([C_points[10], C_points[11]])
p7 = np.array([C_points[12], C_points[13]])



def draw_lines( O_frame, boundry_lines, color, thickness=2):
    for line in boundry_lines:
        cv2.line(O_frame, tuple([line[0], line[1]]), tuple([line[2],line[3]]), color, thickness)
    return O_frame

def draw_line(O_frame, points , color, thickness=1):
    cv2.line(O_frame, tuple([points[0], points[1]]), tuple([points[2], points[3]]), color, thickness)
    return O_frame

def draw_point_uncertainity(O_frame, means, cov_mat, size, color, thickness=2, radius=0 ):

    x1_p1, y1_p1 = np.random.multivariate_normal([means[0][0],means[0][1]], cov_mat, size).T.astype(int)
    x1_p2, y1_p2 = np.random.multivariate_normal([means[0][2], means[0][3]], cov_mat, size).T.astype(int)
    x2_p1, y2_p1 = np.random.multivariate_normal([means[1][0], means[1][1]], cov_mat, size).T.astype(int)
    x2_p2, y2_p2 = np.random.multivariate_normal([means[1][2], means[1][3]], cov_mat, size).T.astype(int)
    x3_p1, y3_p1 = np.random.multivariate_normal([means[2][0], means[2][1]], cov_mat, size).T.astype(int)
    x3_p2, y3_p2 = np.random.multivariate_normal([means[2][2], means[2][3]], cov_mat, size).T.astype(int)
    for i1, j1, k1, l1, i2, j2, k2, l2, i3, j3, k3, l3 in zip(x1_p1, y1_p1, x1_p2, y1_p2, x2_p1, y2_p1, x2_p2, y2_p2, x3_p1, y3_p1, x3_p2, y3_p2):
        O_frame = cv2.circle(O_frame, tuple([i1, j1]), radius, color, thickness)
        O_frame = cv2.circle(O_frame, tuple([k1, l1]), radius, color, thickness)
        O_frame = cv2.circle(O_frame, tuple([i2, j2]), radius, color, thickness)
        O_frame = cv2.circle(O_frame, tuple([k2, l2]), radius, color, thickness)
        get_intersection_point(O_img, np.array([[i1, j1, k1, l1],[i2, j2, k2, l2],[i3, j3, k3, l3]]), color, False)
    return O_frame

def get_uncertain_boundrypair(boundry_pairs, cov_mat, size):
    pass

def draw_point(O_frame, point, color, thickness=2, radius=6):
    point = point.astype(int)
    O_frame = cv2.circle(O_frame, tuple(point), radius, color, thickness)
    return O_frame

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c

def get_intersection_point(O_img, boundry_pairs, color=(255,0,0), detail_draw= False):
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



if p7[0] < p3[0]:
    boundry_pairs_1 = np.array([np.append(p1, p2), np.append(p3, p4), np.append(p5, p6)])
    opposite_point_1 =np.array(p7)
    boundry_pairs_2 = np.array([np.append(p1, p7), np.append(p3, p5), np.append(p4, p6)])
    opposite_point_2 = np.array(p2)
    boundry_pairs_3 = np.array([np.append(p7, p5), np.append(p1, p3), np.append(p2, p4)])
    opposite_point_3 = np.array(p6)
elif p7[0] > p3[0]:
    boundry_pairs_1 = np.array([np.append(p1, p2), np.append(p3, p4), np.append(p5, p6)])
    opposite_point_1 =np.array(p7)
    boundry_pairs_2 = np.array([np.append(p5, p7), np.append(p3, p1), np.append(p4, p2)])
    opposite_point_2 = np.array(p6)
    boundry_pairs_3 = np.array([np.append(p1, p7), np.append(p3, p5), np.append(p4, p6)])
    opposite_point_3 = np.array(p2)

color_1 = (0,0,255)#blue
color_2 = (0,255,0)#green
color_3 = (200,20,20)#red

# img = draw_lines( O_img, boundry_pairs_1, color_1) #Blue
# img = draw_lines( O_img, boundry_pairs_2, color_2) # Green
# img = draw_lines( O_img, boundry_pairs_3, color_3) # Red
# img = draw_point(O_img, opposite_point_1, color_1)
# img = draw_point(O_img, opposite_point_2, color_2)
# img = draw_point(O_img, opposite_point_3, color_3)

mean = [557, 337]
cov_mat = [[6, 0], [0, 6]]
sample_size = 50
# img =draw_point_uncertainity(O_img, boundry_pairs_2, cov_mat, sample_size,color_2)
# img =draw_point_uncertainity(O_img, boundry_pairs_1, cov_mat, sample_size,color_1)
# img =draw_point_uncertainity(O_img, boundry_pairs_3, cov_mat, sample_size,color_3)



# cv2.imshow('Boundry lines', O_img)
cv2.waitKey(0)

intersection_point_1 = np.float64(get_intersection_point(O_img, boundry_pairs_1, color_1))
intersection_point_2 = np.float64(get_intersection_point(O_img, boundry_pairs_2, color_2))
intersection_point_3 = np.float64(get_intersection_point(O_img, boundry_pairs_3, color_3))

# print(np.append(opposite_point_1, intersection_point_1).astype(int))
target_lines = [np.append(opposite_point_1, intersection_point_1, axis=0).astype(int)]
target_lines = np.append(target_lines, [np.append(opposite_point_2, intersection_point_2, axis=0).astype(int)], axis=0)
target_lines = np.append(target_lines, [np.append(opposite_point_3, intersection_point_3, axis=0).astype(int)], axis=0)
# draw_line(img, target_lines[0] , color_1, 1)
# draw_line(img, target_lines[1] , color_2, 1)
# draw_line(img, target_lines[2] , color_3, 1)

final_hidden_point = get_intersection_point(O_img, target_lines, (66, 66, 245), False)
draw_line(O_img, np.append(final_hidden_point, opposite_point_1, axis=0).astype(int), color_1,2)
draw_line(O_img, np.append(final_hidden_point, opposite_point_2, axis=0).astype(int), color_2,2)
draw_line(O_img, np.append(final_hidden_point, opposite_point_3, axis=0).astype(int), color_3,3)

# O_img =draw_point_uncertainity(O_img, final_hidden_point, cov_mat, sample_size,color_3)

cv2.imshow('Boundry lines', O_img)
cv2.waitKey(0)
cv2.destroyAllWindows()