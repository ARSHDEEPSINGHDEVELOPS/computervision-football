import os
from ultralytics import YOLO 

# Load the model
model = YOLO('yolov8x')

# Define the input video path
input_video_path = r"C:\Users\arsh\Desktop\projects\computer vision\10sec.mp4"

# Define the output directory (same as the input directory)
output_directory = r"C:\Users\arsh\Desktop\projects\computer vision"

# Perform prediction and save the results
results = model.predict(input_video_path, save=True, save_dir=output_directory)

# Print the results for the first frame
print(results[0])
print('=====================================')

# Print the bounding boxes for the first frame
for box in results[0].boxes:
    print(box)

# Rename the output video to .mp4
avi_output_path = os.path.join(output_directory, '10sec_avi.avi')
mp4_output_path = os.path.join(output_directory, '10sec_output.mp4')

if os.path.exists(avi_output_path):
    os.rename(avi_output_path, mp4_output_path)
    print(f"Output video saved as {mp4_output_path}")
else:
    print("Output video not found.")
