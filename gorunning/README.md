# BetterGoRunning

http://gorunning.be/calendrier_fr.php

The idea is to make a good looking and fun to navigate agenda of the runs.
A problem I encoutered on the current listing is : there is no way to look for runs happening near a position. Imposible to specify 'show me the runs max 15km near this post code (by example). You can only look for a post code and the website returns only the events corresponding exactly to the criteria. We would like a "You might be interested by" functionnality.

At the moment, you can look for  
* month (a SELECT field).
* date (a SELECT field listing ['01', '02', ... '30' '31'] as days and a field listing ['Janvier 2020', etc...]).
* Location (Namur, Bruxelles, ... It's a text field).
* Postal code (5000, 6000, ... It's a text field).
* Course name (a text field).
and a Search button.

Under that form stands a table with columns listing events by these criterias.

I could simply email the webmaster and ask for a excel file to experiment or an API endpoint if there is one but that would be less fun. (Maybe later)

Let's investigate if we can scrap the data with Python.

#### 01-webbrowser.py
is a simple experimentation (I'm following 'borin stuff with python' tutorial) about using webbrowser package to open the browser. It's just what it does.

#### 02-get_adress.py
It' does not do what the name indicate
`╰─$ python 02-get_adress.py 51 boulevard audent charleroi` opens webbrowser on the specified adress on open street map which is cool.





