import aiml
import urllib2 as url
import urllib
import os
import time
import commands
k = aiml.Kernel()
replyin=["hey","What's up","asl","Howdy","How are you"] #Specify random compliments
replyout=["Are u still there","Hello, anybody still there","Is anyone still listening to me"] #To check if the stranger is still online
k.bootstrap(brainFile = "Omegle.brn") #Brain file
k.setBotPredicate("name","PAIC") #Name of the bot
k.setBotPredicate("master","pkoli(My Creator)") #Name of the creator
k.setBotPredicate("age","Well, i've lost the track of my age") #Age of the bot
k.setBotPredicate("gender","Female") #Gender of the bot
def fmtId( string ): 
    return string[1:len( string ) - 1]

def listenServer( id, req ):
    from time import time
    import random
    while True:
        
        site = url.urlopen(req)
        rec = site.read()
        if 'waiting' in rec:
            print("Waiting...")
            t=time()
            msg=replyin[random.randint(0,len(replyin)-1)] #Greet the stranger
            talk(id,req,msg)
            
        elif 'strangerDisconnected' in rec:
            print('Stranger Disconnected!')
            t=time()
            omegleConnect() #Reconnect to Omegle
 
        elif 'connected' in rec:
            print('Found one')
            t=time()
 
        elif 'typing' in rec:
            print("Stranger is typing...")
            t=time()
        elif 'gotMessage' in rec:
            input=rec[17:len( rec )]
            input=input[:input.index('"')]
            print "Stranger:",input
            msg=k.respond(input) #Reply to the strangers input
            talk(id,req,msg)
            t=time()
        if(time()-t>30):#If the stanger doesn't reply for a long time waits around 30s
            msg=replyout[random.randint(0,len(replyout)-1)] #Check if the stranger is still online
            talk(id,req,msg)
            #print (time()-t)
            if(time()-t>60):#Disconnects if the stranger doesn't reply.
                omegleConnect()
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
    print(id) #Displays the id with which we login to Omegle
    req = url.Request('http://omegle.com/events', urllib.urlencode( {'id':id}))
    print('Finding stranger...')
    listenServer(id,req)
    
omegleConnect()
