# OutfitHunt

OutfitHunt is a machine learning project aimed at identifying clothes in reels and finding matching items from online sources. The model leverages computer vision techniques to analyze video frames and locate visually similar clothing on the internet.

Overview

	•	Goal: Identify outfits from a reel (short video) and match them with similar items available online.
	•	Current State: The foundational model is built to process video frames and extract clothing features.
	•	Future Plans: Enhance the model to include web scraping and integrate a full recommendation pipeline.

Technologies Used
•	Programming Language: Python
•	Libraries:
•	OpenCV: For video processing.
•	TensorFlow / PyTorch: For deep learning and feature extraction.
•	NumPy & Pandas: For data handling.
•	Scikit-learn: For additional ML algorithms.

How to Use

1.	Clone the repository:
• git clone https://github.com/Mohini-vashisth/OutfitHunt.git
• cd OutfitHunt

2.	Install dependencies:
• pip install -r requirements.txt

3.	Process a reel:
• run the scripts/main.py and input reel URL

4.	View the results:
•	The script will generate output frames with detected clothing regions and save them in the output/ folder.
•	Matching items from the web (if implemented) will be displayed in the console or saved as a file.

Folder Structure

OutfitHunt/
│
├── scripts/          # Main script for the model
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
└── ...

Features

•	Clothing Detection: Processes video frames to detect clothing items.
•	Feature Extraction: Identifies key visual attributes (color, pattern, style).
•	Future Integration: Planned integration with web scraping to find matching clothes online.

Future Enhancements

•	Web Scraping Module: Automate searches for matching clothing on e-commerce platforms.
•	Improved Model: Enhance accuracy with larger datasets and pre-trained models.
•	Backend & Frontend: Develop APIs and a user interface for broader usability.

Contact

•	Name: Mohini Vashisth
•	GitHub: github.com/Mohini-vashisth

