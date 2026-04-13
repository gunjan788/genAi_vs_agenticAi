import streamlit as st
import requests

# 🔑 API KEY
API_KEY = "sk-or-v1-0080433114a9e7fad3a4cd112c5aeda77ad5a70892de87f4dc4bcf19dbf940e8Y"

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


# 🌐 PAGE CONFIG
st.set_page_config(page_title="GenAI vs Agentic AI", layout="wide")

# 🎯 HEADER
st.title("🤖 GenAI vs Agentic AI")
st.markdown("### 🚀 From Response Generation to Intelligent Reasoning")
st.divider()

# 📥 INPUT
topic = st.text_input("💡 Enter your topic:")

if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic!")
    else:

        with st.spinner("Thinking... 🤔"):

            # 🟢 SIDE BY SIDE LAYOUT
            col1, col2 = st.columns(2)

            # ========================
            # 🔹 GEN AI COLUMN
            # ========================
            with col1:
                st.markdown("## 🔹 Generative AI")
                st.caption("⚡ Single-step output generation")

                genai_prompt = f"Explain {topic} in 5-6 lines."
                genai_result = call_llm(genai_prompt)

                st.info(genai_result)

            # ========================
            # 🔸 AGENTIC AI COLUMN
            # ========================
            with col2:
                st.markdown("## 🔸 Agentic AI")
                st.caption("🧠 Multi-step reasoning system")

                # Plan
                plan = call_llm(f"Give ONLY 3 steps to solve/explain {topic}")
                st.markdown("### 🧠 Plan")
                st.write(plan)

                # Execution
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

                # Final
                final = call_llm("Summarize in 4-5 lines:\n" + " ".join(outputs))

                st.markdown("### 🔥 Final Output")
                st.success(final)

        st.divider()
        st.markdown("💬 *GenAI answers. Agentic AI thinks, plans, and solves.*")