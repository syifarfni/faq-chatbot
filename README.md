# 🎓 FAQ Chatbot Mahasiswa

Chatbot FAQ sederhana berbasis Large Language Model (LLM) yang dibuat menggunakan **Qwen 2.5-0.5B-Instruct** dan **Sentence Transformers**. Chatbot ini dirancang untuk menjawab pertanyaan mahasiswa berdasarkan konteks yang tersedia pada file FAQ.

## 🚀 Fitur

- Menjawab pertanyaan berdasarkan FAQ yang tersedia.
- Menggunakan Semantic Search dengan Sentence Transformers.
- Menggunakan Qwen untuk menghasilkan jawaban yang lebih natural.
- Menolak pertanyaan yang tidak sesuai dengan konteks FAQ.
- Berjalan melalui antarmuka CLI (Command Line Interface).

## 🛠️ Teknologi

- Python
- Google Colab
- Hugging Face Transformers
- Qwen 2.5-0.5B-Instruct
- Sentence Transformers
- Scikit-Learn
- NumPy

## 📂 Struktur Proyek

```text
.
├── faq.txt
├── FAQ_Chatbot.ipynb
└── README.md
```

## ⚙️ Cara Kerja

1. FAQ dibaca dari file `faq.txt`.
2. Pertanyaan FAQ diubah menjadi embedding menggunakan Sentence Transformers.
3. Pertanyaan pengguna juga diubah menjadi embedding.
4. Cosine Similarity digunakan untuk mencari FAQ yang paling relevan.
5. Jika similarity berada di bawah threshold, chatbot menolak pertanyaan.
6. Jika similarity memenuhi threshold, jawaban FAQ digunakan sebagai konteks untuk Qwen.
7. Qwen menghasilkan jawaban yang lebih natural dan mudah dipahami.

## 📦 Instalasi

Install library yang diperlukan:

```bash
pip install transformers accelerate sentence-transformers scikit-learn numpy torch
```

## ▶️ Menjalankan Program

Buka notebook di Google Colab dan jalankan seluruh cell secara berurutan.

Pastikan file `faq.txt` tersedia dan path telah disesuaikan.

## 💬 Contoh Penggunaan

### Pertanyaan yang tersedia dalam FAQ

```text
User: bagaimana cara meningkatkan nilai akademik?

Chatbot: Rajin mengikuti kuliah, mengerjakan tugas tepat waktu, dan rutin belajar merupakan langkah yang efektif.
```

### Pertanyaan di luar FAQ

```text
User: bagaimana cara memasak nasi goreng?

Chatbot: Maaf, saya tidak dapat membantu dengan pertanyaan itu.
```

## 🧠 Model yang Digunakan

### Qwen 2.5-0.5B-Instruct

Digunakan sebagai Large Language Model (LLM) untuk mengubah jawaban FAQ menjadi respons yang lebih natural.

### Sentence Transformers

Model:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

Digunakan untuk melakukan semantic similarity search pada FAQ.

## 📌 Catatan

Proyek ini dibuat sebagai bagian dari Challenge AI Engineer Intern DOT Indonesia.
