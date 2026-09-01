from ultralytics import YOLO
import supervision as sv

class Tracker:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()

    def detect_frames(self, frames):
        batch_size = 20
        detections = []
        for i in range(0, len(frames), batch_size):
            detection_batch = self.model.predict(frames[i:i+batch_size],conf=0.1)
            detections += detection_batch
            break

        return detections

    def get_object_tracks(self, frames):
        detections = self.detect_frames(frames)

        for _, detection in enumerate(detections):
            cls_names = detection.names
            cls_names_inv = {v:k for k,v in cls_names.items()}

        # Convert it to supervision detection
            detections_supervision = sv.Detections.from_ultralytics(detection)

        # Convert the goalkeeper object to a player object
            for obj_ind, class_id in enumerate(detections_supervision.class_id):
                if cls_names[class_id] == "goalkeeper":
                    detections_supervision.class_id[obj_ind] = cls_names_inv["player"]

            print(detections_supervision.class_id)
            break
            