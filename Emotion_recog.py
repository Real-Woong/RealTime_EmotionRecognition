import cv2
from deepface import DeepFace
import numpy as np

def Emotion_Recog(frame, faces, shape="rect") :
    #반복문으로 검출된 얼굴들 순서대로 처리

    for (x, y, w, h) in faces:
        #얼굴부분만 crop 하기 (즉 넓은 종이를 쓸 부분만 자르는 거)
        face_img = frame[y:y+h, x:x+w]

        # -----------------------
        # 1) 도형별 마스크 만들기
        # -----------------------

        masked_face = face_img

        # 형태는 H x W x C 형태의 NumPy (channel은 버림)
        h_face, w_face, _ = face_img.shape

        # 추출한 이미지를 모두 검정색으로 하고 도형에 맞게 흰색부분만 사용할것임
        mask = np.zeros_like(face_img) 

        # 인식 범위 도형별로 나누기
        if shape == "circle":
            #원형
            center = (w_face // 2, h_face // 2)
            radius = min(w_face, h_face) // 2
            cv2.circle(mask, center, radius, (255, 255, 255), -1)
        

        elif shape == "triangle":
            #역삼각형 (위가 넓고 아래가 좁은 형태)
            pt1 = (0, 0) #좌상단
            pt2 = (w_face, 0) #우상단
            pt3 = (w_face // 2, h_face) #하단 중앙
            pts = np.array([pt1, pt2, pt3], np.int32).reshape((-1, 1, 2))
            cv2.fillPoly(mask, [pts], (255, 255, 255))

        elif shape == "rect":
            #사각형이면 전체 사용 (따로 마스크 안 씌워도 되지만 코드의 통일성을 위해)
            mask[:] = (255, 255, 255)
        
        # 마스크 적용 (도형 안쪽만 남기기)
        if shape in ["circle", "triangle", "rect"]:
            masked_face = cv2.bitwise_and(face_img, mask)
        
        # -----------------------
        # 2) DeepFace 감정 분석
        # -----------------------

        try:
            result = DeepFace.analyze(
                face_img,
                actions=['emotion'],
                detector_backend="opencv", # tf_keras 이슈 피하기 (문제해결!!)
                enforce_detection=False
            )

            # DeepFace 결과 형식에 따라 emotion 정보 가져오기
            # 최신 버전은 result가 리스트 형태일 수 있음
            if isinstance(result, list):
                result = result[0]
            
            dominant_emotion = result.get("dominant_emotion", "unknown")

            print(f"log emotion: {dominant_emotion}")

            text_y = max(20, y - 30)

            cv2.putText(
                    frame,
                    dominant_emotion,
                    (x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2
                )
            
        except Exception as e:
            #분석 실패시 그냥 무시
            print("분석 중 오류:", e)


'''
----- 내가 코드 짜다가 햇갈려서 정리한거 -----
1. 도형 모양으로 마스크 만들기
2. 마스크를 얼굴에 적용해 도형 영역만 남기기
3. 그 masked _face 를 DeepFace로 감정 분석
'''