import cv2

def read(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        _, frame = cap.read()
        if not _:
            break
        frames.append(frame)
    return frames

def write(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()