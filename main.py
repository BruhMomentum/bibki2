import string
import random
import requests
from keep_alive import keep_alive

def randomword(length):
   letters = string.ascii_letters + string.digits
   return ''.join(random.choice(letters) for i in range(length))

def quickChecker(url):
  global nitrochecker
  url2 = f"https://discordapp.com/api/v9/entitlements/gift-codes/{url}?with_application=false&with_subscription_plan=true"
  response = requests.get(url2)  # Get the response from discord
  if response.status_code == 200:
    print(f'{url} - True!')
    url= f"https://http.trashcan5.repl.co/nitro/?nitro={url}"
    requests.get(url)
  else:
    print(f'{url} - False')

keep_alive()
while True:
  try:
    code = randomword(16)
    url = f"https://discord.gift/{code}"  # Generate the url
    quickChecker(url)  # Check the codes
  except:
    url = f'https://http.trashcan5.repl.co/error/?error=nitro1'
    requests.get(url=url)