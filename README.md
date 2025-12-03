 🧠 Real-Time Facial Emotion Recognition

Python · OpenCV · DeepFace

사용자의 얼굴형(circle/rect/triangle)을 선택하면, 해당 도형에 맞춰 오버레이를 생성하고
실시간으로 얼굴을 인식해 감정을 분석하는 프로젝트입니다.

---

 📌 Features (Korean)

 실시간 얼굴 인식 (OpenCV HaarCascade)
 DeepFace 기반 감정 분석
 얼굴형 선택 UI (원형 / 사각형 / 역삼각형)
 도형 오버레이 + 실시간 감정 라벨 표시
 얼굴 크기에 맞춰 도형 자동 조정
 도형별 마스킹 기반 감정 분석

---

 📘 개발 과정에서 어려웠던 점 & 문제 해결 과정 (Korean)

 1. 웹캠 장치 연결 문제

macOS 환경에서 기본 캠 대신 Continuity Camera(휴대폰 카메라) 가 자동 연결되는 문제 발생.
`VideoCapture(1)`로 장치를 직접 바꾸어 해결.

---

 2. DeepFace 실행 오류

RetinaFace가 TensorFlow 2.20+에서 tf-keras를 요구하며 실행이 중단됨.
`pip install tf-keras` 및 `detector_backend="opencv"`로 해결.

---

 3. 감정 텍스트가 출력되지 않는 문제

 `FONT_HERSHEY_simplex` 오타
 `result.get[...]` 잘못된 문법
 텍스트가 화면 밖(y < 0)으로 벗어남
  → 모두 수정하여 정상 작동.

---

 4. 도형 + 사각형 중복 출력

Overlays.py와 Emotion_recog.py가 모두 박스를 그려
원형 선택 시 “원 + 사각형”이 함께 출력되는 문제 발생.
→ Emotion_recog에서는 텍스트만 출력하도록 분리.

---

 5. 파일 분할 시 전역 변수 이슈

`selected_shape`가 모듈 간 동기화되지 않아 shape 선택이 반영되지 않는 문제 발생.
→ main loop에서 매번 Ss.selected_shape를 직접 읽어 해결.

---

 6. 도형 마스크 생성의 복잡함

bitwise_and, 도형 좌표 계산 등 예상보다 까다로웠음.
얼굴 bounding box에 따라 중심을 자동 계산해 문제 해결.

---

 7. DeepFace 실시간 성능 문제

딜레이가 심해지며 실시간 분석 어려움.
→ detector_backend 변경 및 이미지 크기 최적화로 개선.

---

 📁 Project Structure (Korean)

```
📦 Project  
 ├── main.py                 전체 실행 흐름  
 ├── Select_Shape.py         얼굴형 선택 UI  
 ├── Overlays.py             도형 오버레이  
 ├── Emotion_recog.py        감정 분석  
 ├── haarcascade_frontalface_default.xml  
 └── README.md  
```

---

 🚀 실행 방법 (Korean)

```bash
pip install opencv-python deepface numpy tf-keras
python main.py
```

---

 🌍 English Version

(English README for international users)

---

 🧠 Real-Time Facial Emotion Recognition

Python · OpenCV · DeepFace

This project detects faces in real-time, analyzes emotions using DeepFace,
and overlays a user-selected face shape (circle, rectangle, triangle) on top of the detected face.

---

 📌 Features (English)

 Real-time face detection using OpenCV HaarCascade
 Emotion analysis via DeepFace
 Face-shape selection UI (circle / rectangle / triangle)
 Dynamic shape overlays that follow the user’s face
 Emotion labels displayed in real time
 Shape-based masking for more accurate emotion extraction

---

 📘 Challenges & What I Learned (English)

 1. Webcam Device Issues (macOS)

macOS kept connecting the webcam to Continuity Camera (iPhone) instead of the built-in camera.
Solved by manually switching devices (e.g., `VideoCapture(1)`).

---

 2. DeepFace & TensorFlow Errors

RetinaFace required tf-keras, causing runtime errors.
Installing `tf-keras` and switching to `detector_backend="opencv"` resolved the issue.

---

 3. Emotion Text Not Rendering

Issues included:

 Wrong font constant (`FONT_HERSHEY_simplex`)
 Incorrect dictionary access (`result.get[...]`)
 Text printed outside the frame when y < 0

After fixing these, the emotion labels displayed correctly.

---

 4. Duplicate Overlays (Circle + Rectangle Bug)

Both Overlays.py and Emotion_recog.py were drawing shapes,
causing a circle overlay + rectangle box to appear simultaneously.
Fix: Emotion_recog now only draws emotion text.

---

 5. Global Variable Sync Issues During Modularization

`selected_shape` stored in Select_Shape.py was not updating inside main.py
when assigned to a local variable.
Solution: always reference `Ss.selected_shape` directly in the loop.

---

 6. Complex Shape Masking Calculations

Creating round/triangle masks required precise coordinate calculations.
Solved by computing dynamic centers and radii based on face bounding box.

---

 7. Real-Time Performance Limitations

DeepFace is heavy → noticeable delay in real-time processing.
Detector backend adjustments and frame optimization improved performance.

---

 📁 Project Structure (English)

```
📦 Project  
 ├── main.py                 Main program loop  
 ├── Select_Shape.py         Shape selection UI  
 ├── Overlays.py             Shape overlays  
 ├── Emotion_recog.py        Emotion recognition module  
 ├── haarcascade_frontalface_default.xml  
 └── README.md  
```

---

 🚀 How to Run (English)

```bash
pip install opencv-python deepface numpy tf-keras
python main.py
```

---

 ✨ Author

Jinwoong (진웅)
Python · OpenCV · Machine Learning Enthusiast
