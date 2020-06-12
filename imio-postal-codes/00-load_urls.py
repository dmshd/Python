
import webbrowser

urls = [
        'http://geoservices.wallonie.be/geolocalisation/doc/ws/index.xhtml',
        ]

counter = 0

for website in urls:
    webbrowser.open_new_tab(website)
    print("Loading " + website + "...")
    counter += 1

print(str(counter) + " websites loaded !")


