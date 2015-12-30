Light of the Free Disk Space: server
====================================

This is the "backend" of the LFDS project.

## Installation and setup ##

This procedure has been tested on ArchLinux ARM.

```
pacman -S python python-virtualenv
virtualenv .lfds_backend
source .lfds_backend/bin/activate
pip install flask flask-responses psutil
```

After the execution of the previous commands,
you did a correct setup of the environment.

Still, you need a little more work:

1. Update `free_disk_space.sh`: set the right folder the server will be launched,
and the virtualenv position.

2. Update the `ExecStart` of `free_disk_space.service` file. Not necessary if you're not going to use systemd.

Now, everything is ok and you can start the server.

## Usage via command line ##

Please use `free_disk_space.sh` to start 
the server: it will activate the right virtualenv
before running the flask server.

## Run at startup with systemd ##

A simple systemd service unit file is provided.
It can be integrated to start the server when 
the Raspberry Pi (or your own server!) boots up.

As explained in [NetworkTarget @ wiki.freedesktop](https://wiki.freedesktop.org/www/Software/systemd/NetworkTarget/), you need to enable `NetworkManager-wait-online`
or `systemd-networkd-wait-online` services, according to 
the network initialization system you're using.

After that, copy the `free_disk_space.service` file in
the `/etc/systemd/system/` folder and run
`systemctl enable free_disk_space`.

Now you're ready to `reboot`, wait a bit and 
check if the server is online.

## Run at startup with other init systems ##

Even though I know how to start and stop processes using other
init systems (OpenRC and upstart), I don't know how
to configure them to run things at startup.
If you want to contribute, that's a good place to start!

## How do I check everything is ok? ##

Fire up your browser at http://<raspberry_ip>:5000/space.
If you see a JSON response, everything is ok.
