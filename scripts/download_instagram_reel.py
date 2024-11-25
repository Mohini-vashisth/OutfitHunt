import os
from instaloader import Instaloader, Post

def download_instagram_reel(instagram_url, output_path="../downloads"):
    """
    Downloads an Instagram Reel from the provided URL.

    Args:
        instagram_url (str): The URL of the Instagram Reel.
        output_path (str): Directory to save the downloaded Reel.

    Returns:
        str: Path to the downloaded video file.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    try:
        loader = Instaloader()
        shortcode = instagram_url.split("/")[-2]  # Extract shortcode from URL
        post = Post.from_shortcode(loader.context, shortcode)

        print(f"Downloading Reel: {post.title}")
        video_path = os.path.join(output_path, f"{shortcode}.mp4")
        loader.download_post(post, target=output_path)
        print(f"Downloaded Reel to: {output_path}")

        # Find the downloaded video
        for file in os.listdir(output_path):
            if file.endswith(".mp4"):
                return os.path.join(output_path, file)
    except Exception as e:
        print(f"Error downloading Reel: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    reel_url = input("Enter the Instagram Reel URL: ")
    video_path = download_instagram_reel(reel_url)
    print(f"Video saved at: {video_path}")