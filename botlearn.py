import aiml
import os
k=aiml.Kernel()
k.verbose(True)
'''
k.loadBrain("Omegle.brn") # For just adding extra knowledge to the already created brain file.
'''
k.learn("YourFilename.aiml") # The file to be learned by the bot. Note all the previous knowledge will get replaced, if that is not what you intend than uncomment the above code.
k.saveBrain("Omegle.brn")
