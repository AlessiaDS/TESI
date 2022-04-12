import plots
import paths_directory

# Output results

if __name__ == '__main__':
    paths_directory.create_dir(paths_directory.path_dir_plots)
while True:
    choice = input("Select which plots you wants to display:\n"
                   "1 - Plot of video's latency in one transmission mode\n"
                   "2 - Plot of latency's mean in one transmission mode of the different videos\n"
                   "3 - Plot of latency's variance in one transmission mode of the different videos\n"
                   "4 - Plot of latency's mean in the different transmission modes of one video\n"
                   "5 - Plot of latency's variance in the different transmission modes of one video\n"
                   "6 - Exit\n")

    if int(choice) == 1:
        tm = input("Choose the transmission mode to plot (eg. t0):\n")
        tm = tm.replace("t", "")
        for j in range(5):
            path = paths_directory.file_rx + "_t" + tm + "_v" + str(j)
            plots.plotLatency(path, paths_directory.path_dir_plots, tm, j)

    if int(choice) == 2:
        tm = input("Choose the transmission mode to plot (eg. t0):\n")
        tm = tm.replace("t", "")
        path = paths_directory.mean + "_t" + tm
        plots.plotMeanT(path, paths_directory.path_dir_plots, tm)

    if int(choice) == 3:
        tm = input("Choose the transmission mode to plot (eg. t0):\n")
        tm = tm.replace("t", "")
        path = paths_directory.var + "_t" + tm
        plots.plotVarT(path, paths_directory.path_dir_plots, tm)

    if int(choice) == 4:
        vd = input("Choose the video to plot (eg. v0):\n")
        vd = vd.replace("v", "")
        path = paths_directory.mean + "_v" + vd
        plots.plotMeanV(path, paths_directory.path_dir_plots, vd)

    if int(choice) == 5:
        vd = input("Choose the video to plot (eg. v0):\n")
        vd = vd.replace("v", "")
        path = paths_directory.var + "_v" + vd
        plots.plotVarV(path, paths_directory.path_dir_plots, vd)

    if int(choice) == 6:
        break