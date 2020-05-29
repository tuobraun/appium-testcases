import os
from ftplib import FTP
import time
import re
from Credentials.credentials import FtpCredentials


def ftp_download(platform):
    ftp = FTP(FtpCredentials.ic_ftp)
    ftp.login(user=FtpCredentials.user, passwd = FtpCredentials.passwd)
    print(f'- Logged in under {FtpCredentials.user}')

    PATH = f'/{FtpCredentials.ACC_NAME}/{FtpCredentials.RELEASE_DIR}/{FtpCredentials.BRANCH_DIR}/'
    ftp.cwd(PATH)

    dir_folders = str(ftp.nlst())
    build_nums = re.findall(r'[\d\.\d]+', dir_folders) #Extracts all build numbers
    
    def filterNumber(n): #Finds only 3-digit numbers for branch builds
        if(len(n)==3):
            return True
        else:
            return False

    build_nums = list(filter(filterNumber, build_nums))
    build_nums = sorted(build_nums, key=float) #Sorts build numbers ascending
    print(f'- The latest build is {build_nums[-1]}') #Gets the latest (the highest) build number

    ftp.quit()
    print('- Disconnected')

ftp_download(FtpCredentials.ANDROID_DIR)
