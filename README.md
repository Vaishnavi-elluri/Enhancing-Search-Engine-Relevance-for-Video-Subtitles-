# 🎵 Shazam Clone: Audio Transcription & Subtitle Search
## 📌 Overview
### This project enhances search relevance for video subtitles by leveraging Natural Language Processing (NLP) and Machine Learning (ML). It allows users to search subtitles using audio queries, just like Shazam does for music! 🎶🔍

## 🏆 Key Features
### ✅ 🎙️ Audio to Text – Convert speech into text using AssemblyAI.
### ✅ 🔍 Semantic & Keyword-Based Search – Find subtitles with exact words or meaning-based search.
### ✅ 🧠 Deep Learning – Uses Sentence Transformers (BERT) for semantic understanding.
### ✅ ⚡ Fast Retrieval – Stores embeddings in ChromaDB for quick searches.
### ✅ 🎬 Large Subtitle Dataset – Processes over 82,000 subtitle files from movies & TV shows.

## 🛠 Tech Stack
### 🔹 Python 🐍
### 🔹 Pandas🐼
### 🔹 AssemblyAI 🎙️
### 🔹 ChromaDB 🗄️
### 🔹 SQLite 🗃️

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/shazam-clone.git
cd shazam-clone
### 2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
### 3️⃣ Run the App
bash
Copy
Edit
python app.py
## 🎯 How It Works?
### 1️⃣ Upload an audio file (2-minute movie clip 🎬)
### 2️⃣ Transcribe it into text using AssemblyAI 📝
### 3️⃣ Convert subtitles into embeddings & store in ChromaDB 🧠
### 4️⃣ Retrieve the most relevant subtitles using Cosine Similarity 🔍
### 5️⃣ Display matching subtitle timestamps 📺

## 📁 Project Structure
php
Copy
Edit
## 📂 shazam-clone
### ┣ 📂 data              # Subtitle dataset
### ┣ 📂 models            # Trained ML models
### ┣ 📂 scripts           # NLP & processing scripts
 ### ┣ 📜 app.py            # Main application script
 ### ┣ 📜 requirements.txt  # Dependencies list
 ### ┣ 📜 README.md         # Project documentation
## 🚀 Future Improvements
### ✨ Multi-Language Support (Hindi, Spanish, etc.)
### ✨ Improved Audio Noise Filtering
### ✨ Faster Real-Time Processing

## 📢 Contributions
Feel free to fork the project and submit a pull request! 🤝

## ⭐ Like This Project?
Give it a ⭐ on GitHub & share your feedback! 🚀🔥
