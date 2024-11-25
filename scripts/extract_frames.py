import cv2
import os
from download_instagram_reel import download_instagram_reel

def extract_frames(video_path, output_dir="../frames", frame_rate=1):
    """
    Extracts frames from a video file.

    Args:
        video_path (str): Path to the video file.
        output_dir (str): Directory to save frames.
        frame_rate (int): Save one frame every `frame_rate` frames.

    Returns:
        List[str]: Paths to the saved frame images.
    """
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    frame_number = 0
    saved_frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_number % frame_rate == 0:  # Save every nth frame
            frame_path = os.path.join(output_dir, f"frame_{frame_number:04d}.jpg")
            cv2.imwrite(frame_path, frame)
            saved_frames.append(frame_path)
        frame_number += 1

    cap.release()
    print(f"Extracted {len(saved_frames)} frames to {output_dir}")
    return saved_frames

if __name__ == "__main__":
    reel_url = input("Enter the Instagram Reel URL: ")
    video_path = download_instagram_reel(reel_url)
    if video_path:
        extract_frames(video_path)