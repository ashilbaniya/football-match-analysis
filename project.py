from utils import read, write
from trackers import Tracker
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner
from camera_movement_estimator import CameraMovementEstimator
from view_transformer import ViewTransformer
from speed_and_distance_estimator import SpeedAndDistanceEstimator
import numpy as np
import argparse
import textwrap

def main():
    # Read the video
    cap_frames = read(f"assets/{args.read}")        

    tracker = Tracker('models/best.pt')
    tracks = tracker.get_object_tracks(cap_frames, read_from_stub=True,
                                        stub_path='./stubs/track_stubs.pkl')

    # Get object positions
    tracker.add_position_to_tracks(tracks)


    # camera movement estimator
    camera_movement_estimator = CameraMovementEstimator(cap_frames[0])
    camera_movement_per_frame = camera_movement_estimator.get_camera_movement(cap_frames,
                                                                           read_from_stub=True,
                                                                           stub_path='./stubs/camera_movement_stub.pkl')

    camera_movement_estimator.add_adjust_positions_to_tracks(tracks, camera_movement_per_frame)

    # View Transformer
    view_transformer = ViewTransformer()
    view_transformer.add_transformed_position_to_tracks(tracks)

    tracks["ball"] = tracker.interpolate_ball_position(tracks["ball"])

    # Speed and Distance Estimator
    speed_and_distance_estimator = SpeedAndDistanceEstimator()
    speed_and_distance_estimator.add_speed_and_distance_to_tracks(tracks)

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

    # Draw camera movements
    output_video_frames = camera_movement_estimator.draw_camera_movement(output_video_frames, camera_movement_per_frame)

    # Draw speed and distance
    output_video_frames = speed_and_distance_estimator.draw_speed_and_distance(output_video_frames, tracks)

    # Save the video
    write(output_video_frames, f'output_videos/{args.write}')
    print("Program execucted successfully.")
    print(f"Output saved to 'output_videos/{args.write}.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='Football Analysis Tool',
                    description="This is a football analysis tool made using YOLO and opencv",
                    formatter_class=argparse.RawDescriptionHelpFormatter,
                    epilog=textwrap.dedent('''Example: 
python project.py -r input.mp4 -w output.mp4        # read from input.mp4 and then write the results in output.mp4
Check out "https://github.com/ashilbaniya/football-match-analysis" for more information.
'''
                    ))
    parser.add_argument("-r", "--read", required=True, help="read from the given video path")
    parser.add_argument("-w", "--write", required=True, help="write the results to the given path.")

    args = parser.parse_args()

    main()
