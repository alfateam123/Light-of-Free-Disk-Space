Light Of [Free Disk] Space
===========================

What would you do with a RPi and a GameSense-enabled mouse?
That's obvious: make your mouse a free disk space notifier!

Let your mouse light its LEDs with different colours, according
to the available disk space on your RPi.
Useful if you use it as a downloading machine and you want a colorful~ notifier.

"Why?", you may wonder. It's Christmas, and I'm bored.

## Installation notes ##

This project is separated into two components:

* server
  a simple Flask server that returns a JSON

* client
  a client that requests the percentage of free disk space
  to the Flask server and updates the mouse LEDs via SteelSeries
  Engine's API.

Please check the `server` and the `client` folders
to read the installation notes of each component.
