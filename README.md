# Instagram-selfiebooth-python
This is a Selfie Booth that uses a Raspberry Pi to take pictures and sends them to Instagram. It takes a picture of you when you sit down and edits the picture before sending it to a pre-destined Instagram account. 

I have split this up into 2 parts – the capturing of image and uploading the image to Instagram. 

## Part 1: Capturing the image
Things you will need: 
1.	Raspberry Pi (I’m using Raspberry Pi 2)
2.	Raspberry Pi Camera (you can also use a USB camera but you’ll have to modify the code)
3.	Light source (I used Christmas/fairy lights)
4.	Relay
5.	Battery pack that can hold 4 AA batteries
6.	Wires
7.	LED lights 
8.	Wires (female & male pin connectors)
9.	Duct/electrical tape

### Install and use the PiCamera
Install the Raspberry Pi Camera module by inserting the cable into the Raspberry Pi. The cable slots into the connector situated between the Ethernet and HDMI ports, with the silver connectors facing the HDMI port.

Boot up your Raspberry Pi and from the prompt, run 
```
sudo apt-get update && sudo apt-get upgrade
```

After that, run 
```
sudo raspi-config
```
and make sure camera is “enabled”. 

Run 
```
vcgencmd get_camera
```
and make sure that the PiCamera is supported and detected. 

### Connecting the hardware to Raspberry Pi
![raspi hardware](https://user-images.githubusercontent.com/41287923/42916041-c49b0f18-8b35-11e8-97d7-b5f7e46cdf67.png)

The fairy lights are only turned on when a picture is being taken so you will need a relay to turn the fairy lights on and off on command. You will need to connect the button such that the battery pack is connected between the Raspberry Pi and button.

