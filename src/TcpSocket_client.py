#coding:utf-8

import socket
import mysql

SERVERIP='192.168.219.1'
PORT=8008


def SendCommand(VoiceResponse):
    '''
    '''
    if(str("打开客厅灯，")==VoiceResponse):
        mysql.insert_mysql('11')
        return
    if(str("关闭客厅灯，")==VoiceResponse):
        mysql.insert_mysql('10')
        return    
    if(str("打开卧室灯，")==VoiceResponse):
        mysql.insert_mysql('21')
        return
    
    if(str("关闭卧室灯，")==VoiceResponse):
        mysql.insert_mysql('20')
        return
    if(str("打开排气扇，")==VoiceResponse):
        mysql.insert_mysql('31')
        return        
    if(str("关闭排气扇，")==VoiceResponse):
        mysql.insert_mysql('30')
        return  
    if(str("打开浴室灯，")==VoiceResponse):
        mysql.insert_mysql('41')
        return        
    if(str("关闭浴室灯，")==VoiceResponse):
        mysql.insert_mysql('40')
        return
        
    if(str("打开卧室台灯，")==str(VoiceResponse)):
        mysql.insert_mysql('51')
        return        
    if(str("关闭卧室台灯，")==str(VoiceResponse)):
        mysql.insert_mysql('50')
        return
    if(str("打开阳台灯，")==str(VoiceResponse)):
        mysql.insert_mysql('61')
        return        
    if(str("关闭阳台灯，")==str(VoiceResponse)):
        mysql.insert_mysql('60')
        return
    return

def Tcp_Send(ip,port,msg):
    
    socket.setdefaulttimeout(10)
    TcpClient=socket.socket()    
    try:    
        TcpClient.connect((ip,port))
    except:
        print "connection false"
        return False
    try:
        TcpClient.sendall(msg)
    except:
        print "send error"
        return False
    TcpClient.close()
    return True
    
