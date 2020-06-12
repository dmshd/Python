import webbrowser

urls = [
        'https://realpython.com/python-json/',
        'https://docs.python.org/fr/3.6/tutorial/datastructures.html'
        ]

counter = 0

for website in urls:
    webbrowser.open_new_tab(website)
    print("Loading " + website + "...")
    counter += 1

print(str(counter) + " websites loaded !")
  
