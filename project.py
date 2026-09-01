from ultralytics import YOLO

model = YOLO("yolov8m.pt")

result = model.predict('./assets/match.mp4', save=True)

print(result)