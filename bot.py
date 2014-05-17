import aiml
import os
k=aiml.Kernel()
k.verbose(True)
homedir=os.getcwd()
lists=os.listdir('./')
for item in lists:
    if (item[len(item)-4:])=='aiml':
        k.learn(item)
k.loadBrain("Omegle.brn")
k.setPredicate("name","PARI")
k.setPredicate("master","pkoli")
print ("Enter something")
while(1):
    print(k.respond(raw_input()))
k.saveBrain("Omegle.brn")
