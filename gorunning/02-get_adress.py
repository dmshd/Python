# this was made following https://automatetheboringstuff.com/2e/chapter12/

# 1 Gets a street adress from the command line arguments or clipboard
# 2 Opens the web browser to the OpenStreetMap page for the adress
#  the code will need to read the command line arguments from sys.argv
#  and read the clipboard contents
# call the webbrowser.open()

# It needs to be launched like "02-get_adress.py 1 Rue Léon Morel, 6000, Charleroi".
# If there no arguments it will takes what's in clipboard.

# I tested to look for 'Boulevard Audent 6000 Charleroi' on OpenStreetMap.com
# and looked at the url which is : 'https://www.openstreetmap.org/search?query=51%20Boulevard%20audent%206000%20charleroi#map=19/50.40978/4.44582'
# I think #map=... is not required. It seems added after the searching
# We will open a map by openning 'https://www.openstreetmap.org/search?query=Location_Number%20Street%20Adress%20Postal_Code%20City'

# Let's do this following automatetheboringstuff tutorial :

#! python3

import webbrowser, sys
if len(sys.argv) > 1:
    # Get adress from command line.
    address = '%20'.join(sys.argv[1:])
    webbrowser.open('https://www.openstreetmap.org/search?query=' + address)
    # information from the tutorial : 
    # Command line arguments are usually separated by spaces, but in this case, you want to interpret all of the arguments as a single string. Since sys.argv is a list of strings, you can pass it to the join() method, which returns a single string value. You don’t want the program name in this string, so instead of sys.argv, you should pass sys.argv[1:] to chop off the first element of the array. (#https://automatetheboringstuff.com/2e/chapter12/)
   # I use '%20' for put spaces in the url php query
else:
    print(">>> An arg is needed")

