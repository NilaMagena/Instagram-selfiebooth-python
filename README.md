# Instagram-selfiebooth-python
This is a Selfie Booth that uses a Raspberry Pi to take pictures and sends them to Instagram. It takes a picture of you when you sit down and edits the picture before sending it to a pre-destined Instagram account. 


## Part 1: Capturing the image

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

### [Connecting the hardware to Raspberry Pi](https://makershare.com/portfolio/nila-govindaraju?tab=public)


Run the 
```
capture.py
```
code using the command prompt. It should take pictures when the button closes the circuit. 

## Part 2: Uploading the image
You'll need this code installed to run the upload.py code
[Instagram-API-python](https://github.com/LevPasha/Instagram-API-python) code

Run the 
```
upload.py
```
code on another command prompt. 

