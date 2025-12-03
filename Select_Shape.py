import cv2

# 전역 상태
selected_shape = None # "circle", "rect", "triangle"

#UI 설계
button_areas = {
    "circle": ((50,30), (200, 90)),
    "rect": ((230, 30), (380, 90)),
    "triangle": ((410, 30), (600, 90))
}

def mouse_callback(event, x, y, flags, param):
    
    """
    마우스로 버튼 클릭했을 때 selected_shape를 설정하는 콜백
    """

    global selected_shape

    # 아직 선택 안 된 상태에서만 클릭 처리
    if event == cv2.EVENT_FLAG_LBUTTON and selected_shape is None:
            for shape, ((x1, y1), (x2, y2)) in button_areas.items():
                if x1 <= x <= x2 and y1 <= y <= y2:
                    selected_shape = shape
                    print(f"[INFO] 선택된 얼굴형 : {shape}")
                    break

def draw_buttons(frame):

    """
    처음 화면에서 얼굴형 선택 버튼(동그라미/네모/역삼각형) 그리기
    """

    for shape, ((x1, y1), (x2, y2)) in button_areas.items():
        #버튼 박스
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        #텍스트
        if shape == "circle":
            label = "Round (Circle)"
        elif shape == "rect":
            label = "Angular (Rect)"
        else:
            label = "V-shape (Triangle)"

        cv2.putText(
            frame,
            label,
            (x1 + 5, y1 + 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    #안내 문구
    cv2.putText(
        frame,
        "Select your face shape by clicking a box",
        (50, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )