# Filedetector
Check a specific folder if a new file is created in it and send it to discord 

## Prerequisites
Needs python3 to work
```bash
python3 --version
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip3 install -r requirements.txt
```
* Directly download packages:
```
pip3 install dhooks==1.1.4
pip3 install inotify==0.2.10
```

### Discord
To see how the tool works,
1. Create server.
2. Create and copy server [webhook](https://discordjs.guide/popular-topics/webhooks.html#fetching-all-webhooks-of-a-guild) and use in sample code.
   ```python3
   from dhooks import Webhook, File, Embed
   hook = Webhook('WEBHOOK')
   file = File('file path', name='name')
   embed.add_field(name='file name',  value='message')
   hook.send('message', file=file, embed=embed) #send file
   ```
3. Run sample code.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
