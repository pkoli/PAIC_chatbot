import aiml
import os
k=aiml.Kernel()
k.verbose(True)
k.learn("YourFilename.aiml") # The file to be learned by the bot. Note all the previous knowledge will get replaced, if that is not what you want than remove this line and uncomment the following two lines.
'''
k.loadBrain("Omegle.brn") # For just adding extra knowledge to the already created brain file.
k.learn("Yourfilename.aiml")
'''
k.saveBrain("Omegle.brn")
