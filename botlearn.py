import aiml
import os
k=aiml.Kernel()
k.verbose(True)
'''
k.loadBrain("Omegle.brn") # For just adding extra knowledge to the already created brain file.
'''
k.learn("YourFilename.aiml") # The file to be learned by the bot. Note all the previous knowledge will get replaced, if that is not what you want than remove this line and uncomment the above line.
k.saveBrain("Omegle.brn")
