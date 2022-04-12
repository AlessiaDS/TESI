import socket
import sys
import cv2
import paths_directory
import tx
import rx

# Initial command if using MacOs
# sudo sysctl -w net.inet.udp.maxdgram=65535
# Command for the transmitter which is the server
# python main.py tx ip_address_server name_video.mp4
# Command for the receiver which is the client
# python main.py rx ip_address_server mode_of_transmission

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Invalid parameters')
        sys.exit()

if sys.argv[1] == 'tx':

    # Creating necessary folders
    paths_directory.create_dir(paths_directory.path_dir_qr)
    paths_directory.create_dir(paths_directory.path_dir_img)
    paths_directory.create_dir(paths_directory.path_dir_ts)

    # Encoding and transmitting part (UDP)

    BUFF_SIZE = 65536
    port = 8080
    host_ip = sys.argv[2]

    id_video = sys.argv[3]
    id_video = id_video.replace(".mp4", "")

    vid = cv2.VideoCapture(paths_directory.path_dir_video + sys.argv[3])  # vn
    tx = tx.tx(vid, host_ip, port, BUFF_SIZE, id_video)
    tx.tx_socket()

if sys.argv[1] == 'rx':

    # Creating necessary folders
    paths_directory.create_dir(paths_directory.path_dir_rf)
    paths_directory.create_dir(paths_directory.path_file)
    paths_directory.create_dir(paths_directory.path_statistics)

    # Receiving and decoding part (UDP)
    BUFF_SIZE = 65536
    port = 8080
    host_ip = sys.argv[2]
    mode = sys.argv[3]

    rx = rx.rx(host_ip, port, BUFF_SIZE, mode)
    rx.rx_socket()
