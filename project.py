from utils import read, write
from trackers import Tracker
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner
import numpy as np
import cv2

def main():
    # Read the video
    cap_frames = read("assets/match.mp4")

    tracker = Tracker('models/best.pt')
    tracks = tracker.get_object_tracks(cap_frames, read_from_stub=True,
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

    # Assigning ball acquisition
    player_assigner = PlayerBallAssigner()
    team_ball_control = []

    for frame_num, player_track in enumerate(tracks['players']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

        if assigned_player != -1:
            tracks['players'][frame_num][assigned_player]['has_ball'] = True
            team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
        else:
            team_ball_control.append(team_ball_control[-1])

    team_ball_control = np.array(team_ball_control)

    output_video_frames = tracker.draw_annotations(cap_frames,tracks,team_ball_control)

    # Save the video
    write(output_video_frames, 'output_videos/out.avi')

if __name__ == '__main__':
    main()