# Football Analysis Project 

# introduction

This project aims to detect and track players, referees, and footballs in video footage using YOLO, a leading AI-based object detection model. To enhance its performance, we will fine-tune the model through training. In addition, we'll classify players into teams by analyzing the colors of their t-shirts using K-means clustering for pixel segmentation. This approach will allow us to calculate a team's ball possession percentage during a match. We'll also employ optical flow techniques to track camera movements between frames, which will help us accurately measure player movement. By applying perspective transformation, we can represent the scene's depth and perspective, enabling us to convert player movement from pixels to meters. Ultimately, we will calculate the players' speed and the distance they cover. This project integrates various advanced concepts and solves real-world challenges, making it ideal for both beginners and experienced machine learning engineers.

The YOLO (You Only Look Once) model is a state-of-the-art deep learning algorithm designed for real-time object detection. Unlike traditional object detection models that rely on a two-stage process (first identifying regions of interest and then classifying objects within those regions), YOLO uses a single-stage approach. It processes the entire image in one go, making predictions directly for bounding boxes and class probabilities.
Overall, YOLO's combination of speed and accuracy has made it one of the most popular and widely used models for object detection in various applications, including surveillance, autonomous driving, and sports analytics.

![screenshot](https://github.com/user-attachments/assets/7f3b7bc4-614c-4cb5-b8ec-d4aab849dcec)

# modules used
The following modules are used in this project:

- YOLO: AI object detection model
- Kmeans: Pixel segmentation and clustering to detect t-shirt color
- Optical Flow: Measure camera movement
- Perspective Transformation: Represent scene depth and perspective
- Speed and distance calculation per player

# sample video
https://drive.google.com/file/d/1t6agoqggZKx6thamUuPAIdN_1zR9v9S_/view

# Requirements
To run this project, you need to have the following installed:

- Python
- ultralytics
- supervision
- OpenCV
- NumPy
- Matplotlib
- Pandas

