from ultralytics import YOLO

model = YOLO("models/best.pt")

result = model.predict('./assets/match.mp4', save=True, stream=True)
print(result[0])
print("=================================")
for box in result[0].boxes:
    print(box)
print("=================================")