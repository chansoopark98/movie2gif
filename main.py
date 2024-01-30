from moviepy.editor import VideoFileClip
import PIL

def convert_video_to_gif(input_video_path, output_gif_path, fps=10, resolution=None, start_time=0, end_time=None):
    # 비디오 파일을 로드합니다
    clip = VideoFileClip(input_video_path)

    # 선택적으로 비디오의 특정 부분을 자를 수 있습니다
    if end_time:
        clip = clip.subclip(start_time, end_time)
    else:
        clip = clip.subclip(start_time)

    # 해상도 조정 (예: (width, height))
    if resolution:
        clip = clip.resize(0.5)

    # GIF로 변환하며 프레임 속도를 설정합니다
    clip.write_gif(output_gif_path, fps=fps, program='ffmpeg')    

# 사용 예제
convert_video_to_gif("output.mp4", "output.gif", fps=25, resolution=0.5, start_time=25, end_time=32)