import cv2

# RTSP URL
url = "rtsp://localhost:554/stream"

# RTSP stream
stream = cv2.VideoCapture(url)

# Check if the stream is opened
if not stream.isOpened():
    print("Cannot open the stream")
    exit()

# Read the frames
i = 0
while True:
    ret, frame = stream.read()
    if not ret:
        print("Cannot receive the frame")
        break

    if i == 0:
        print("Frame shape: ", frame.shape)

    if i == 25:
        # save the frame
        cv2.imwrite("tmp/frame.jpg", frame)

        break

    i += 1
