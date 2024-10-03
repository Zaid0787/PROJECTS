import requests
import json
import win32com.client as wincom
from pyttsx3 import speak

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
# print(r.text)
dic = json.loads(r.text)
# print(dic["current"]["temp_c"])
w = dic["current"]["temp_c"]

speak = wincom.Dispatch("SAPI.SpVoice")

text = (f"The current weather in {city} is {w} degrees")
speak.Speak(text)