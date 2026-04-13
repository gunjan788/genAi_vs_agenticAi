import streamlit as st
import requests

#  API KEY
API_KEY = "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"

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "GenAI vs Agentic AI"
}

MODEL = "openai/gpt-4o-mini"


def call_llm(prompt):
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.text}"


#  UI START
st.set_page_config(page_title="GenAI vs Agentic AI", layout="centered")

st.title("🤖 GenAI vs Agentic AI Demo")

topic = st.text_input("Enter your topic:")

if st.button("Generate"):
    
    if topic.strip() == "":
        st.warning("Please enter a topic!")
    else:

        #  GEN AI
        st.subheader("🔹 GenAI Output")
        genai_prompt = f"Explain {topic} in 5-6 lines."
        genai_result = call_llm(genai_prompt)
        st.write(genai_result)

        #  AGENTIC AI
        st.subheader(" Agentic AI Output")

        # Step 1: Plan
        plan = call_llm(f"Give ONLY 3 steps to solve/explain {topic}")
        st.markdown("###  Plan")
        st.write(plan)

        # Step 2: Execution
        steps = plan.split("\n")[:3]
        outputs = []

        st.markdown("###  Execution")

        for step in steps:
            if step.strip() == "":
                continue

            result = call_llm(f"Explain in 2-3 lines: {step}")
            st.write(f" {step}")
            st.write(result)
            outputs.append(result)

        # Step 3: Final summary
        final = call_llm("Summarize in 4-5 lines:\n" + " ".join(outputs))

        st.markdown("###  Final Output")
        st.write(final)