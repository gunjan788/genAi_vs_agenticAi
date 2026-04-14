print("RUNNING FILE: testapi.py")
print("MODEL USED:", "nousresearch/nous-capybara-7b")
import requests

API_KEY = "your_api_key"

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "openai/gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "Hello, test message"}
    ]
}

try:
    response = requests.post(url, headers=headers, json=data)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("\nAI Response:\n")
        print(response.json()["choices"][0]["message"]["content"])
    else:
        print("\nError:\n")
        print(response.text)

except Exception as e:
    print("Exception occurred:", e)
