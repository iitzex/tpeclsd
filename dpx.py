import dropbox
from util import getday

#get token from dropbox
token = ''
dpx = dropbox.Dropbox(token)

def upload():
    today = getday()
    fname = "TPEclsd_" + today + ".png"
    print fname + " uploaded"

    dpx.files_upload(fname, '/TPEclsd/' + fname)

if __name__ == '__main__':
    upload()

