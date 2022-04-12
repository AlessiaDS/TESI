import cv2
import time
import os
import qrcode
from PIL import Image
import paths_directory


class encoder:

    def __init__(self, frame):
        self.frame = frame

    # Function used to create a timestamp as QR code
    def getQr(self, count, timestamp):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(str(timestamp))
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        with open(paths_directory.path_dir_qr + "/" + (str(count) + ".jpg"), 'wb') as f:
            qr_img.save(f)

    # Function used to overlay in a specific position the frame and its timestamp
    def pasteImages(self, count):
        # Opening the primary image (used in background)
        img1 = Image.open(paths_directory.path_dir_img + "/" + (str(count) + ".jpg"))
        resized_img1 = img1.resize((350, 210))
        # Opening the secondary image (overlay image)
        img2 = Image.open(paths_directory.path_dir_qr + "/" + (str(count) + ".jpg"))
        resized_img2 = img2.resize((100, 100))
        # Pasting img2 image on top of img1
        # starting at coordinates (0, 0)
        resized_img1.paste(resized_img2, (0, 0))
        with open(paths_directory.path_dir_ts + '/' + (str(count) + ".jpg"), 'wb') as f:
            resized_img1.save(f)

    # Function used to encode the frame
    def getFrame(self, count):
        timestamp = time.time_ns()
        cv2.imwrite(os.path.join(paths_directory.path_dir_img, str(count) + '.jpg'),
                    self.frame)  # Save frame as jpg file
        self.getQr(count, timestamp)  # Get its timestamp as QR code
        self.pasteImages(count)  # Overlay the two images
