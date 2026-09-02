from utils import read, write
from trackers import Tracker

def main():
    # Read the video
    cap_frames = read("assets/match.mp4")

    tracker = Tracker('models/best.pt')
    tracks = tracker.get_object_tracks(cap_frames, read_from_stub=True,
                                        stub_path='./stubs/track_stubs.pkl')

    output_video_frames = tracker.draw_annotations(cap_frames,tracks)

    # Save the video
    write(output_video_frames, 'output_videos/out.avi')

if __name__ == '__main__':
    main()