from asyncio.windows_utils import BUFSIZE
from socket import *
from codecs import decode
from breezypythongui import EasyFrame

HOST = 'localhost'
PORT = 5500
BUFSIZE = 1024
ADDRESS = (HOST,PORT)
CODE = 'ascii'

class DoctorClient(EasyFrame):
    
    COLOR = '#CCEEFF'
    
    def __init__(self):
        
        EasyFrame.__init__(self, title = 'Doctor',
                           background = DoctorClient.COLOR)
        
        self.drLabel = self.addLabel (text= 'Please enter your name to connect.',
                                      row=0, column =0, columnspan=2,
                                      background = DoctorClient.COLOR)
        self.ptField = self.addTextField (text = '', row = 1,
                                          column=0, columnspan = 2,
                                         width = 50)
        self.sendBtn = self.addButton (row=2, column =0, text = 'send reply',
                                       command = self.sendReply,
                                       state = 'disabled')
        self.connectBtn = self.addButton (row=2, column=1,
                                          text='Connect',
                                          command= self.connect)
        
        self.ptField.bind('<Return>', lambda event: self.sendReply())
        
    def sendReply(self):
        
        ptInput = self.ptField.getText()
        if ptInput != '':
            self.server.send(bytes(ptInput, CODE))
            drReply = decode(self.server.recv(BUFSIZE), CODE),
            if not drReply:
                self.messageBox(message = 'Doctor disconnected')
                self.disconnect()
            else:
                self.drLabel['text'] = drReply
                self.ptfield.setText("")
                
    def connect(self):
        ptInput = self.ptField.getText()
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.connect(ADDRESS)
        self.server.send(bytes(ptInput, CODE))
        self.drLabel['text'] = decode(self.server.recv(BUFSIZE), CODE)
        self.connectBtn['text']= 'Disconnect'
        self.connectBtn['command']= self.disconnect
        self.sendBtn['state'] = 'normal'
        
    def disconnect(self):
        self.server.close()
        self.ptField.setText('')
        self.drLabel['text'] = 'please enter your name to connect.'
        self.connectBtn['text'] = 'Connect'
        self.connectBtn['command'] = self.connect 
        self.sendBtn['state'] = 'disabled'
        
def main():
    
    DoctorClient().mainloop()

if __name__ == '__main__':
    main()
        
        
