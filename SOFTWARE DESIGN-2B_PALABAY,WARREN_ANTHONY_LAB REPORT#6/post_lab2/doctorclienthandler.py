from asyncio.windows_utils import BUFSIZE
from codecs import decode
from threading import Thread
from doctor import Doctor
import os.path
import pickle

BUFSIZE = 1024
CODE = 'ascii'

class DoctorClientHandler(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client
    
    def run(self):
        self.filename = decode(self.client.resv(BUFSIZE), CODE) + '.dat'
        if os.path.exists(self.filename):
            fileObj= open(self.filename, 'rb')
            self.dr = pickle.load(fileObj)
            
        else:
            self.dr = Doctor()
        self.client.send(bytes(self.dr.greeting(), CODE))
        while True:
            message = decode(self.client.resv(BUFSIZE), CODE)
            if not message:
                print('Client disconnected')
                self.client.close()
                fileObj = open(self.filename, 'wb')
                pickle.dump(self.dr, fileObj)
                fileObj.close()
                break
            else:
                self.client.send(bytes(self.dr.reply(message), CODE))