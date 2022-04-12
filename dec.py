import cv2
import paths_directory


class decoder:

    def __init__(self, frame, frameN, mode, id_video):
        self.frame = frame
        self.frameN = frameN
        self.mode = mode
        self.id_video = id_video

    # Function used to decode the qr code
    def decodeQr(self):
        image = self.frame
        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()
        # detect and decode
        data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
        return data, vertices_array

    # Function used to calculate the latency
    def getLatency(self, t_i):
        lat = 0
        before, vertices_array = self.decodeQr()  # it gets the timestamp of the video in that frame
        if vertices_array is None:
            return lat
        else:
            try:
                lat = t_i - float(before)  # latency between the actual time and the timestamp
            except:
                return lat
            if self.frameN == 0:  # If it is the first frame
                # Saving latency per mode of transmission
                file = open(paths_directory.file_rx + "_" + str(self.mode) + "_" + str(self.id_video), "w")
                file.write(str(self.frameN) + "\n" + str(before) + "\n" + str(t_i) + "\n" + str(lat) + "\n")
                file.close()
                return lat

            # Saving latency per mode of transmission
            file = open(paths_directory.file_rx + "_" + str(self.mode) + "_" + str(self.id_video), "a")
            file.write(str(self.frameN) + "\n" + str(before) + "\n" + str(t_i) + "\n" + str(lat) + "\n")
            file.close()
        return lat
