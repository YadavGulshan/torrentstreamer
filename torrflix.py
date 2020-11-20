import requests
import subprocess
import sys


def main(movie_name):
    base_url = f"https://api.sumanjay.cf/torrent/?query={movie_name}"
    print(base_url)
    torrent_result = requests.get(base_url).json()
    # print(torrent_result)
    # print(torrent_result)
    index = 1
    magnet = []
    for result in torrent_result:
        if "movies" in result["type"].lower():
            print(index, ".", result["name"], result["size"], "\n",
                  "\tseeders =", result["seeder"], "leachers =", result["leecher"], "\n")
            index += 1
            magnet.append(result["magnet"])
    # print("\n\n")
    choice = int(input("Enter the index no. \n"))
    magnet_link = magnet[choice-1]
    # print(magnet_link)
    download = False  # default mode is to stream
    stream = True
    tv_stream = False
    stream_choice = int(input(
        "Do you want to stream the movie ?\n yes =1 \n no =2\n stream on Tv via chromecast = 3\n"))
    if stream_choice == 1:
        download = False
        tv_stream = False
    elif stream_choice == 2:
        download = True
        stream = False
        tv_stream = False
    elif stream_choice == 3:
        tv_stream = True
        stream = False
        download = False
    handler(magnet_link, download, tv_stream, stream)


def handler(magnet_link, download, tv_stream, stream):
    cmd = []
    cmd.append("webtorrent")
    cmd.append(magnet_link)
    # if not download and tv_stream:
    #     cmd.append("--vlc")
    # if not download and stream:
    #     cmd.append("--chromecast")
    if stream == True:
        cmd.append("--vlc")
    if download == True:
        cmd.append("")
    if tv_stream == True:
        cmd.append("--chromecast")
    if sys.platform.startswith("linux"):
        subprocess.call(cmd)
    elif sys.platform.startswith("win32"):
        subprocess.call(cmd, shell=True)


movie_name = input("Enter the name of movie: ")
main(movie_name)
