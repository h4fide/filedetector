import inotify.adapters
import os
from dhooks import Webhook, File, Embed
import time
import sys

notifier = inotify.adapters.Inotify()
folder = r'FOLDER PATH' #PUT '/' AT THE END OF THE PATH'  
hook = Webhook('WEBHOOK')
watch = notifier.add_watch(folder)
embed = Embed(
    description='FileSpotter',
    color=0x5CDBF0
    )

print('Started')
for event in notifier.event_gen():
    if event is not None:
        if 'IN_CREATE' in event[1]:
            filename = event[3]
            filepath = folder + filename
            print("Okay somthing new here called: " + filename + '\nNow i will send it to discord')
            time.sleep(2)
            file = File(filepath, name=filename)
            embed.add_field(name=filename,  value='Voila :smiling_face_with_3_hearts: ')
            hook.send('New File', file=file, embed=embed)
            print("Send it :)")
            
            #time.sleep(10)  
            #os.remove(filepath) if you want to delete the file after
            #print(filename + " Has been removed")
            #sys.exit("Quiting...")
