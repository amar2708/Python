import webbrowser
import time

def open_browser():
    url='https://www.youtube.com/watch?v=JGwWNGJdvx8'
    webbrowser.open(url,new=1,autoraise=True)

def wait():
    time.sleep(20)

def open_book():
    url='https://docs.python.org/3/library/webbrowser.html'
    webbrowser.open(url,new=2,autoraise=True)

if __name__=='__main__':
    open_book()
    wait()
    open_browser()
