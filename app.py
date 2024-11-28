import requests

name = input("What's your name ? ")
r = requests.get("https://api.agify.io?name=" + name + "&country_id=BE")
result = r.json()
age = str(result.get('age'))
print("The estimated age for " + name + " is " + age + ".")
