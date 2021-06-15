import os

from imageai.Detection.Custom import CustomObjectDetection
import cv2
import matplotlib.pyplot as plt

'''
设置模型为RetinaNet
'''
detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("./detection_model.h5")
detector.setJsonPath("detection_config.json")
detector.loadModel()
filepath = "./identity_card/train/images/"
files = os.listdir(filepath)
for filename in files:
    detections = detector.detectObjectsFromImage(input_image=filepath + filename, output_image_path="output2/" + filename, minimum_percentage_probability=30)
#
# image = cv2.imread('./out_11.jpg')
#
# # 马赛克
# def do_mosaic(frame, x, y, w, h, neighbor=40):
#     """
#     马赛克的实现原理是把图像上某个像素点一定范围邻域内的所有点用邻域内左上像素点的颜色代替，这样可以模糊细节，但是可以保留大体的轮廓。
#     :param frame: opencv frame
#     :param int x :  马赛克左顶点
#     :param int y:  马赛克右顶点
#     :param int w:  马赛克宽
#     :param int h:  马赛克高
#     :param int neighbor:  马赛克每一块的宽
#     """
#     fh, fw = frame.shape[0], frame.shape[1]
#     if (y + h > fh) or (x + w > fw):
#         return
#     for i in range(0, h - neighbor, neighbor):  # 关键点0 减去 neighbour 防止溢出
#         for j in range(0, w - neighbor, neighbor):
#             rect = [j + x, i + y, neighbor, neighbor]
#             color = frame[i + y][j + x].tolist()  # 关键点1 tolist
#             left_up = (rect[0], rect[1])
#             right_down = (rect[0] + neighbor - 1, rect[1] + neighbor - 1)  # 关键点2 减去一个像素
#             cv2.rectangle(frame, left_up, right_down, color, -1)
#
# '''
# 测试
# '''
# for eachObject in detections:
#     print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
#     print('-----------------------')
#     # 左上顶点 [0][1] 右下顶点 [2][3]
#     # image[eachObject["box_points"][1]:eachObject["box_points"][3], eachObject["box_points"][0]:eachObject["box_points"][2]] = (0, 0, 255)
#     if eachObject["name"] == "person":
#         do_mosaic(image, eachObject["box_points"][0], eachObject["box_points"][1], eachObject["box_points"][2] - eachObject["box_points"][0], eachObject["box_points"][3] - eachObject["box_points"][1])
#
# cv2.imwrite("image.jpg", image)
# plt.imshow(image)
# plt.show()