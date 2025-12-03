🧠 Real-Time Facial Emotion Recognition

Python · OpenCV · DeepFace

This project detects faces in real-time, analyzes emotions using DeepFace,
and overlays a user-selected face shape (circle, rectangle, triangle) on top of the detected face.

📌 Features (English)

  - Real-time face detection using OpenCV HaarCascade
  - Emotion analysis via DeepFace
  - Face-shape selection UI (circle / rectangle / triangle)
  - Dynamic shape overlays that follow the user’s face
  - Emotion labels displayed in real time
  - Shape-based masking for more accurate emotion extraction
  

📘 Challenges & What I Learned

  
1. Webcam Device Issues (macOS)

  macOS kept connecting the webcam to Continuity Camera (iPhone) instead of the built-in camera.
  Solved by manually switching devices (e.g., VideoCapture(1)).
  

2. DeepFace & TensorFlow Errors

  RetinaFace required tf-keras, causing runtime errors.
  Installing tf-keras and switching to detector_backend="opencv" resolved the issue.


3. Emotion Text Not Rendering

  Issues included:
    Wrong font constant (FONT_HERSHEY_simplex)
    Incorrect dictionary access (result.get[...])
    Text printed outside the frame when y < 0
  
  After fixing these, the emotion labels displayed correctly.


4. Duplicate Overlays (Circle + Rectangle Bug)

  Both Overlays.py and Emotion_recog.py were drawing shapes,
  causing a circle overlay + rectangle box to appear simultaneously.
  Fix: Emotion_recog now only draws emotion text.


5. Global Variable Sync Issues During Modularization

  selected_shape stored in Select_Shape.py was not updating inside main.py
  when assigned to a local variable.
  Solution: always reference Ss.selected_shape directly in the loop.
  

6. Complex Shape Masking Calculations

  Creating round/triangle masks required precise coordinate calculations.
  Solved by computing dynamic centers and radii based on face bounding box.
  

7. Real-Time Performance Limitations

  DeepFace is heavy → noticeable delay in real-time processing.
  Detector backend adjustments and frame optimization improved performance.


📁 Project Structure
  📦 Project  
   ├── main.py                # Main program loop  
   ├── Select_Shape.py        # Shape selection UI  
   ├── Overlays.py            # Shape overlays  
   ├── Emotion_recog.py       # Emotion recognition module  
   ├── haarcascade_frontalface_default.xml  
   └── README.md


🚀 How to Run
  pip install opencv-python deepface numpy tf-keras
  python main.py


✨ Author
Jinwoong (진웅)
Python · OpenCV · Machine Learning Enthusiast
