# streamdeck_navitool addon
Stream Deck Extension for valalols navitool for star citizen

It will write the text to the buttons seen in the screenshot. \
The Satellite Button triggers for me the Autohotkey script for typing /showlocation \
The "Navitool" button starts the navitool from valalol

Installation: \
copy the files to your NaviTool installation from valalol's tool (https://github.com/Valalol/Star-Citizen-Navigation) 

pip install -r requirements.txt \
hideapi-win needs to get extracted and the dll and the other 2 files copied to e.g. windows/system32 

Usage: \
as in the screenshot, i have a subpage with 2 buttons, the satellite which triggers the hotkey f24 for me, \
which is hooked up to a autohotkey script triggering the /showlocation command \
and the Navitool button which launches the exe of the tool itselve... \
Rest of buttons will get filled with information when the tool starts the planetary navigation. \
The included Database.json is a unofficial version with Sandcaves and Rivers included.

![alt text](https://github.com/doabigcheese/streamdeck_navitool/blob/main/streamdeck.jpg?raw=true)
