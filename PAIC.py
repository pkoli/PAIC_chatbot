import aiml
import urllib2 as url
import urllib
import os
import time
import commands 
k = aiml.Kernel()
k.learn("omegle.aiml")
k.bootstrap(brainFile = "Omegle.brn")	
k.setPredicate("name","PARI")
k.setPredicate("master","pkoli")
def fmtId( string ):
 
    return string[1:len( string ) - 1]
 

def listenServer( id, req ):
 
    while True:
        
         
        site = url.urlopen(req)
        rec = site.read()
        if 'waiting' in rec:
            print("Waiting...")
 
        elif 'strangerDisconnected' in rec:
            print('Stranger Disconnected!')
            omegleConnect()
 
        elif 'connected' in rec:
            print('Found one')
            print(id)
            talk(id,req,"Hey")
 
        elif 'typing' in rec:
            print("Stranger is typing...")
 
        elif 'gotMessage' in rec:
            input=rec[17:len( rec )]
            print(input.index('"'))
            input=input[:input.index('"')]
            print "Stranger:",input
            msg=k.respond(input)
            talk(id,req,msg)
def talk(id,req,msg):
    typing = url.urlopen('http://omegle.com/typing', '&id='+id)
    typing.close()
    time.sleep((len(msg))/5) 
    print "You:",msg
    msgReq = url.urlopen('http://omegle.com/send', '&msg='+msg+'&id='+id)
    msgReq.close()
    return 0

def omegleConnect():
 
    site = url.urlopen('http://omegle.com/start','')
    id = fmtId( site.read() )
    print(id)
    req = url.Request('http://omegle.com/events', urllib.urlencode( {'id':id}))
    print('Finding stranger...')
    listenServer(id,req)
    
omegleConnect()
