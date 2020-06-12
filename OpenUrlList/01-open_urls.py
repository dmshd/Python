import webbrowser

urls = [
        'https://www.gmail.com',
        'https://www.inoreader.com',
        'https://www.developpez.com/',
        'https://www.meteobelgique.com',
        'https://github.com/dmshd/Python',
        'https://docs.python.org/3.7/library/webbrowser.html?highlight=webbrowser'
        ]

counter = 0

for website in urls:
    webbrowser.open_new_tab(website)
    print("Loading " + website + "...")
    counter += 1

print(str(counter) + " websites loaded !")
  
