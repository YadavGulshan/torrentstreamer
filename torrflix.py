import requests
import subprocess
import sys

def main():
    movie_name = input("Enter the movie name which you want to stream \n")
    base_url = f"https://api.sumanjay.cf/torrent/?query={movie_name}"
    ##thanks to sumanjay sir for creating this api.
    torrent_results = requests.get(base_url).json()

    ####
   
    
    index=1
    magnet = []
    for result in torrent_results:
        if "movie" in result["type"].lower():
            print(index,result["name"],result["size"])
            #print(result["size"])
            #print(result["magnet"])
            index+=1
            magnet.append(result["magnet"]) 
    print("/n/n")        
    choice = int(input("Enter the index no. of the movie you want to watch\n"))        
    #print("Magnet link of the movie is :")
    magnet_link = magnet[choice-1]
    
    download = False #default mode is to stream
    stream = True
    stream_choice = int(input("Do you want to stream the movie ?\n yes =1 \n no =2\n stream on Tv via chromecast = 3\n"))
    if stream_choice==1:
        download = False
        tv_stream = False
    elif stream_choice==2:
        download = True
        stream = False
        tv_stream = False
    elif stream_choice == 3:
        tv_stream = True
        stream = False
        download = False
    handler(magnet_link,download, tv_stream, stream)



def handler(magnet_link, download, tv_stream,stream):
    cmd = []
    cmd.append("webtorrent")
    cmd.append(magnet_link)
    # if not download and tv_stream:        
    #     cmd.append("--vlc")
    # if not download and stream:
    #     cmd.append("--chromecast")   
    if stream== True:
        cmd.append("--vlc")
    if download == True:
        cmd.append("")
    if tv_stream == True:
        cmd.append("--chromecast")     
    if sys.platform.startswith("linux"):
        subprocess.call(cmd)
    elif sys.platform.startswith("win32"):
        subprocess.call(cmd,shell=True)

main()
