# Raspnode Config

### Motivation
I wanted to setup a raspbery pi as a Bitcoin, Litecoin, or Ethereum full node, but most of the documentation I found online was no longer maintained or hard to find. The guides at http://raspnode.com/ were invaluable for the initial phases, but I still encountered missing depdendencies and issues. While I was able to find the resources I needed and resolve any dependencies that were missing I thought that there might be others that might want to support the network, yet have difficulty getting started or give up due to fragmented resources. I decided that I'd try and consolidate the common steps and turn them into code. This way anybody-including myself-could use reproducible and versioned steps to set up a new node; I thought it would be smarter to represent the [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_Code).

_Note: a lot of the steps will have overlap to that of raspnode's_

### Hardware
I am using the following hardware:

- [Raspberry Pi 3](https://www.amazon.com/CanaKit-Raspberry-Complete-Starter-Kit/dp/B01C6Q2GSY/ref=sr_1_2?ie=UTF8&qid=1518376095&sr=8-2&keywords=canakit)
- [256 GB Flash Drive](https://www.amazon.com/SanDisk-Cruzer-Glide-3-0-256GB/dp/B01JHLJBO8/ref=sr_1_3?s=electronics&ie=UTF8&qid=1518376171&sr=1-3&keywords=256+flash+drive). 

_Note: The size of the blockchain may be substantially larger months or years from this post, ensure to get an external drive that can support the blockchain size. You can check the [blockchain sizes here](https://bitinfocharts.com/)_

### Equipment for Setup
- HDMI cable
- Monitor with HDMI in or adapters to convert HDMI to your monitor
- USB keyboard
- Router and a connection to the Internet

### Installation of the Rasbian OS
After initial assembly of the pi, I powered it on, hooked it up to the internet and installed the most basic rasbian os.

__TODO: PICTURES SETUP__

### Setup of External Drive
Take the external USB drive and ensure it's empty and using the file format FAT32. If you bought the 256 GB drive above it's (probably) already in the correct format. Empty it's contents and rename it, we will use the name for verifying the drive is using the correct file format.

Plug the USB  drive into your computer or raspberry, confirm the correct setup of the flash drive by typing `sudo blkid` into terminal and looking for a line in the output that looks like the following:

`/dev/sda1: LABEL="<your usb label>" UUID="<some id>" TYPE="vfat"`

If `TYPE="vfat"` then you're good to go. If not then you'll need to format the drive. 

__TODO: STEPS for formatting thd drive__

### Running the Setup script
To make things simple I've made a `setup.py` script that should be all that is needed to set up the node.
To get things started run:

`sudo python setup.py --currency-type <CURRENCY>`

where `<CURRENCY>` is `bitcoin`, `ethereum`, or `litecoin`
    
_NOTE: Be patient. The following tasks take the longest amount of time: Update & Upgrade apt packages, Configure Command, and the Make Command, with the Make Command taking the longest. It took ~ 1.5 hours for me._   

When the setup.py script finishes, reboot the pi.
`sudo reboot`

####Confirm the setup
TODO:

### Advanced
For those who are comfortable with the terminal, there are some additional parameters that are available
```
-h, --help            show this help message and exit
--skip-ansible-install
                    allows skipping of ansible install
-c CURRENCY_TYPE, --currency-type CURRENCY_TYPE
                    bitcoin, ethereum, litecoin
--smtp                if you have the smpt server, port, username, and
                    password you can set up alerting
-d, --dry-run         dry-run ansible playbook
```

Most of the parameters are pretty straight forward, but I want to point out one in particular, `--smtp`
As mentioned above, I'm using monit to monitor the processes as well as for alerting, using --smtp sets up the monit configuration to use a particular smtp server and send email alerts.

In order to get this to work you'll need to make a few changes to some file variables and run the setup script with an additional parameter.

TODO: what variables need to change

`sudo python setup.py --currency-type <CURRENCY> --smtp`

### Code Structure
```
.
├── playbook.yml
├── README.md
├── roles
│   ├── bitcoin
│   │   ├── meta
│   │   │   └── main.yml
│   │   ├── tasks
│   │   │   └── main.yml
│   │   └── vars
│   │       └── main.yml
│   ├── ethereum
│   │   ├── meta
│   │   │   └── main.yml
│   │   ├── tasks
│   │   │   └── main.yml
│   │   └── vars
│   │       └── main.yml
│   ├── litecoin
│   │   ├── meta
│   │   │   └── main.yml
│   │   ├── tasks
│   │   │   └── main.yml
│   │   └── vars
│   │       └── main.yml
│   └── monit
│       ├── defaults
│       │   └── main.yml
│       ├── tasks
│       │   └── main.yml
│       └── vars
│           └── main.yml
├── run_ansible.py
└── vars
    └── general.yml
```

The code is broken up into three main roles: bitcoin, ethereum, and litecoin which depend on another role, monit.
Due to the similar nature of setup, `playbook.yml` handles the common setup while the indiviual roles for bitcoin, litecoin, and ethereum are specific. Monit is used to monitor the 'node' process so that if the daemon that is running the the client were to vanish or disappear it would restart that process ensuring that it running. This also means that in the event of a power outage monit will automatically handle the startup of the node. I also use monit as an alerting system to send me an email if a process does go down. The advanced section contains more about alerting and the setup of a smtp server.

### Resources
- https://bitinfocharts.com/
- http://raspnode.com/
