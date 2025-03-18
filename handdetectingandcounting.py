import cv2

# HOG (Histogram of Oriented Gradients) tanımlayıcısını ve insan algılayıcıyı başlat
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Kameradan video yakalama
cap = cv2.VideoCapture(0)

counter = 0  # Sayaç başlangıç değeri
line_position = 0  # Çizgi pozisyonu (bu değişken kullanılmıyor, kaldırılabilir)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Çerçevede insanları algıla
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    boxes, weights = hog.detectMultiScale(gray, winStride=(8, 8))

    # Sabit çizgiyi çiz
    cv2.line(frame, (frame.shape[1] // 2, 0), (frame.shape[1] // 2, frame.shape[0]), (0, 0, 255), 2)

    # Herhangi bir insan çizgiyi geçiyor mu kontrol et
    for (x, y, w, h) in boxes:
        if x + w // 2 > frame.shape[1] // 2:
            counter += 1
            break

    # Çerçeveye sayaç değerini ekle
    cv2.putText(frame, f"sayac : {counter}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Çerçeveyi göster
    cv2.imshow('Frame', frame)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Kamerayı ve pencereleri serbest bırak
cap.release()
cv2.destroyAllWindows()
