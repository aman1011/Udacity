import urllib
def readtext():
    readfile = open('/Users/gaman/Documents/GitHub/Udacity/Module 1/Python/randomtext.txt')
    filecontent = readfile.read()
    readfile.close()

    print(filecontent)

    # Sending this text to the checked which
    # would use the google API to checked# for a profane word.
    CheckForProfanity(filecontent)


def CheckForProfanity(text):

    # Checking by calling to the google API.
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    response = connection.read()
    print response
    if response == 'true':
        print("Profanity Alert!")
    elif response == 'false':
        print("Clean text without cuss words")
    else:
        print("Document was not scanned properly")

readtext()
