import cv2
import Select_Shape as Ss
import Overlays as Ov
import Emotion_recog as Er

# cv안에 포함된 얼굴 인식기능 (Global)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# 윈도우 이름 (Global)
window_name = "Face Shape Selector"

def main():

    cap = cv2.VideoCapture(1) #기본캠

    if not cap.isOpened():
        print("웹캠을 불러올 수 없습니다")
        return False
    
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, Ss.mouse_callback)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        shape = Ss.selected_shape

        # 1) 아직 얼굴형 선택 전이면 버튼 UI만 그리기 (여기서는 변수 참조해옴)
        if shape is None:
            Ss.draw_buttons(frame)
        
        else:
        # 2) 얼굴형 선택 완료 → 얼굴 검출 + 오버레이 + 감정 분석
        #회색 변환
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 얼굴 탐지
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5
            )

            # 선택된 모양에 따라 다른 오버레이
            if shape == "circle":
                Ov.draw_circle_overlay(frame, faces)
            elif shape == "rect":
                Ov.draw_rect_overlay(frame, faces)
            elif shape == "triangle":
                Ov.draw_triangle_overlay(frame, faces)

            # Er에 있는 변수에 main local 변수 넣기
            Er.Emotion_Recog(frame, faces, shape=shape) 

            # 현재 선택된 얼굴형 안내 텍스트
            cv2.putText(
                frame,
                f"Face shape: {shape}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        # 공통: 프레임 보여주기 + 키 입력
        cv2.imshow(window_name, frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27: #ESC키 누르면 종료
            break

    cap.release()
    cv2.destroyAllWindows()


'''
def frame_circle(frame, faces) :
    for (x, y, w, h) in faces:
        radius = int(w * 0.6)
        face_center = (x + w//2, y + h//2)
        cv2.circle(frame, face_center, radius, (0, 255, 0), 3)
'''

if __name__ == "__main__":
    main()
