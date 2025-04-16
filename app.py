import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# --- API Client Setup ---
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# --- Streamlit UI Setup ---
st.set_page_config(page_title="Chatbot with Animation", layout="centered")
st.title("🤖 Chatbot with Thinking Animation")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Xin chào! Bạn cần giúp gì hôm nay?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input from user
prompt = st.chat_input("Nhập tin nhắn...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Thinking Animation ---
    with st.chat_message("assistant"):
        thinking_placeholder = st.empty()
        thinking_placeholder.markdown("Đang suy nghĩ...")

    try:
        # Gọi API
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1",
            messages=st.session_state.messages,
            extra_headers={
                "HTTP-Referer": "https://your-site.com",
                "X-Title": "Chatbot with Animation",
            },
            extra_body={},
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"❌ Lỗi: {e}"

    # Cập nhật phản hồi
    st.session_state.messages.append({"role": "assistant", "content": reply})
    thinking_placeholder.markdown(reply)
