import urllib.request
import os
import time
def main():
    userInput = input("Enter Youtube URL: ")

    x = userInput.replace("https://www.youtube.com/watch?v=", "", 1000)
    x = x[0: 11]
    thumbUrl = "https://img.youtube.com/vi/" + x + "/0.jpg"



    try:
        x = userInput.replace("https://www.youtube.com/watch?v=", "", 1000)
        x = x[0: 11]
        thumbUrl = "https://img.youtube.com/vi/" + x + "/0.jpg"
        
        r = urllib.request.urlopen(thumbUrl)
        localPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\' + x + ".jpg"
        with open(localPath, "wb") as f:
            f.write(r.read())

        print(f"Sucessfuly saved as {x}.jpg at Desktop.")
        os.system('pause')
        
    except:
        try:
            x = userInput.replace("https://youtu.be/", "", 1000)
            x = x[0: 11]
            thumbUrl = "https://img.youtube.com/vi/" + x + "/0.jpg"
            
            r = urllib.request.urlopen(thumbUrl)
            localPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\' + x + ".jpg"
            with open(localPath, "wb") as f:
                f.write(r.read())

            print(f"Sucessfuly saved as {x}.jpg at Desktop.")
            os.system('pause')
        except:
            print("Looks like URL is invalid. Please, try again.")
            time.sleep(2)
            os.system('pause')
            main()
        
        

if __name__ == '__main__':
    main()


    
