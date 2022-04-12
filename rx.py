# This is client code to receive encoded video frames over UDP
import base64
import time
import os
import cv2
import numpy as np
import socket
import dec
import paths_directory
import statistics

message = b'Hello'


class rx:
    def __init__(self, host_ip, port, BUFF_SIZE, mode):
        self.BUFF_SIZE = BUFF_SIZE
        self.host_ip = host_ip
        self.port = port
        self.mode = mode

    def rx_socket(self):
        # Initializing client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.BUFF_SIZE)
        client_socket.sendto(message, (self.host_ip, self.port))

        # Used for knowing which video is been transmitted
        packet, _ = client_socket.recvfrom(self.BUFF_SIZE)
        id_video = base64.b64decode(packet, ' /')
        id_video = str(id_video)
        id_video = id_video.replace("b'", "")
        id_video = id_video.replace("'", "")

        frameN = 0
        latency = []
        while True:

            # Receiving
            packet, _ = client_socket.recvfrom(self.BUFF_SIZE)
            # Decoding
            data = base64.b64decode(packet, ' /')

            if data == paths_directory.stop_msg:
                client_socket.close()

                # Updating statistics

                mn = statistics.mean(latency)
                file = open(paths_directory.mean + "_" + str(self.mode), "a")
                file.write(str(mn) + "\n")
                file = open(paths_directory.mean + "_" + str(id_video), "a")
                file.write(str(mn) + "\n")

                vr = np.var(latency)
                file = open(paths_directory.var + "_" + str(self.mode), "a")
                file.write(str(vr) + "\n")
                file = open(paths_directory.var + "_" + str(id_video), "a")
                file.write(str(mn) + "\n")

                cv2.destroyWindow("RECEIVING VIDEO")
                break

            npdata = np.frombuffer(data, dtype=np.uint8)
            frame = cv2.imdecode(npdata, 1)
            cv2.imwrite(os.path.join(paths_directory.path_dir_rf, str(frameN) + '.jpg'), frame)

            # Calculating latency
            t_i = time.time_ns()
            decoder = dec.decoder(frame, frameN, self.mode, id_video)
            lat = decoder.getLatency(t_i)

            frameN += 1

            if lat != 0:
                latency.append(lat)

            # Showing video received
            cv2.imshow("RECEIVING VIDEO", frame)

            cv2.waitKey(1)
