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
    FILE_NAME = FtpCredentials.FILE_NAME
    CONFIG_NAME = FtpCredentials.CONFIG_NAME

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
    build_num = build_nums[-1] #Gets the latest (the highest) build number

    BUILD_DIR = 'build_'+build_num
    ftp.cwd(f'{BUILD_DIR}/{platform}')

    file_ext = None
    if platform == 'Android_Apps':
        file_ext = 'apk'
    elif platform == 'iOS_Apps':
        file_ext = 'ipa'
    elif platform == 'Configs':
        file_ext = 'xml'
    
    FILE_NAME = f'IC_Forms_7.0.{build_num}.{file_ext}'

    if platform == 'Configs':
        FILE_NAME = f'{CONFIG_NAME}.{file_ext}'
    elif platform == 'iOS_Apps':
        FILE_NAME = f'ICForms_7.0.{build_num}.{file_ext}'

    file_path = f'{PATH}/{BUILD_DIR}/{platform}/{FILE_NAME}'
    
    print(f'- Started downloading file: {FILE_NAME}')
    
    currentpath = os.getcwd()
    folderpath = os.path.join(f'{currentpath}/apps/{FILE_NAME}')

    with open(folderpath, 'wb') as f:
        ftp.retrbinary('RETR ' + file_path, f.write)
    
    print('- File download finished')
    ftp.quit()
    print('- Disconnected')

ftp_download(FtpCredentials.ANDROID_DIR)
ftp_download(FtpCredentials.IOS_DIR)
ftp_download(FtpCredentials.CONFIG_DIR)
print('- All Files Downloaded')
