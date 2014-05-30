import aiml
import os
k=aiml.Kernel()
k.verbose(True)
k.learn("YourFilename.aiml") # The file to be learned by the bot
k.saveBrain("Omegle.brn")
