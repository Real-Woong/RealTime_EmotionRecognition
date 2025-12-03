# 🧠 Real-Time Facial Emotion Recognition

Python · OpenCV · DeepFace

This project detects faces in real-time, analyzes emotions using DeepFace,
and overlays a user-selected face shape (circle, rectangle, triangle) on top of the detected face.

---

## 📌 Features (English)

* Real-time face detection using OpenCV HaarCascade
* Emotion analysis via DeepFace
* Face-shape selection UI (circle / rectangle / triangle)
* Dynamic shape overlays that track the user’s face
* Emotion labels displayed in real time
* Shape-based masking for more accurate emotion extraction

---

## 📘 Challenges & What I Learned (English)

### 1. Webcam Device Issues (macOS)

macOS often connected the webcam to **Continuity Camera (iPhone)** instead of the MacBook’s built-in camera.
Solved by manually specifying the device index (e.g., `VideoCapture(1)`).

---

### 2. DeepFace & TensorFlow Errors

RetinaFace required **tf-keras**, causing runtime errors on TensorFlow 2.20+.
Fix: install `tf-keras` and switch to `detector_backend="opencv"` for stability.

---

### 3. Emotion Text Not Rendering

Errors caused by:

* Wrong font constant (`FONT_HERSHEY_simplex`)
* Incorrect dictionary access (`result.get[...]`)
* Text going out of frame due to negative y-coordinates

Fixed by correcting the API usage and adding bounds checks for text position.

---

### 4. Duplicate Overlays (Circle + Rectangle Overlap)

Both Overlays.py and Emotion_recog.py were drawing shape frames,
causing unintended double rendering (e.g., circle + rectangle).
Solution: Only Overlays.py handles drawing shapes; Emotion_recog draws text only.

---

### 5. Global Variable Sync Issues During Modularization

`selected_shape` was not updating properly when assigned locally in main.py.
Now the main loop references `Ss.selected_shape` directly to maintain consistency.

---

### 6. Complex Shape Masking Calculations

Shape masks (circle/triangle) required precise coordinate math.
Solved by dynamically calculating centers and dimensions from the face bounding box.

---

### 7. Real-Time Performance Limitations

DeepFace is heavy and caused noticeable lag.
Improved performance by switching backends and optimizing frame operations.

---

## 📁 Project Structure (English)

```
📦 Project  
 ├── main.py                # Main program loop  
 ├── Select_Shape.py        # Shape selection UI  
 ├── Overlays.py            # Shape overlay rendering  
 ├── Emotion_recog.py       # Emotion recognition module  
 ├── haarcascade_frontalface_default.xml  
 └── README.md  
```

---

## 🚀 How to Run (English)

```bash
pip install opencv-python deepface numpy tf-keras
python main.py
```

---
---
---

# 🇰🇷 한국어 버전 For Korean Readers

(한국 사용자용 README)

---

# 🧠 실시간 얼굴 감정 인식 프로젝트

Python · OpenCV · DeepFace

사용자의 얼굴형(circle/rect/triangle)을 선택하면,
해당 도형에 맞춰 오버레이가 적용되고
DeepFace로 실시간 감정 분석을 수행하는 프로젝트입니다.

---

## 📌 기능 (한국어)

* 실시간 얼굴 인식(OpenCV HaarCascade)
* DeepFace 기반 감정 분석
* 얼굴형 선택 UI (원형 / 사각형 / 역삼각형)
* 얼굴을 따라다니는 동적 오버레이
* 실시간 감정 라벨 표시
* 도형별 마스크 기반 감정 분석

---

## 📘 개발 과정에서 어려웠던 점 & 해결 과정 (한국어)

### 1. 웹캠 장치 연결 문제

macOS 환경에서 기본 웹캠 대신 **Continuity Camera(아이폰 카메라)** 가 우선 연결됨.
`VideoCapture(1)` 같은 장치 번호 지정으로 해결.

---

### 2. DeepFace 실행 오류

RetinaFace가 TensorFlow 2.20 이상에서 **tf-keras 패키지를 요구**하며 실행 중단.
`pip install tf-keras` + `detector_backend="opencv"`로 문제 해결.

---

### 3. 감정 텍스트가 출력되지 않는 문제

* 오타(`FONT_HERSHEY_simplex`)
* 잘못된 dictionary 접근(`result.get[...]`)
* 텍스트가 y < 0 으로 벗어나 화면 밖으로 사라짐
  → 전부 수정하여 정상 출력되도록 개선.

---

### 4. 도형 및 사각형 프레임 중복 출력

Overlays.py와 Emotion_recog.py가 둘 다 프레임을 그리면서
원형 선택 시 “원 + 사각형”이 동시에 출력되는 문제 발생.
Emotion_recog.py에서는 텍스트만 그리도록 분리해서 해결.

---

### 5. 파일 분할 시 전역 변수 문제

`selected_shape`가 main.py에서 로컬 변수로 복사되면 업데이트가 반영되지 않는 문제 발생.
main loop에서 항상 **Ss.selected_shape**를 직접 사용하도록 수정.

---

### 6. 도형 마스킹 구현의 복잡함

삼각형·원 마스크를 만들 때 좌표 계산과 bitwise 연산이 까다로웠음.
bounding box 기준으로 중심/반지름을 자동 계산하는 방식으로 해결.

---

### 7. 실시간 DeepFace 성능 지연

DeepFace가 무거워 실시간 속도가 느려짐.
백엔드 전환 및 프레임 최적화를 통해 성능 개선.

---

## 📁 프로젝트 구조 (한국어)

```
📦 Project  
 ├── main.py                # 전체 실행 루프  
 ├── Select_Shape.py        # 얼굴형 선택 UI  
 ├── Overlays.py            # 도형 오버레이  
 ├── Emotion_recog.py       # 감정 분석  
 ├── haarcascade_frontalface_default.xml  
 └── README.md  
```

---

## 🚀 실행 방법 (한국어)

```bash
pip install opencv-python deepface numpy tf-keras
python main.py
```

---

# ✨ Author

**Jinwoong (진웅)**
Python · OpenCV · Machine Learning Enthusiast

