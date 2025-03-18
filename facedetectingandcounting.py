import cv2

# Haar Cascade yüz algılayıcıyı yükle
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def open_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    counter = 0  # Sayaç başlangıç değeri
    face_detected = False  # Yüz algılandı mı kontrolü
    face_on_right = False  # Yüz sağda mı kontrolü

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Çerçevede yüzleri algıla
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        height, width, _ = frame.shape
        top_center = (width // 2, 0)
        bottom_center = (width // 2, height)
        cv2.line(frame, top_center, bottom_center, (0, 0, 255), 2)

        # Herhangi bir yüz çizgiyi geçiyor mu kontrol et
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                face_center_x = x + w // 2
                if face_center_x > width // 2:
                    if not face_detected and not face_on_right:
                        counter += 1
                        face_detected = True
                        face_on_right = True
                    break
                elif face_center_x < width // 2:
                    if not face_detected and face_on_right:
                        counter -= 1
                        face_detected = True
                        face_on_right = False
                    break
        else:
            face_detected = False

        # Çerçeveye sayaç değerini ekle
        cv2.putText(frame, f"sayac : {counter}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_camera()
