wordlist={'Hello':'Hi! there','How are u?':'I am fine, what about u'}
def chat_bot(user_input):
    keyss=0
    words=[str(z) for z in user_input.split()]
    for sentences in words:
        if(sentences in 'bye' ):
            keyss=1
            print("Ok, bye. See ya later")
            break
        if(sentences in wordlist.keys()):
                                       print(wordlist[sentences])
        else:
                                       print("I didn't get it")
    return keyss

print("Start Chatting With the Bot")
while(chat_bot(str(input()))!=1):
    continue
    
