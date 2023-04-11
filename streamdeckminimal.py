# Streamdeck addon
# https://python-elgato-streamdeck.readthedocs.io/en/stable/pages/backend_libusb_hidapi.html

import os
import threading

from PIL import Image, ImageDraw, ImageFont
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper

# Folder location of image assets used by this example.
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "Assets")

# Generates a custom tile with run-time generated text and custom image via the
# PIL module.
def render_key_image(deck, icon_filename, font_filename, label_text):
    # Resize the source image asset to best-fit the dimensions of a single key,
    # leaving a margin at the bottom so that we can draw the key title
    # afterwards.
    #icon = Image.open(icon_filename)
    #image = PILHelper.create_scaled_image(deck, icon, margins=[0, 0, 20, 0])
    W, H = (72,72)
    image = Image.new('RGB',(W,H), "black")

    # Load a custom TrueType font and use it to overlay the key index, draw key
    # label onto the image a few pixels from the bottom of the key.
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_filename, 14)
    
    w,h = font.getsize(label_text)
    #draw.text((image.width / 2, image.height / 2), text=label_text, font=font, fill="white")
    draw.text(((W-w)/2,(H-h)/2), label_text, font=font, fill="white")
    return PILHelper.to_native_format(deck, image)


# Returns styling information for a key based on its position and state.
def get_key_style(deck, key, text):
  
    
    name = "Ausgabe"
    icon = "{}.png".format("Released")
    font = "Arial.ttf"
    label = text

    return {
        "name": name,
        "icon": os.path.join(ASSETS_PATH, icon),
        "font": os.path.join(ASSETS_PATH, font),
        "label": label
    }

# Creates a new key image based on the key index, style and current key state
# and updates the image on the StreamDeck.
def update_key_image(deck, key, text):
    # Determine what icon and label to use on the generated key.
    key_style = get_key_style(deck, key, text)

    # Generate the custom key with the requested image and label.
    image = render_key_image(deck, key_style["icon"], key_style["font"], key_style["label"])

    # Use a scoped-with on the deck to ensure we're the only thread using it
    # right now.
    with deck:
        # Update requested key with the generated image.
        deck.set_key_image(key, image)






def update_key(key,text):
    streamdecks = DeviceManager().enumerate()
    print("Found {} Stream Deck(s).\n".format(len(streamdecks)))
    for index, deck in enumerate(streamdecks):
        # This example only works with devices that have screens.
        if not deck.is_visual():
            continue

        deck.open()
        

        print("Opened '{}' device (serial number: '{}', fw: '{}')".format(
            deck.deck_type(), deck.get_serial_number(), deck.get_firmware_version()
        ))
        # Set initial key images.
        update_key_image(deck, key, text)
        

        # Register callback function for when a key state changes.
        #deck.set_key_callback(key_change_callback)

        # Wait until all application threads have terminated (for this example,
        # this is when all deck handles are closed).
        #for t in threading.enumerate():
        #    try:
        #        t.join()
        #    except RuntimeError:
        #        pass