# Text → Image with Streamlit (Hugging Face Inference)

A minimal, production-ready Streamlit app that turns text prompts into images using the **Hugging Face Inference API** (no GPU setup required).

https://github.com/your-username/text2img-streamlit

---

## ✨ Features
- Clean Streamlit UI (prompt, negative prompt, steps, guidance, size, batch size)
- Uses `huggingface_hub.InferenceClient().text_to_image(...)`
- Works locally and on **Streamlit Community Cloud**
- Download generated images as PNG

## 🚀 Quickstart (Local)

1) **Clone** and enter the folder:
```bash
git clone https://github.com/your-username/text2img-streamlit.git
cd text2img-streamlit
```

2) **Create a virtual env** (optional but recommended) and install deps:
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3) **Set your Hugging Face token** (create one at https://huggingface.co/settings/tokens):
```bash
export HUGGINGFACEHUB_API_TOKEN=hf_xxx   # Windows (Powershell): $env:HUGGINGFACEHUB_API_TOKEN="hf_xxx"
```

Alternatively, create `.streamlit/secrets.toml` and add:
```toml
HF_TOKEN="hf_xxx"
```

4) **Run the app:**
```bash
streamlit run app.py
```

## ☁️ Deploy to Streamlit Community Cloud

1) Push this repo to GitHub:
```bash
git init
git remote add origin https://github.com/your-username/text2img-streamlit.git
git add .
git commit -m "Initial commit: Streamlit text-to-image"
git branch -M main
git push -u origin main
```

2) Go to https://share.streamlit.io/ → **New app** → pick your repo/branch.

3) In the app **Settings → Secrets**, paste:
```toml
HF_TOKEN="hf_xxx"
```

4) **Deploy**. First build may take ~1–2 minutes. If you hit rate limits, try smaller image sizes or fewer steps.

## 🔧 Configuration

- Change default model in the sidebar — options include:
  - `stabilityai/stable-diffusion-xl-base-1.0` (default)
  - `stabilityai/stable-diffusion-2-1`
  - `runwayml/stable-diffusion-v1-5`

- Tweak defaults inside `app.py` if you like (steps, guidance, etc.).

## 📁 Project Structure
```
text2img-streamlit/
├─ app.py
├─ requirements.txt
├─ README.md
└─ .streamlit/
   └─ secrets.toml  # (optional locally; NEVER commit tokens)
```

> Pro tip: Add `.streamlit/secrets.toml` to `.gitignore` so tokens never get committed.

## 🧰 Troubleshooting

- **Missing token** → Ensure `HF_TOKEN` is set in Streamlit secrets **or** `HUGGINGFACEHUB_API_TOKEN` is set as an env var.
- **Rate limited / 5xx** → Reduce image size, steps, or try again later.
- **Model not allowed** → Pick a different model that supports the Inference API.

## 🛡️ Safety & Use
Prompts and images are user‑generated. Please follow your organization’s usage policies and Hugging Face model licenses.
