import os


# List of directories/paths
root = "/Users/alessiadisanto/Desktop/TESI/py/venv/"

# QR code directory timestamp
path_dir_qr = root + 'qr'

# Frame directory
path_dir_img = root + 'frames-nots'

# Frame with timestamp directory
path_dir_ts = root + 'frames-ts'

path_dir_rf = root + 'frames_received'

# New video from frame with timestamp directory
path_dir_video = root + 'videos/'

# Encoded video name
video_rf = 'received_video.mp4'

# Folder file
path_file = root + "files/"

# File timestamp rx
file_rx = path_file + 'rx'

# Mode, mean and variance
path_statistics = root + "statistics/"
var = path_statistics + "variance"
mean = path_statistics + "mean"

# Directory with plots
path_dir_plots = root + "plots/"

# Message to terminate communication
stop_msg = b'stop'


# Function used to create a new directory
def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"Error: creating directory {path}")
