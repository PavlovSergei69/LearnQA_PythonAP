import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
first_responce = response.history[0]
second_responce = response.history[1]
third_responce = response


print(first_responce.url)
print(second_responce.url)
print(third_responce.url)