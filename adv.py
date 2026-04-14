import streamlit as st
import requests

#  API KEY
API_KEY = "your_api_key"

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


#  PAGE CONFIG
st.set_page_config(page_title="GenAI vs Agentic AI", layout="wide")

st.title("🤖 GenAI vs Agentic AI")
st.markdown("### 🚀 From Response Generation to Intelligent Reasoning")
st.divider()

#  CHAT INPUT
topic = st.chat_input("💬 Enter your topic...")

if topic:

    st.chat_message("user").write(topic)

    with st.spinner("Thinking... 🤔"):

        #  TABS START HERE
        tab1, tab2 = st.tabs(["🔹 Generative AI", "🔸 Agentic AI"])

        # =====================
        #  GEN AI TAB
        # =====================
        with tab1:
            st.subheader("🔹 Generative AI")
            st.caption("⚡ Single-step response generation")

            genai_result = call_llm(f"Explain {topic} in 5-6 lines")

            st.info(genai_result)

        # =====================
        #  AGENTIC AI TAB
        # =====================
        with tab2:
            st.subheader("🔸 Agentic AI")
            st.caption("🧠 Multi-step reasoning and execution")

            #  PLAN
            plan = call_llm(f"Give ONLY 3 steps to solve/explain {topic}")

            st.markdown("### 🧠 Plan")
            st.info(plan)

            #  EXECUTION
            steps = plan.split("\n")[:3]
            outputs = []

            st.markdown("### ⚙️ Execution")

            for step in steps:
                if step.strip() == "":
                    continue

                result = call_llm(f"Explain in 2-3 lines: {step}")

                st.write(f"➡️ {step}")
                st.success(result)

                outputs.append(result)

            #  FINAL OUTPUT
            final = call_llm("Summarize in 4-5 lines:\n" + " ".join(outputs))

            st.markdown("### 🔥 Final Output")
            st.success(final)

    st.divider()
    st.markdown("💬 *GenAI answers. Agentic AI thinks, plans, and solves.*")
