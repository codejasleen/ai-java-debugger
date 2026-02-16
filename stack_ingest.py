import requests

URL = "https://api.stackexchange.com/2.3/questions"

params = {
    "order": "desc",
    "sort": "activity",
    "tagged": "java",
    "site": "stackoverflow",
    "pagesize": 20
}

response = requests.get(URL, params=params)
data = response.json()

questions = data.get("items", [])

with open("data/stack_java_errors.txt", "w", encoding="utf-8") as f:
    for q in questions:
        title = q.get("title", "")
        f.write(title + "\n")

print("Fetched and stored", len(questions), "Java debugging questions.")
