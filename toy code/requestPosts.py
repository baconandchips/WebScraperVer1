import requests


my_data = {"name": "Me", "email": "emailofme@example.com"}
r = requests.post("http://www.w3schools.com/php/welcome.php", data = my_data)

f = open("myfile.html", "w+")
f.write(r.text)
# can open in browser to see how it looks!
# type in the info as we listed, and it the W3School should display back to us something

