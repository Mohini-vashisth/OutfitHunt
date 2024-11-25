import os
import torch

def detect_clothing(frame_dir, output_dir="../detections"):
    """
    Detects clothing items in frames using YOLOv5.

    Args:
        frame_dir (str): Directory with input frames.
        output_dir (str): Directory to save detection results.
    """
    os.makedirs(output_dir, exist_ok=True)
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # YOLOv5 small model
    images = [os.path.join(frame_dir, img) for img in os.listdir(frame_dir) if img.endswith('.jpg')]
    
    results = model(images)
    results.save(output_dir)
    print(f"Detections saved to {output_dir}")

from transformers import CLIPProcessor, CLIPModel
from PIL import Image

def extract_features(image_path):
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    image = Image.open(image_path)
    inputs = processor(text=["clothing"], images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    return outputs.pooler_output

if __name__ == "__main__":
    detect_clothing("../frames")