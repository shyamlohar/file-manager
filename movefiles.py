import os
import glob
import shutil

if os.getcwd().split('\\')[-1] == "Desktop":
    current_directory = os.getcwd()
    move_directory = os.path.join(os.getcwd(),'Arrangedfiles')

    if not "Arrangedfiles" in os.listdir():
        print('nahi hai folder bana bhai');
        os.system('mkdir Arrangedfiles')

    files = os.listdir()

    text_files = glob.glob('*.txt')
    image_files = glob.glob('*.png') + glob.glob('*.jpeg') + glob.glob('*.gif') + glob.glob('*.bmp') + glob.glob('*.jpg') + glob.glob('*.avi')

    video_files = glob.glob('*.mp4') + glob.glob('*.avi') + glob.glob('*.mp4') + glob.glob('*.flv') + glob.glob('*.mkc') + glob.glob('*.wmv') +               glob.glob('*.mov') + glob.glob('*.3gp') + glob.glob('*.mpg')

    compressed_files = glob.glob('*.zip') + glob.glob('*.rar') + glob.glob('*.7z') + glob.glob("*.tar")

    document_files = glob.glob('*.pdf') + glob.glob('*.docx') + glob.glob('*.doc') + glob.glob('*.xls') + glob.glob                                             ('*.xlsm') + glob.glob('*.ppt') + glob.glob('*.pptx')


    for file in text_files:
        src = os.path.join(current_directory,file)
        if not 'textfiles' in move_directory:
            os.system(f'cd {move_directory} && mkdir textfiles')
        dst = os.path.join(move_directory,'textfiles')
        shutil.move(src,dst)
        print('all text files moved')
    
    for file in image_files:
        src = os.path.join(current_directory,file)
        if not 'images' in move_directory:
            os.system(f'cd {move_directory} && mkdir images')
        dst = os.path.join(move_directory,'images')
        shutil.move(src,dst)
        print('all images moved')

    for file in video_files:
        src = os.path.join(current_directory,file)
        if not 'images' in move_directory:
            os.system(f'cd {move_directory} && mkdir videos')
        dst = os.path.join(move_directory,'videos')
        shutil.move(src,dst)
        print('all videos moved')

    for file in compressed_files:
        src = os.path.join(current_directory,file)
        if not 'images' in move_directory:
            os.system(f'cd {move_directory} && mkdir compressed_files')
        dst = os.path.join(move_directory,'compressed_files')
        shutil.move(src,dst)
        print('all videos moved')

    for file in document_files:
        src = os.path.join(current_directory,file)
        if not 'documents' in move_directory:
            os.system(f'cd {move_directory} && mkdir documents')
        dst = os.path.join(move_directory,'documents')
        shutil.move(src,dst)
        print('all documents moved')

    print('{:*^80}'.format('all done'))

