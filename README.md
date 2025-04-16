# 🤖 Chatbot UI với OpenRouter và Streamlit by Khamtay

Đây là một ứng dụng chatbot đơn giản sử dụng mô hình AI qua [OpenRouter](https://openrouter.ai) và được xây dựng bằng Python với [Streamlit](https://streamlit.io).

---

## 🧰 Tính năng

- Giao diện chat đẹp mắt.
- Kết nối mô hình AI như `deepseek/deepseek-r1` qua OpenRouter API.
- Hiệu ứng "đang suy nghĩ..." khi bot trả lời.
- Lưu giữ lịch sử hội thoại.

---

## 🚀 Cài đặt & Chạy ứng dụng

### 1. Clone dự án hoặc tạo file mới

```bash
git clone https://github.com/KT246/chatbot-openrouter-streamlit.git
cd chatbot-openrouter-streamlit 
```` 
---
### 2. Cài đặt thư viện cần thiết

```bash
pip install -r requirements.txt
```

### 3. Chạy ứng dụng Streamlit

```bash
streamlit run app.py
```

## 🔐 Cấu hình API Key
Ứng dụng dùng OpenRouter API, bạn cần:
- Truy cập: https://openrouter.ai/keys
- Tạo API Key
- Dán key vào dòng api_key= trong app.py:

```bash
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-...YOUR_KEY_HERE..."
)
```
## 📂 Cấu trúc dự án
```bash
chatbot-openrouter-streamlit/
│
├── app.py              # Code chính của Streamlit Chatbot
├── requirements.txt    # Thư viện cần thiết
└── README.md           # Tài liệu hướng dẫn
```

