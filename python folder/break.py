import webbrowser
import time
link=["https://www.youtube.com/watch?v=RE87rQkXdNw","https://www.youtube.com/watch?v=57VIiRMhSsA",
      "https://www.youtube.com/watch?v=le2taK4vstQ","https://www.youtube.com/watch?v=Ofy0aAXiVpg"]
counter=0
while True:
    if counter>3:
        counter=0
    time.sleep(60*10)
    webbrowser.open(link[counter])
    counter+=1
