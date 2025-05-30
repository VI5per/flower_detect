import torch
import cv2
import os

# Load model YOLOv5 custom (deteksi bunga)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='flower_07042022.pt')

# Path gambar
image_path = r'' #(ganti sesuai tempat directori file\nama_gambar_yg_dideteksi.jpg)

# Periksa apakah gambar tersedia
if not os.path.exists(image_path):
    print(f"[!] Gambar tidak ditemukan: {image_path}")
    exit()

# Baca gambar dengan OpenCV
img = cv2.imread(image_path)

# Jalankan deteksi
results = model(img)

# Ambil anotasi deteksi
for *box, conf, cls in results.xyxy[0]:
    x1, y1, x2, y2 = map(int, box)
    label = model.names[int(cls)]
    conf_text = f"{label} {conf:.2f}"
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(img, conf_text, (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Tampilkan hasil
cv2.imshow("Deteksi Bunga", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
