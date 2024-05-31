import cv2

# Завантаження класифікатора для облич людей
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Відкриття відео потоку з веб-камери
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Не вдалося відкрити відео потік")
    exit()

while True:
    # Зчитування кадру
    ret, frame = cap.read()
    if not ret:
        print("Не вдалося прочитати кадр")
        break

    # Перетворення кадру у відтінки сірого (це покращує роботу класифікатора)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Знаходження облич у кадрі
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Відображення кадру з обличами
    cv2.imshow('Face Detection', frame)

    # Відслідковування натискання клавіші "q" для виходу з циклу
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Закриття відео потоку та вікна
cap.release()
cv2.destroyAllWindows()
