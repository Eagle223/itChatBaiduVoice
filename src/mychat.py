#coding:utf-8
import itchat
import time
from itchat.content import *
import global_list
import RecordAPI
import BaiduVoiceTranslationAPI
import TcpSocket_client
import os


apiKey='XWZUnn2c9oujAuSrTSEOjE7h'
secretKey='96afeab10ed8287b719767728e13c78f'
        
def login(loginCB,exitCB):
    '''
    log in itchat
    '''
    if(loginCB==None or exitCB==None):
        itchat.auto_login(enableCmdQR=2)
        itchat.run()
        return
    itchat.auto_login(enableCmdQR=2,loginCallback=loginCB,exitCallback=exitCB)
    
    itchat.start_receiving()
    
            
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    datatosend='abc'
    print msg.text    
    datatosend=msg.text
    #TcpSocket_client.Tcp_Send(TcpSocket_client.SERVERIP,TcpSocket_client.PORT,datatosend)
    TcpSocket_client.SendCommand(str(msg.text.encode('utf-8'))) 
    return msg.text

@itchat.msg_register([PICTURE,RECORDING,ATTACHMENT,VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    
    print '@%s@%s'%({'Picture':'img','Video':'vid'}.get(msg['Type'],'fil'),msg['FileName'])
    filename='%s'%(msg['FileName'])
#    global_list.Mp3FileNameList=filename 
    destFileName=RecordAPI.Change_fileType(filename)
    VoiceTranslation =  BaiduVoiceTranslationAPI.BaiduVoiceHttpClient(apiKey,secretKey)
    VoiceRespone = VoiceTranslation.VocieTranslation("zh" ,1,destFileName,'pcm',16000)
    print VoiceRespone
    global_list.commandList.append(VoiceRespone)
    global_list.isNewComandComes=True
    os.system('rm -rf '+destFileName)
    #TcpSocket_client.Tcp_Send(TcpSocket_client.SERVERIP, TcpSocket_client.PORT, str(VoiceRespone.encode('utf-8')))
    TcpSocket_client.SendCommand(str(VoiceRespone.encode('utf-8')))    
    '''
    should replay the VoiceRespone to the sender
    '''
    
    return VoiceRespone
    
    
