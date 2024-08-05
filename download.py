import requests

n = int(input("soni: "))

for i in range(1, n + 1):
    response = requests.get('http://127.0.0.1:8000/rand/download-randomized-docx/')
    with open(f'tests/{i}.docx', 'wb') as f:
        f.write(response.content)
        f.close()
