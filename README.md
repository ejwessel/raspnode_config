# Raspnode Config

### Motivation
I wanted to setup a raspbery pi as a Bitcoin, Litecoin, or Ethereum full node, but most of the resources I found online were no longer maintained, hard to find, or had fragmented steps. For example, when I started I was following the guides at http://raspnode.com/. These steps were invaluable for the initial phases, but unfortunately, "it is currently no longer being maintained but will remain online in case people find the tutorials useful." While I was able to find the resources I needed and resolve any dependencies that were missing I thought that there might be other people out there that might want to support the network, yet have difficulty getting started or give up due to fragmented resources. I decided that I'd try and consolidate the common steps and turn them into code - if not for others then for myself since I wanted reproducible versioned steps that I could apply to multiple machines; everything can be [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_Code) 

### Hardware
I am using the following hardware:

- [Raspberry Pi 3](https://www.amazon.com/CanaKit-Raspberry-Complete-Starter-Kit/dp/B01C6Q2GSY/ref=sr_1_2?ie=UTF8&qid=1518376095&sr=8-2&keywords=canakit)
- [256 GB Flash Drive](https://www.amazon.com/SanDisk-Cruzer-Glide-3-0-256GB/dp/B01JHLJBO8/ref=sr_1_3?s=electronics&ie=UTF8&qid=1518376171&sr=1-3&keywords=256+flash+drive). 

_Note: The size of the blockchain may be substrantially larger months or years from this post, ensure to get an external drive that can support the blockchain size. You can check the [blockchain sizes here](https://bitinfocharts.com/)_

### Equipment for Setup
- HDMI cable
- Monitor with HDMI in or adapters to convert HDMI to your monitor
- USB keyboard
- Router and a connection to the Internet

### Installation of the Rasbian OS
After initial assembmly of the pi, I powered it on, hooked it up to the internet and installed the most basic rasbian os.
TODO: PICTURES SETUP

### Setup of External Drive
Take the external USB flash drive and ensure it's both empty and using the file format FAT32. If you bought the 256 GB drive above it's (probably) alredy in the correct format, you just need to empty it.

In order for the setup script to work, we'll need to insert the flash drive into the bottom right USB port. This is configurable in the script, but the script expects it to be in that spot to automount the drive if the pi is to restart. 

TODO: PICTURE ATTACHED

You can confirm the correct setup of the flash drive by typing `sudo blkid` into terminal and looking for a line that looks like the following:

`/dev/sda1: LABEL="<your usb label>" UUID="<some id>" TYPE="vfat"`

### Code Structure

### Setup

### Advanced

### Resources
