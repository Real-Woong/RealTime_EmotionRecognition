import cv2
import numpy as np

def draw_circle_overlay(frame, faces):
    # print("circle overlay called") 호출 확인용
    for (x, y, w, h) in faces:
        radius = int(w * 0.6)
        radius = max(20, radius)
        center = (x + w // 2, y + h // 2)
        cv2.circle(frame, center, radius, (0, 255, 0), 3)


def draw_rect_overlay(frame, faces):
    # print("rect overlay called") 호출 확인용
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


def draw_triangle_overlay(frame, faces):
    # print("triangle overlay called") 호출 확인용
    for (x, y, w, h) in faces:
        # 역삼각형: 위에 긴 변, 아래에 꼭짓점
        pt1 = (x, y)             # 좌상단
        pt2 = (x + w, y)         # 우상단
        pt3 = (x + w // 2, y + h)  # 하단 중앙

        pts = np.array([pt1, pt2, pt3], np.int32).reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 255, 0), 3)