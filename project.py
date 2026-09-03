from utils import read, write
from trackers import Tracker
from team_assigner import TeamAssigner
import cv2

def main():
    # Read the video
    cap_frames = read("assets/match.mp4")

    tracker = Tracker('models/best.pt')
    tracks = tracker.get_object_tracks(cap_frames, read_from_stub=False,
                                        stub_path='./stubs/track_stubs.pkl')

    tracks["ball"] = tracker.interpolate_ball_position(tracks["ball"])

    # Assigning player teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(cap_frames[0], tracks['players'][0])

    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(cap_frames[frame_num],
                                                  track['bbox'],
                                                    player_id
                                                    )

            tracks['players'][frame_num][player_id]['team'] = team
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_color[team]

    output_video_frames = tracker.draw_annotations(cap_frames,tracks)

    # Save the video
    write(output_video_frames, 'output_videos/out.avi')

if __name__ == '__main__':
    main()