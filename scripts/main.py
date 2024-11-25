from download_instagram_reel import download_instagram_reel
from extract_frames import extract_frames
from detect_clothing import detect_clothing

if __name__ == "__main__":
    reel_url = input("Enter Instagram Reel URL: ")
    video_path = download_instagram_reel(reel_url)
    
    if video_path:
        frame_dir = "../frames"
        extract_frames(video_path, frame_dir)
        
        detect_clothing(frame_dir)
        print("Pipeline completed!")