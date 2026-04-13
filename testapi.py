print("RUNNING FILE: testapi.py")
print("MODEL USED:", "nousresearch/nous-capybara-7b")
import requests

API_KEY = "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"

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