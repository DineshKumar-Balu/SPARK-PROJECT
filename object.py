import cv2

def extract_frames(video_path, output_dir):
    # Read video file
    video = cv2.VideoCapture(r"C:\Users\DINESH 07\Downloads\TEAM-SPARK\AUTO_IN_20230503083000_20230503085941_173581725.mp4")
    frame_number = 0

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Save frame as an image
        frame_path = f"{output_dir}/frame_{frame_number}.jpg"
        cv2.imwrite(frame_path, frame)
        print(f"Saved {frame_path}")

        frame_number += 1

    # Release resources
    video.release()

if __name__ == "__main__":
    video_path = r"C:\Users\DINESH 07\Downloads\TEAM-SPARK\AUTO_IN_20230503083000_20230503085941_173581725.mp4"  # Replace with your video file path
    output_directory = r"C:\Users\DINESH 07\Downloads\TEAM-SPARK\output-files"  # Replace with the directory where you want to save the frames

    extract_frames(video_path, output_directory)
