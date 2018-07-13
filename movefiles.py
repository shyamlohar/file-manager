import os
import glob
import shutil
import sys
import argparse

parser = argparse.ArgumentParser(description = 'make your directory look clean again')
parser.add_argument('-e','--extension', metavar = '' ,help = 'extension of file you wanna move to selected folder')
parser.add_argument('-f','--folder', metavar = '' ,help = 'name of folder you wanna move your files to')
args = parser.parse_args()

current_directory = os.getcwd()
move_directory = os.path.join(os.getcwd(),'Arrangedfiles')

def creat_folder():
    if not 'Arrangedfiles' in os.listdir():
        os.system('mkdir Arrangedfiles')
        print('created Arrangedfiles folder and your files will be move to that directory');

def move_all_smart():
    # current_directory = os.getcwd()
    # move_directory = os.path.join(os.getcwd(),'Arrangedfiles')

    if not 'Arrangedfiles' in os.listdir():
        print('nahi hai folder bana bhai');
        os.system('mkdir Arrangedfiles')

    files = os.listdir()

    text_files = glob.glob('*.txt')

    image_files = glob.glob('*.png') + glob.glob('*.jpeg') + glob.glob('*.gif') + glob.glob('*.bmp') + glob.glob('*.jpg') 

    video_files = glob.glob('*.mp4') + glob.glob('*.flv') + glob.glob('*.mkv') + glob.glob('*.wmv') + glob.glob('*.avi') + glob.glob('*.mov') + glob.glob('*.3gp') + glob.glob('*.mpg')

    compressed_files = glob.glob('*.zip') + glob.glob('*.rar') + glob.glob('*.7z') + glob.glob('*.tar')

    document_files = glob.glob('*.pdf') + glob.glob('*.docx') + glob.glob('*.doc') + glob.glob('*.xls') + glob.glob                                             ('*.xlsm') + glob.glob('*.ppt') + glob.glob('*.pptx')


    for file in text_files:
        src = os.path.join(current_directory,file)
        if not 'textfiles' in os.listdir(move_directory):
            os.system(f'cd {move_directory} && mkdir textfiles')
        dst = os.path.join(move_directory,'textfiles')
        shutil.move(src,dst)
    print('all text files moved')

    for file in image_files:
        src = os.path.join(current_directory,file)
        if not 'images' in os.listdir(move_directory):
            os.system(f'cd {move_directory} && mkdir images')
        dst = os.path.join(move_directory,'images')
        print(src,'src')
        shutil.move(src,dst)
    print('all images moved')

    for file in video_files:
        print(file)
        src = os.path.join(current_directory,file)
        if not 'videos' in os.listdir(move_directory):
            os.system(f'cd {move_directory} && mkdir videos')
        dst = os.path.join(move_directory,'videos')
        shutil.move(src,dst)
    print('all videos moved')

    for file in compressed_files:
        src = os.path.join(current_directory,file)
        if not 'compressed_files' in os.listdir(move_directory):
            os.system(f'cd {move_directory} && mkdir compressed_files')
        dst = os.path.join(move_directory,'compressed_files')
        shutil.move(src,dst)
    print('all videos moved')

    for file in document_files:
        src = os.path.join(current_directory,file)
        if not 'documents' in os.listdir(move_directory):
            os.system(f'cd {move_directory} && mkdir documents')
        dst = os.path.join(move_directory,'documents')
        shutil.move(src,dst)
    print('all documents moved')

    print('{:*^80}'.format('all done'))

def move_manually(extension,folder):
    files_to_move = glob.glob(f'*.{extension}')
    creat_folder()
    for file in files_to_move:
        src = os.path.join(current_directory,file)
        if not folder in os.listdir(move_directory):
            os.system(f'cd {move_directory} && mkdir {folder}')
        dst = os.path.join(move_directory,folder)
        shutil.move(src,dst)
    print('moved all your files in your desired folder')

if __name__ == '__main__':

    if not args.extension and args.folder:
        print('specify extension of file which you wanna move to specifield folder and rerun the script')

    elif args.extension and not args.folder:
        print('specify folder in which you wanna move all you files and re run the script again');

    elif args.extension and args.folder:
        print(f'moving all files with {args.extension} extension to {args.folder} folder')
        move_manually(args.extension,args.folder)

    else:
        k = input('reply with "y" if you wanna arrange all your files or reply with "n" if you wanna exit \n')
        if k.lower() == 'y':
            print ("yes moving everything smartly")
            move_all_smart()
        elif k.lower() == 'n':
            print ("you are free enough to do it on your own it seems if not rerun script and use appropriate options use --help command while running script for help")

    