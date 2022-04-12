# This is server code to send encoded video frames over UDP
import base64
import time
import cv2
import paths_directory
import socket
import enc
import keyboard


class tx:
    def __init__(self, vidcap, host_ip, port, BUFF_SIZE, id_video):
        self.BUFF_SIZE = BUFF_SIZE
        self.id_video = id_video
        self.vidcap = vidcap  # video to decode
        self.host_ip = host_ip
        self.port = port
        self.FPS = self.vidcap.get(cv2.CAP_PROP_FPS)  # frame per seconds
        self.TS = (0.5 / self.FPS) * 1000000000  # time per frame

    def tx_socket(self):

        # Initializing server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.BUFF_SIZE)
        socket_address = (self.host_ip, self.port)
        server_socket.bind(socket_address)
        print('Listening at:', socket_address)

        count = 0
        sec = 0

        while True:
            # Waiting for connection
            msg, client_addr = server_socket.recvfrom(self.BUFF_SIZE)
            print('GOT connection from ', client_addr)
            # Communicating info video name
            message = base64.b64encode(bytes(self.id_video, 'UTF-8'))
            server_socket.sendto(message, client_addr)

            while True:
                self.vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
                hasFrames, frame = self.vidcap.read()
                if hasFrames:

                    # Encoding
                    delta_i = time.time_ns()
                    en = enc.encoder(frame)
                    en.getFrame(count)

                    # Sending
                    frame = cv2.imread(paths_directory.path_dir_ts + "/" + (str(count) + ".jpg"))
                    encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
                    message = base64.b64encode(buffer)
                    server_socket.sendto(message, client_addr)

                    # Adjusting the rate
                    count += 1
                    delta_f = time.time_ns()
                    delta = delta_f - delta_i
                    wait = 1
                    if delta < self.TS:
                        wait = self.TS - delta

                    sec = round((sec + (1 / self.FPS)), 2)

                    # Showing video sent
                    cv2.imshow('TRANSMITTING VIDEO', frame)
                    # Waiting if transmission is too fast
                    cv2.waitKey(int(wait))

                # Sending stop message
                if keyboard.is_pressed("e"):
                    base64_bytes = base64.b64encode(paths_directory.stop_msg)
                    server_socket.sendto(base64_bytes, client_addr)
                    cv2.destroyWindow("TRANSMITTING VIDEO")
                    server_socket.close()
                    break
