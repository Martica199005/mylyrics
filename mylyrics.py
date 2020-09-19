import sys 
import requests
from bs4 import BeautifulSoup as BS

separator=" "
providers=['azlyrics','elyrics']
# add '' in string to artist


list=['mylyrics.py','-p', 'elyrics', '-a', "red hot chili peppers", '-l', "can't stop"]
numbers=range(0,len(list))

only_odd = [num for num in numbers if num % 2 == 1] 

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
    '''toglie i caratteri speciali e gli spazi
    li fa diventare lowercase
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
    ''' right url for each provider'''
    if provider==providers[0]:
        # example https://www.azlyrics.com/lyrics/mahmood/soldi.html
        page="https://www."+provider+".com/lyrics/"+artist+"/"+lyrics+".html"
    else:
        # example https://www.elyrics.net/read/e/eminem-lyrics/role-model-lyrics.html
        firstchar=artist[0]
        page="https://www."+provider+".net/read/"+firstchar+"/"+artist+"-lyrics/"+lyrics+"-lyrics/.html"
    return page

def searchlyric(url,provider):
    ''' Gestisci se non trova la canzone o l'artista trycatch'''
    page= requests.get(url)
    soup= BS(page.content , 'html.parser')
    if provider==provider[1]:
        lyrics=soup.find(id='inlyr').text
    else:
        former_div=(soup.find(name="div", class_='ringtone')) #azlyrics search div with  id='ringtone'
        lyrics_div=former_div.find_next_sibling("div")
        lyrics=lyrics_div.text
    return lyrics
    

def checkList(list):
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

def saveLyrics(bool,text):
    '''Attraverso l'utilizzo del flag -s (opzionale) 
    l'utente decide di salvare il testo della canzone in una cartella dedicata all'artista, 
    successivi utilizzi dello script leggeranno il testo della canzone dal disco invece che 
    recuperare dai provider se è stato salvato.'''
    print('flag -s: '+ str(bool))


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
                page=URLpage(provider, singer, title)
                searchlyric(page,provider)
                saveLyrics(checkList(list)[1])
                
                print("Provided by "+provider)
            else:
                print("Wrong provider")

        else:
            errorString()
    else:
        errorString()
 




mylyrics(list)





            
