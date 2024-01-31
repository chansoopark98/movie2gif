from moviepy.editor import VideoFileClip
import os

def convert_video_to_gif(input_video_path, output_gif_path, fps=10, resolution=None, start_time=0, end_time=None):
    clip = VideoFileClip(input_video_path)

    if end_time:
        clip = clip.subclip(start_time, end_time)
    else:
        clip = clip.subclip(start_time)

    if resolution:
        clip = clip.resize(resolution)

    clip.write_gif(output_gif_path, fps=fps, program='ffmpeg', loop=-1)

# 사용자 입력 받기
input_video_path = input("비디오 파일 경로를 입력하세요: (예: my_video.mp4) :  ")
output_gif_path = input("출력될 GIF 파일 이름을 입력하세요 (예: my_gif.gif) :  ")
fps = int(input("프레임 속도를 입력하세요 (기본값 30):  ") or "30")
start_time = int(input("시작 시간을 초 단위로 입력하세요 (기본값 0):  ") or "0")
end_time = input("종료 시간을 초 단위로 입력하세요 (기본값은 비디오 끝까지):  ")
end_time = int(end_time) if end_time else None
resolution = float(input("해상도 조정 비율을 입력하세요 (예: 0.5, 기본값은 변경 없음):  "))

convert_video_to_gif(input_video_path, output_gif_path, fps=fps, resolution=resolution, start_time=start_time, end_time=end_time)