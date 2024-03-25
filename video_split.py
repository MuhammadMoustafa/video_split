from moviepy.editor import VideoFileClip

class SplitInfo:
    def __init__(self, start_time:float, end_time:float, filename:str=""):
        self.start_time = start_time
        self.end_time = end_time
        self.filename = filename

def split_video(video_path: str, split_info_list: list[SplitInfo]) -> None:
    video = VideoFileClip(video_path)    
    total_duration = video.duration
    start_time = 0.0
    for split_info in split_info_list:
        start_time = split_info.start_time
        end_time = min(split_info.end_time, total_duration)
        assert(start_time < total_duration)
        assert(start_time < end_time)
        filename = split_info.filename or f"subclip_{start_time}_{end_time}.mp4"
        subclip = video.subclip(start_time, end_time)
        subclip.write_videofile(filename)
        
    video.close()


if __name__ == "__main__":
    # Example usage
    video_path = "input_video.mp4"
    split_info_list = [
        SplitInfo(start_time=1, end_time=3, filename='subclip_1_3.mp4'),
        SplitInfo(start_time=7.5, end_time=9, filename='subclip_7_8.mp4'),
        SplitInfo(start_time=10, end_time=30, filename='')
    ]
    split_video(video_path, split_info_list)
