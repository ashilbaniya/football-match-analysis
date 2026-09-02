from utils import read, write
from trackers import Tracker
import cv2

def main():
    # Read the video
    cap_frames = read("assets/match.mp4")

    tracker = Tracker('models/best.pt')
    tracks = tracker.get_object_tracks(cap_frames, read_from_stub=True,
                                        stub_path='./stubs/track_stubs.pkl')

    # Cropping a player out of a frame
    # for track_id, player in tracks["players"][0].items():
    #     bbox = player['bbox']
    #     frame = cap_frames[0]

    #     cropped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]

    #     # Saving the cropped image
    #     cv2.imwrite(f'cropped_images/image_{track_id}.png', cropped_image)

    #     break

    output_video_frames = tracker.draw_annotations(cap_frames,tracks)

    # Save the video
    write(output_video_frames, 'output_videos/out.avi')

if __name__ == '__main__':
    main()