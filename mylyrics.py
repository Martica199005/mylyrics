import sys 
import os
import os.path
from os import path
from pathlib import Path
import requests
from bs4 import BeautifulSoup as BS

separator=" "
providers=['azlyrics','elyrics']
path=os.getcwd() # da mettere ovunque come path non come stringa
# add '' in string to artist
list=['mylyrics.py','-p', 'elyrics', '-a', "red hot chili peppers", '-l', "can't stop"]
numbers=range(0,len(list))
only_odd = [num for num in numbers if num % 2 == 1] 

def converterStrToPath(str_path):
    return Path(str_path)


def specialChar(ch):
    '''Check if character is a Special Character'''
    if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
       bool=False
    elif(ch >= '0' and ch <= '9'):
        bool=False
    else:
        bool=True
    return bool

def modifyword(str,provider):
    '''Removes special characters and spaces and
    makes them become lowercase
    '''
    if provider==providers[0]:
        for i in str:
            if specialChar(i):
                str=str.replace(i,"")
    else:
        for i in str:
            if i=="'":
                str=str.replace(i,"_")
            elif (i==" "):
                str=str.replace(i,"-")
    lower=[i.lower() for i in str]
    str=separator.join(lower)
    str=str.replace(" ","")
    return str
    
def URLpage(provider, artist, lyrics):
    ''' Gives the right url for each provider'''
    if provider==providers[0]:
        # example https://www.azlyrics.com/lyrics/mahmood/soldi.html
        page="https://www."+provider+".com/lyrics/"+artist+"/"+lyrics+".html"
    else:
        # example https://www.elyrics.net/read/e/eminem-lyrics/role-model-lyrics.html
        firstchar=artist[0]
        page="https://www."+provider+".net/read/"+firstchar+"/"+artist+"-lyrics/"+lyrics+"-lyrics/.html"
    return page

def searchlyric(url,provider):
    ''' Searches the lyrics'''
    print(url)
    print(provider)
    page= requests.get(url)
    soup= BS(page.content , 'html.parser')
    try:
        if provider==providers[1]:
            print('provider elyrics')
            lyrics=soup.find(id='inlyr').text
        else:
            print('provider azlyrics')
            former_div=(soup.find(name="div", class_='ringtone')) #azlyrics search div with  id='ringtone'
            lyrics_div=former_div.find_next_sibling("div")
            lyrics=lyrics_div.text
        return lyrics
    except :
        print ("Lyrics not found")
        sys.exit()
    

def checkList(list):
    '''Checks if the inserted string length is correct
    and if there is the -s command
    '''
    if len(sys.argv)==len(list):
        bool=[True,False]
    elif len(sys.argv)==len(list)+1 and sys.argv[len(list)]=='-s':
        bool=[True,True]
    else:
        bool=[False,False]
    return bool

def errorString():
    print("Write for example a string like: ")
    separator=" "
    print("python "+ separator.join(list))


def writetxt(filename,text,provider,path): 
  original_stdout = sys.stdout 
  with open(str(path)+"/"+filename, 'w') as f:
    sys.stdout =f 
    print(text)
    print('\n')
    print("Provided by "+provider)
    
    sys.stdout = original_stdout 
    # Reset the standard output to its original value

def createFolder(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

def checkFileExists(filename):
    bool=filename.exists()
    return bool

def checkFolderExists(pathdir):
    bool=pathdir.exists()
    return bool

def readFile(path):
    file=open(str(path),'r')
    print(file.read())
    file.close()


        

def saveLyrics(bool,path_folder,filename,text,provider):
    '''Through the use of the -s flag (optional)
    the user decides to save the lyrics of the song in a folder dedicated to the artist,
    subsequent uses of the script will read the lyrics from the disc instead of
    retrieve from providers if it has been saved'''
    print('flag -s: '+ str(bool))
    if bool:
        bool=checkFolderExists(path_folder)
        if not bool:
            createFolder(path_folder)
        #if folder already exists but file doesn't exist

        writetxt(filename,text,provider,path_folder)


def mylyrics(list):
    if checkList(list)[0]:
        commands_line_arguments=[list[i] for i in only_odd if sys.argv[i]==list[i]]
        if len(commands_line_arguments)==3:
            provider = sys.argv[2]
            artist=sys.argv[4]
            lyrics=sys.argv[6]
            if provider in providers:
                singer=modifyword(artist,provider) #change string artist 
                title=modifyword(lyrics,provider) #change string lyrics
                #check if the txt file already exists
                filename=title+".txt"
                path_folder=converterStrToPath(path+"/"+singer)
                path_file=converterStrToPath(path+"/"+singer+"/"+filename)
                bool=checkFileExists(path_file)
                if bool:
                    readFile(path_file)
                else:
                    page=URLpage(provider, singer, title)
                    text=searchlyric(page,provider)
                    saveLyrics(checkList(list)[1],path_folder,filename,text,provider)
            else:
                print("Wrong provider")

        else:
            errorString()
    else:
        errorString()
 


mylyrics(list)





            
