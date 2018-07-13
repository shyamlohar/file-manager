# File Arranger

#### Minimal Script to keep your folders clean from pile of files.
##### just run python script in folder you want to organize and script will do the job

### Example
---
##### you have C:\Users\shyam directory with following files 

* hello.png
* bye.mp4
* dd.avi
* python.mkv
* logo.bmp
* resume.pdf
* data.zip
* compressed_images.7z

##### And you want to organize this folder.

##### Open Terminal in that folder and run python script.
###### if you dont know how to use this script just put this script in folder you wanna organize and  runs script in terminal using command ```python movefiles.py``` just make sure you have installed python 3 on your machine.

##### Script will arrange file for you like shown below

```
   Arrangedfiles/
   		textfiles/..*txt files here*
        images/..*image files here*
        videos/..*video files here*
        compressed_files/..*compressed files here*
        documents/.. *document files here* 
   ```
   
 ##### If you wanna move files with certain extension to desired folder you can pass arguments while running script as shown below 
 
 ``` python movefiles.py -e <file extension here> -f <folder name here>```
#### 					or
 ``` python movefiles.py -extension <file extension here> -f <folder name here>```
 
 ### Example
 ---
 ```python movefiles.py -e py -f pythonfiles```
 
 ###### this will move all your files with .py extensions in 
 ```
 Arrangedfiles/
      pythonfiles..
   ```
  
  
######  For help Related Script run
```python movefiles.py -help```