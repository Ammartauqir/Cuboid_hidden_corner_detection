import cv2
import numpy as np
import matplotlib.pyplot as plt

box = "TS1_5"

if box is 'TS1_5':
    boundry_pairs_1 = np.array([[231 , 149,489 , 121],[250 , 259,530 , 229], [258 , 368,522 , 335]])
    boundry_pairs_2 = np.array([[230 , 149,238 , 253], [251 , 259,258 , 366],[489 , 122,530 , 227]])
    boundry_pairs_3 = np.array([[238 , 255,231 , 149], [258 , 367,251 , 258],[521 , 335,530 , 228]])
    opposite_point_1 = np.array([237 , 254])
    opposite_point_2 = np.array([521 , 334])
    opposite_point_3 = np.array([486 , 122])

if box is 'TS1_4':
    boundry_pairs_1 = np.array([[264 , 123,519 , 149],[222 , 229,500 , 259], [230 , 336,493 , 367]])
    boundry_pairs_2 = np.array([[221 , 229,229 , 334], [501 , 260,494 , 367],[520 , 150,513 , 254]])
    boundry_pairs_3 = np.array([[221 , 228,264 , 122], [500 , 258,520 , 148],[494 , 365,513 , 253]])
    opposite_point_1 = np.array([513 , 255])
    opposite_point_2 = np.array([264 , 122])
    opposite_point_3 = np.array([229 , 335])

if box is 'TS1_3':
    boundry_pairs_1 = np.array([[211 , 193,309 , 105],[452 , 282,538 , 180], [448 , 389,530 , 286]])
    boundry_pairs_2 = np.array([[212 , 195,452 , 281], [311 , 105,538 , 181],[219 , 300,449 , 390]])
    boundry_pairs_3 = np.array([[211 , 194,221 , 301], [453 , 281,448 , 388],[538 , 181,531 , 287]])
    opposite_point_1 = np.array([220 , 298])
    opposite_point_2 = np.array([530 , 286])
    opposite_point_3 = np.array([309 , 105])
if box is 'TS1_2':
    boundry_pairs_1 = np.array([[360 , 97,537 , 216],[222 , 161,394 , 292], [229 , 267,393 , 401]])
    boundry_pairs_2 = np.array([[229 , 267,222 , 163], [394 , 402,394 , 292],[529 , 321,538 , 214]])
    boundry_pairs_3 = np.array([[221 , 162,360 , 98], [394 , 292,539 , 216],[392 , 403,529 , 320]])
    opposite_point_1 = np.array([528,322])
    opposite_point_2 = np.array([361 , 98])
    opposite_point_3 = np.array([231 , 267])
if box is 'TS1_1':
    boundry_pairs_1 = np.array([[250 , 133,331 , 289],[413 , 99,515 , 247], [255 , 238,334 , 400]])
    boundry_pairs_2 = np.array([[248 , 130,255 , 238], [332 , 290,334 , 399],[516 , 247,510 , 354]])
    boundry_pairs_3 = np.array([[331 , 289,515 , 247], [334 , 399,507 , 355],[249 , 133,414 , 99]])
    opposite_point_1 = np.array([508 , 355])
    opposite_point_2 = np.array([413 , 99])
    opposite_point_3 = np.array([256 , 237])

if box is 'blend2':
    boundry_pairs_1 = np.array([[297 , 134,446 , 179],[212 , 174,370 , 222], [216 , 343,370 , 344]])
    boundry_pairs_2 = np.array([[211 , 174,215 , 341], [369 , 221,370 , 344],[446 , 180,446 , 292]])
    boundry_pairs_3 = np.array([[210 , 172,297 , 133], [371 , 222,445 , 179],[372 , 342,447 , 293]])
    opposite_point_2 = np.array([295 , 135])
    opposite_point_3 = np.array([216 , 340])
    opposite_point_1 = np.array([445 , 293])

# if box is 'blend1':
#     boundry_pairs_1 = np.array([[468 , 323,656 , 285],[474 , 522,655 , 480], [367 , 255,543 , 224]])
#     boundry_pairs_2 = np.array([[656 , 285,542 , 223], [467 , 322,365 , 256],[473 , 523,372 , 444]])
#     boundry_pairs_3 = np.array([[365 , 256,371 , 443], [468 , 323,473 , 523],[656 , 286,655 , 479]])
#     opposite_point_2 = np.array([656 , 481])
#     opposite_point_3 = np.array([543 , 224])
#     opposite_point_1 = np.array([372 , 444])
#
# if box is 'test1':
#     boundry_pairs_1 = np.array([[206 , 196, 274 , 151],[286 , 250, 355 , 198], [284 , 277, 354 , 219]])
#     boundry_pairs_2 = np.array([[274 , 149, 354 , 197], [206 , 196, 285 , 249],[207 , 221, 282 , 274]])
#     boundry_pairs_3 = np.array([[206 , 196, 205 , 221], [284 , 249, 283 , 276],[356 , 197, 354 , 220]])
#     opposite_point_2 = np.array([355 , 219])
#     opposite_point_3 = np.array([274 , 151])
#     opposite_point_1 = np.array([207 , 221])
#
# if box is 'test3':
#     boundry_pairs_1 = np.array([[250 , 161, 322 , 118],[277 , 179, 348 , 135], [271 , 258, 336 , 214]])
#     boundry_pairs_2 = np.array([[247 , 241, 249 , 162], [271 , 259, 276 , 181],[336 , 212, 347 , 135]])
#     boundry_pairs_3 = np.array([[347 , 134, 322 , 120], [275 , 179, 250 , 164],[271 , 259, 244 , 242]])
#     opposite_point_2 = np.array([320 , 119])
#     opposite_point_3 = np.array([335 , 215])
#     opposite_point_1 = np.array([246 , 241])
#
# if box is 'test4':
#     boundry_pairs_1 = np.array([[275 , 138, 368 , 177],[254 , 153, 349 , 193], [248 , 235, 332 , 277]])
#     boundry_pairs_2 = np.array([[248 , 235, 254 , 152], [347 , 194, 334 , 277],[369 , 175, 352 , 260]])
#     boundry_pairs_3 = np.array([[255 , 151, 276 , 137], [349 , 190, 368 , 177],[332 , 277, 351 , 260]])
#     opposite_point_2 = np.array([278 , 137])
#     opposite_point_3 = np.array([249 , 236])
#     opposite_point_1 = np.array([352 , 259])
#
# if box is 'test5':
#     boundry_pairs_1 = np.array([[448 , 414, 632 , 323],[587 , 590,780 , 483], [580 , 630,762 , 525]])
#     boundry_pairs_2 = np.array([[444 , 462,577 , 628], [449 , 414,587 , 589],[634 , 324,780 , 482]])
#     boundry_pairs_3 = np.array([[444 , 462,448 , 414], [578 , 632,588 , 590],[778 , 482,763 , 524]])
#     opposite_point_2 = np.array([763 , 523])
#     opposite_point_3 = np.array([633 , 323])
#     opposite_point_1 = np.array([443 , 462])
#
# if box is 'test6':
#     boundry_pairs_1 = np.array([[115 , 163, 192 , 123],[179 , 213,257 , 168], [182 , 240,257 , 192]])
#     boundry_pairs_2 = np.array([[192 , 123,257 , 167], [114 , 164,179 , 214],[117 , 189,181 , 242]])
#     boundry_pairs_3 = np.array([[116 , 165,117 , 189], [179 , 215,181 , 242],[258 , 167,257 , 192]])
#     opposite_point_1 = np.array([118, 191])
#     opposite_point_2 = np.array([258 , 192])
#     opposite_point_3 = np.array([191 , 125])
#
# if box is 'test7':
#     boundry_pairs_1 = np.array([[138 , 139,219 , 124],[157 , 185,244 , 167], [160 , 210,245 , 192]])
#     boundry_pairs_2 = np.array([[137 , 139,158 , 183], [218 , 125,245 , 167],[140 , 165,160 , 210]])
#     boundry_pairs_3 = np.array([[138 , 140,140 , 163], [158 , 185,160 , 210],[245 , 166,245 , 192]])
#     opposite_point_1 = np.array([141 , 165])
#     opposite_point_2 = np.array([243 , 192])
#     opposite_point_3 = np.array([219 , 126])
#
# if box is 'test8':
#     boundry_pairs_1 = np.array([[162 , 108,225 , 147],[188 , 99,249 , 137], [162 , 187,220 , 231]])
#     boundry_pairs_2 = np.array([[162 , 109,163 , 185], [223 , 148,220 , 230],[250 , 136,246 , 217]])
#     boundry_pairs_3 = np.array([[163 , 108,188 , 99], [225 , 148,249 , 137],[221 , 230,246 , 217]])
#     opposite_point_1 = np.array([246 , 216])
#     opposite_point_2 = np.array([187 , 99])
#     opposite_point_3 = np.array([164 , 187])
#
# if box is 'test9':
#     boundry_pairs_1 = np.array([[160 , 172,158 , 95],[242 , 112,239 , 191], [254 , 100,252 , 174]])
#     boundry_pairs_2 = np.array([[173 , 83,254 , 99], [159 , 95,242 , 112],[161 , 173,239 , 193]])
#     boundry_pairs_3 = np.array([[158 , 96,173 , 83], [241 , 113,255 , 100],[240 , 191,251 , 176]])
#     opposite_point_1 = np.array([173 , 85])
#     opposite_point_2 = np.array([251 , 176])
#     opposite_point_3 = np.array([161 , 172])
#
# if box is 'test10':
#     boundry_pairs_1 = np.array([[127 , 163,191 , 128],[187 , 199,250 , 161], [187 , 224,251 , 184]])
#     boundry_pairs_2 = np.array([[191 , 129,249 , 161], [126 , 164,187 , 199],[129 , 187,187 , 223]])
#     boundry_pairs_3 = np.array([[126 , 163,128 , 187], [187 , 198,187 , 224],[251 , 161,250 , 183]])
#     opposite_point_1 = np.array([128 , 186])
#     opposite_point_2 = np.array([251 , 185])
#     opposite_point_3 = np.array([192 , 129])
#
# if box is 'test11':
#     boundry_pairs_1 = np.array([[481 , 209,362 , 293],[537 , 225,418 , 314], [536 , 389,427 , 481]])
#     boundry_pairs_2 = np.array([[360 , 294,374 , 458], [420 , 313,426 , 483],[537 , 226,537 , 390]])
#     boundry_pairs_3 = np.array([[483 , 209,536 , 225], [361 , 294,419 , 314],[373 , 458,426 , 483]])
#     opposite_point_1 = np.array([373 , 457])
#     opposite_point_2 = np.array([481 , 208])
#     opposite_point_3 = np.array([535 , 390])
#
# if box is 'box1':
#     boundry_pairs_1 = np.array([[731, 314, 847, 332],[672, 550, 573, 468], [557, 337, 672, 374]])
#     boundry_pairs_2 = np.array([[557, 337, 731, 314], [832, 449, 672, 550],[847, 332, 672, 374]])
#     boundry_pairs_3 = np.array([[672, 550, 672, 374], [573, 468, 557, 337],[847, 332, 832, 449]])
#     opposite_point_2 = np.array([573, 468])
#     opposite_point_3 = np.array([731, 314])
#     opposite_point_1 = np.array([832, 449])
#
# if box is 'cam1':
#     boundry_pairs_1 = np.array([[303 , 167, 397 , 185],[262 , 229, 363 , 252], [267 , 258, 367 , 277]])
#     boundry_pairs_2 = np.array([[263 , 230, 304 , 167], [365 , 250, 397 , 185],[368 , 276, 399 , 208]])
#     boundry_pairs_3 = np.array([[262 , 231, 270 , 259], [364 , 252, 366 , 278],[397 , 183, 399 , 210]])
#     opposite_point_2 = np.array([269 , 257])
#     opposite_point_3 = np.array([303 , 165])
#     opposite_point_1 = np.array([399 , 210])
#
# if box is 'cam2':
#     boundry_pairs_1 = np.array([[344 , 139, 409 , 189],[261 , 180, 320 , 234], [264 , 209, 320 , 265]])
#     boundry_pairs_2 = np.array([[320 , 237, 409 , 189], [323 , 265, 410 , 215],[264 , 180, 345 , 140]])
#     boundry_pairs_3 = np.array([[260 , 182, 264 , 208], [322 , 236, 324 , 265],[409 , 189, 411 , 215]])
#     opposite_point_2 = np.array([266 , 210])
#     opposite_point_3 = np.array([343 , 139])
#     opposite_point_1 = np.array([411 , 214])
#
# if box is 'cam3':
#     boundry_pairs_1 = np.array([[303 , 131, 396 , 148],[260 , 193, 364 , 213], [268 , 221, 365 , 241]])
#     boundry_pairs_2 = np.array([[302 , 131, 261 , 193], [365 , 212, 396 , 149],[366 , 238, 400 , 174]])
#     boundry_pairs_3 = np.array([[262 , 193, 269 , 218], [362 , 211, 365 , 238],[397 , 147, 398 , 172]])
#     opposite_point_2 = np.array([268 , 221])
#     opposite_point_3 = np.array([303 , 131])
#     opposite_point_1 = np.array([397 , 172])
#
# if box is 'cam4':
#     boundry_pairs_1 = np.array([[262 , 147, 343 , 113],[311 , 196, 395 , 157], [315 , 222, 398 , 182]])
#     boundry_pairs_2 = np.array([[264 , 170, 314 , 222], [262 , 144, 311 , 193],[342 , 112, 395 , 156]])
#     boundry_pairs_3 = np.array([[262 , 147, 265 , 172], [313 , 195, 315 , 222],[396 , 155, 397 , 182]])
#     opposite_point_2 = np.array([398 , 184])
#     opposite_point_3 = np.array([344 , 112])
#     opposite_point_1 = np.array([267 , 172])

color_1 = (0,0,255)#blue
color_2 = (0,255,0)#green
color_3 = (200,20,20)#red

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


if box is 'TS1_1':
    O_img = cv2.imread('D:/Fraunhoffer_FLW_data/Cube_hidden_corner_prediction/Paper DATA/Results Evaluation/TestSet1/20deg.png')
if box is 'TS1_2':
    O_img = cv2.imread('D:/Fraunhoffer_FLW_data/Cube_hidden_corner_prediction/Paper DATA/Results Evaluation/TestSet1/40deg_w.png')
if box is 'TS1_3':
    O_img = cv2.imread('D:/Fraunhoffer_FLW_data/Cube_hidden_corner_prediction/Paper DATA/Results Evaluation/TestSet1/60deg_w.png')
if box is 'TS1_4':
    O_img = cv2.imread('D:/Fraunhoffer_FLW_data/Cube_hidden_corner_prediction/Paper DATA/Results Evaluation/TestSet1/80deg_w.png')
if box is 'TS1_5':
    O_img = cv2.imread('D:/Fraunhoffer_FLW_data/Cube_hidden_corner_prediction/Paper DATA/Results Evaluation/TestSet1/100deg_w.png')

# if box is 'blend1':
#     O_img = cv2.imread('pictures/Box5/blend1.png')
# if box is 'blend2':
#     O_img = cv2.imread('pictures/Box5/blend2.png')
# if box is 'box1':
#     O_img = cv2.imread('pictures/box3.png')
# if box is 'cam1':
#     O_img = cv2.imread('pictures/cam111.jpg')
# if box is 'cam2':
#     O_img = cv2.imread('pictures/cam11.jpg')
# if box is 'cam3':
#     O_img = cv2.imread('pictures/cam12.jpg')
# if box is 'cam4':
#     O_img = cv2.imread('pictures/cam13.jpg')
# if  box is 'test1':
#     O_img = cv2.imread('pictures/Box1/Picture1.png')
# if  box is 'test3':
#     O_img = cv2.imread('pictures/Box1/Picture3.png')
# if  box is 'test4':
#     O_img = cv2.imread('pictures/Box1/Picture4.png')
# if  box is 'test5':
#     O_img = cv2.imread('pictures/Box1/Picture5.png')
# if  box is 'test6':
#     O_img = cv2.imread('pictures/Box3/Picture1.png')
# if  box is 'test7':
#     O_img = cv2.imread('pictures/Box3/Picture2.png')
# if  box is 'test8':
#     O_img = cv2.imread('pictures/Box3/Picture3.png')
# if  box is 'test9':
#     O_img = cv2.imread('pictures/Box3/Picture4.png')
# if  box is 'test10':
#     O_img = cv2.imread('pictures/Box3/Picture5.png')
# if  box is 'test11':
#     O_img = cv2.imread('pictures/Box3/Picture6.png')

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



cv2.imshow('Boundry lines', O_img)
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


cv2.imshow('Boundry lines', O_img)
cv2.waitKey(0)
cv2.destroyAllWindows()