import matplotlib.pyplot as plt


# Plot for the frames' latency in the 5 different videos in one transmission mode
def plotLatency(path, path_dir, mode, video):
    with open(path) as file:
        n = 0
        lat = []
        while True:
            line = file.readline()
            if not line:
                plt.title("Latency of every frame", fontsize=10)
                plt.ylabel("Latency in ns", fontsize=8)
                plt.xlabel("Frame's number", fontsize=8)
                plt.plot(lat, linestyle='dotted')
                if video == 4:  # saving plot after all the file have been plotted
                    plt.legend(["video 0", "video 1", "video 2", "video 3", "video 4"])
                    plt.savefig(path_dir + "latency_t" + str(mode))
                break
            if n == 3:
                line = line.replace("\n", "")
                lat.append(float(line))
                n = 0
            else:
                n += 1


# Plot of the mean of latency of the 5 videos in one transmission mode
def plotMeanT(path, path_dir, mode):
    f = open(path, "r")
    Lines = f.readlines()
    f.close()
    arr = []

    for j in range(len(Lines)):
        str = Lines[j]
        str = str.replace("\n", "")
        arr.append(float(str))

    fig, ax = plt.subplots()
    plt.title("Video's latency mean for transmission mode " + mode, fontsize=10)
    plt.ylabel("Latency", fontsize=8)

    b = []
    for i in range(len(arr)):
        b.append(i)

    ax.bar(0, arr[0])
    ax.bar(1, arr[1])
    ax.bar(2, arr[2])
    ax.bar(3, arr[3])
    ax.bar(4, arr[4])

    plt.legend(["video 0", "video 1", "video 2", "video 3", "video 4"])
    plt.savefig(path_dir + "mean_t" + mode)


# Plot of the mean of latency of one video in the different transmission modes
def plotMeanV(path, path_dir, video):
    f = open(path, "r")
    Lines = f.readlines()
    f.close()
    arr = []

    for j in range(len(Lines)):
        str = Lines[j]
        str = str.replace("\n", "")
        arr.append(float(str))

    fig, ax = plt.subplots()
    plt.title("Video's latency mean for video " + video + " in the different transmission modes", fontsize=8)
    plt.ylabel("Latency", fontsize=8)

    b = []
    for i in range(len(arr)):
        b.append(i)

    ax.bar(0, arr[0])
    ax.bar(1, arr[1])
    ax.bar(2, arr[2])

    plt.legend(["mode 0", "mode 1", "mode 2"])
    plt.savefig(path_dir + "mean_v" + video)


# Plot of the variance of latency of the 5 videos in one transmission mode
def plotVarT(path, path_dir, mode):
    f = open(path, "r")
    Lines = f.readlines()
    f.close()
    arr = []

    for j in range(len(Lines)):
        str = Lines[j]
        str = str.replace("\n", "")
        arr.append(float(str))

    fig, ax = plt.subplots()
    plt.title("Video's latency variance for transmission mode " + mode, fontsize=10)
    plt.ylabel("Variance", fontsize=8)

    b = []
    for i in range(len(arr)):
        b.append(i)

    ax.bar(0, arr[0])
    ax.bar(1, arr[1])
    ax.bar(2, arr[2])
    ax.bar(3, arr[3])
    ax.bar(4, arr[4])

    plt.legend(["video 0", "video 1", "video 2", "video 3", "video 4"])
    plt.savefig(path_dir + "variance_t" + mode)


# Plot of the variance of latency of one video in the different transmission modes
def plotVarV(path, path_dir, video):
    f = open(path, "r")
    Lines = f.readlines()
    f.close()
    arr = []

    for j in range(len(Lines)):
        str = Lines[j]
        str = str.replace("\n", "")
        arr.append(float(str))

    fig, ax = plt.subplots()
    plt.title("Video's latency variance for video " + video + " in the different transmission modes", fontsize=8)
    plt.ylabel("Variance", fontsize=8)

    b = []
    for i in range(len(arr)):
        b.append(i)

    ax.bar(0, arr[0])
    ax.bar(1, arr[1])
    ax.bar(2, arr[2])

    plt.legend(["mode 0", "mode 1", "mode 2"])
    plt.savefig(path_dir + "variance_v" + video)
