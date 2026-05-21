# 🐇 Talking Rabbitt – Conversational AI Analytics MVP

> *Ask questions. Get insights. Instantly.*

---

## 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-MVP-orange.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)


---

## 📌 Overview

**Talking Rabbitt** is a conversational intelligence layer that enables business leaders to interact with their data using **natural language queries** — no dashboards, no filters, no technical expertise required.

Instead of navigating complex BI tools, users can simply **ask questions about their data and receive instant insights with automatic visualizations.**

This repository contains the **MVP prototype** of Talking Rabbitt.

---

## 🎯 Demo Screenshot



<img width="451" height="713" alt="Screenshot 2026-03-11 181426" src="https://github.com/user-attachments/assets/c2910d53-1cf5-428d-8aed-8c597e9121ac" />


---

## 🚀 Live Demo

👉 **[Try Talking Rabbitt Now](https://talking-rabbitt-ai-analytics-mvp-iwxpbqowutubklvjdycauv.streamlit.app/)**  

---

## ❌ The Problem

Traditional analytics tools like:

- Microsoft Power BI
- Tableau
- Excel Pivot Tables

require users to:

- Navigate multiple dashboards
- Apply filters manually
- Create charts step by step
- Understand technical syntax

**This process is time-consuming, frustrating, and excludes non-technical users.**

| Tool | Time to Answer | Technical Skill Required |
|------|----------------|--------------------------|
| Excel | 5–10 min | Medium |
| Power BI | 5–15 min | High |
| Tableau | 5–15 min | High |
| **Talking Rabbitt** | **5 seconds** | **None** |

---

## ✅ The Solution

Talking Rabbitt introduces a **conversational query layer** on top of structured data.

### How it works:

1. 📂 **Upload** your CSV file
2. 💬 **Ask** a natural language question
3. 🤖 **Receive** instant text insight
4. 📊 **View** automated chart

### Example:

| User Question | System Output |
|---------------|---------------|
| *"Which region had the highest revenue?"* | ✅ *"Region with highest revenue: West"* + Bar chart |

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📁 CSV Upload | Drag & drop or browse files (up to 200MB) |
| 🔍 Dataset Preview | See your data before asking questions |
| 💬 Natural Language Query | Ask questions in plain English |
| ⚡ Instant Insights | Get text answers immediately |
| 📊 Dynamic Charts | Auto-generated bar charts for relevant queries |
| 🧠 Extensible | Easy to add more query patterns |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| Backend | Python 3.x |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| File Handling | CSV (native support) |

---

## 📁 Project Structure

```
talking-rabbitt/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── screenshot.png         # Demo screenshot
└── README.md              # This file
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/harleenkaurkambojgandhi-design/talking-rabbitt-ai-analytics-mvp
cd talking-rabbitt-ai-analytics-mvp
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

### 4. Open your browser

Navigate to `http://localhost:8501`

---

## 📦 requirements.txt

```txt
streamlit
pandas
matplotlib
```

---

## 💡 Sample Query Patterns

| Question Type | Example |
|---------------|---------|
| Highest value | *"Which region had the highest revenue?"* |
| (More coming soon) | *"What was total revenue by quarter?"* |

---

## ⏱️ The Magic Moment

| Before (Traditional) | After (Talking Rabbitt) |
|----------------------|-------------------------|
| Open Excel | Upload CSV |
| Find correct sheet | Type question |
| Apply filters | Hit enter |
| Create pivot table | ✅ Instant answer + chart |
| Build chart | |
| Copy to presentation | |
| **⏰ 10 minutes** | **⚡ 5 seconds** |

> **10 minutes → 5 seconds**  
> *That's the magic of conversational analytics.*

---

## 🔮 Future Enhancements

- [ ] Support for more question types (average, total, trends)
- [ ] Multiple chart types (line, pie, scatter)
- [ ] AI-powered NLP (OpenAI integration)
- [ ] Date-range filtering
- [ ] Export insights as PDF/PNG
- [ ] Multi-file uploads and joins

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Fork the repo
- Create a feature branch
- Submit a pull request

---

## 📄 License

MIT License — free for personal and commercial use.

---

## 🙏 Acknowledgments

Built with:
- Streamlit — rapid app development
- Pandas — data power
- Matplotlib — beautiful charts

---

> *"Stop navigating dashboards. Start asking questions."*  
> — **Talking Rabbitt** 🐇


```

## Support

If you find this project useful, please consider giving it a ⭐ star on GitHub to help others discover it.
