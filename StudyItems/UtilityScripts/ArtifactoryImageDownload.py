import os
import subprocess

def download_image():
    """This will download image or helm from artifactory"""
    yangDownload = 'wget --no-check-certificate --user=prakash.pawar@gmail.com --password=AKCp5fTaNYFCNeN1rRDZ2eefcgcarBDPdshDpqAa5DqXWRqak2SUEbzirZ9pj9sRKzVr4Jq16 artifactory/4_10_36_0-v1-helmCharts.tgz'
    print("current path :: {}".format(os.getcwd()))
    subprocess.run(yangDownload, shell=True)
    #print("Printing yangDownload::{}".format(yangDownload))


download_image()