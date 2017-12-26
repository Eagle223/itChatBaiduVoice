#coding:utf-8

import socket
import threading
import global_list
import time

class TcpSocket_Server(threading.Thread):
    connList=[]
    TcpServer=''
    port=0
    
    def __init__(self,port):
        threading.Thread.__init__(self)
        self.port=port
    
    def BuildServer(self):
        '''
        '''
        self.TcpServer=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        name=socket.gethostname()
        self.TcpServer.bind((name,self.port))
        self.TcpServer.listen(5);
    def run(self):
        self.BuildServer()        
        while(True):
            print "thread runing"
            conn,addr=self.TcpServer.accept()            
            if(None==conn):
                continue
            self.connList.append(conn)
            print "已经接收到",addr
            conn.send('欢迎访问'.encode("UTF-8"))
            if(global_list.isNewComandComes):
                conn.send('欢迎访问'.encode("UTF-8"))
            
            time.sleep(2)
            

            
        
        