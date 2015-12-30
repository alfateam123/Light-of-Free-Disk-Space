Light of the Free Disk Space: client
====================================

This is the "frontend" of the LFDS project.

## Installation ##

This procedures has been tested on Windows 10, using cygwin.
I prefer using Linux-like environments. If you're using a Mac, you should be ok too.

If you are a Windows fan... please, open a Pull Request adding Windows-specific installation notes:
your contribution will be appreciated!

```
virtualenv .lfds_client
source .lfds_client/bin/activate
pip install . -r requirements.txt

# modify the configuration to make it work
cp config.json.example config.json
notepad config.json

# start the script!
light_of_free_disk_space
```

## What should I see? ##

At first, the bigger led should be green.
According to the free disk space -as reported by the server-, the led
will change its color using the following rules:

* 100% free = blue
--> dark blue
* 50% free = black
--> light red
* 0% free = red

## I'm using a Mac, and the script is doing Windows-specific things! ##

Replace the following line in `bin/light_of_free_disk_space`

```py
COREPROPS = "C:/ProgramData/SteelSeries/SteelSeries Engine 3/coreProps.json"
```
with the Mac-specific path, as explained by [the official doc](https://github.com/SteelSeries/gamesense-sdk/blob/master/doc/api/sending-game-events.md#server-discovery).

Yes, you're right. This thing should be handled by pygamesense, and users should not see that.
Feel free to open an issue on [the pygamesense project repository](https://github.com/juliusmh/Python-Gamesense-Api).