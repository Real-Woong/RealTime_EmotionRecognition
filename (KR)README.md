🧠 Real-Time Facial Emotion Recognition

Python · OpenCV · DeepFace

사용자의 얼굴형(circle/rect/triangle)을 선택하면, 해당 도형에 맞춰 오버레이를 생성하고
실시간으로 얼굴을 인식해 감정을 분석하는 프로젝트입니다.

 📌 Features

 실시간 얼굴 인식 (OpenCV HaarCascade)
 DeepFace 기반 감정 분석
 얼굴형 선택 UI (원형 / 사각형 / 역삼각형)
 도형 오버레이 + 실시간 감정 라벨 표시
 얼굴 크기에 맞춰 도형이 자동 조정
 마스킹 기반 도형별 분석 구조 적용
 

 📘 개발 과정에서 어려웠던 점 & 문제 해결 과정
 

 1. 웹캠 장치 연결 문제

 macOS 환경에서 기본 웹캠이 아니라 휴대폰 카메라(Continuity Camera) 가 자동 연결됨.
 VideoCapture(1) 등 장치 번호를 직접 조정해야 했음.
 카메라 장치가 고정되지 않아 계속 연결이 바뀌는 문제도 발생.
 

 2. DeepFace 설치/실행 오류

 RetinaFace가 TensorFlow 2.20 환경에서 tf-keras 패키지를 요구하여 실행이 중단됨.
 pip install tf-keras 후 해결했지만, RetinaFace 오류가 반복 발생.
 감정 분석 시 detector_backend="opencv" 로 변경해 안정화를 달성.
 

 3. 감정 텍스트가 화면에 출력되지 않는 문제

 발생 원인은 여러 가지가 있었음:
 cv2.FONT_HERSHEY_simplex 오타 → 존재하지 않는 상수라 텍스트 렌더링 실패
 result.get["dominant_emotion"] 잘못된 문법 사용 → 매번 예외 발생
 y - 10이 화면 밖으로 벗어나 텍스트가 보이지 않는 문제
 해결:
   FONT_HERSHEY_SIMPLEX로 수정
   result.get("dominant_emotion", "unknown")으로 변경
   화면 밖으로 벗어나지 않게 y 좌표를 제한하는 로직 추가
   

 4. 도형 오버레이 + 사각형 박스가 동시에 출력되는 문제

 Overlays.py에서 원/삼각형/사각형을 그리고 있었는데
 Emotion_recog.py에서도 rectangle을 또 그려 중복 발생.
 원형 선택 시 → 원 + 사각형이 같이 따라오는 버그가 있었음.
 해결:
   Emotion_recog.py에서는 감정 텍스트만 표시하도록 분리.
   

 5. 파일 분할(모듈화) 과정에서의 이슈

 파일을 아래처럼 나누면서 여러 문제가 생김:
 Select_Shape.py
 Overlays.py
 Emotion_recog.py
 main.py

 문제점:
   전역 변수 selected_shape의 관리가 헷갈리고 값이 갱신되지 않음
   shape = Ss.selected_shape처럼 로컬 변수에 복사하면 선택이 실시간 반영되지 않음
   import 순서/모듈 간 순환 의존성 때문에 혼란 발생
 해결:
   main loop 내에서 Ss.selected_shape를 직접 참조하는 형태로 유지
   각 파일의 역할을 명확히 분리하여 책임 분리
     Select_Shape → UI+선택
     Overlays → 그림 처리
     Emotion_recog → 감정 분석
     main → 전체 플로우
     

 6. 도형 마스킹 기반 감정 분석의 어려움

 얼굴 이미지를 crop 후 도형 마스크 적용(bitwise_and) 과정이 까다로움
 특히 삼각형/원 좌표 계산이 얼굴 bounding box 크기마다 달라져 계산에 어려움
 마스크가 정확히 얼굴 중심에 오도록 좌표 작업을 배웠음


 7. 실시간 성능 지연 문제

 DeepFace는 무거워서 실시간 분석 시 딜레이 발생
 detector_backend 변경, 해상도 축소, 마스크 사용 등을 통해 개선


 📁 Project Structure


📦 Project  
 ├── main.py                 전체 실행 흐름  
 ├── Select_Shape.py         얼굴형 선택 UI  
 ├── Overlays.py             원/사각형/삼각형 오버레이  
 ├── Emotion_recog.py        감정 분석  
 ├── haarcascade_frontalface_default.xml  
 └── README.md  


 🚀 How to Run
 python main.py

필요 패키지 설치:
pip install opencv-python deepface numpy tf-keras


 📝 Author
Jinwoong (진웅)
Python / OpenCV / ML Enthusiast

