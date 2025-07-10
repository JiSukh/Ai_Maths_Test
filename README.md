# AI Math Question Generator (Prototype)

This is a prototype AI-powered math question generator. It generates math questions and answers using a language model, and writes them to an `output.html` file. Very shoddy code and sometimes doesn't work. Formatting is really bad and it outputs raw HTML 😭.

---

## 🛠 Setup

### 1. Install Python dependencies

Make sure you have **Python 3.8+** installed. Then, install the required modules:

```bash
pip install -r requirements.txt
```

### 2. Login to Hugging Face CLI
This project uses models from the Hugging Face Hub. You need to authenticate your CLI to access models (especially if they are gated or private).

```bash
huggingface-cli login
```

## Once everything is set up, run the generator using 
```bash
python app.py
```

The output is a simple HTML file: output.html

Open it in your web browser to view the generated questions and answers

