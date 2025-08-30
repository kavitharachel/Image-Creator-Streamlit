# Text → Image (Local) — Streamlit + Diffusers (No external APIs)

This app runs *entirely locally* using your CPU/GPU. It **does not** call Hugging Face Inference API or any other hosted service.
You must provide a **local Stable Diffusion model** directory in Diffusers format.

---

## 🚀 Quickstart

1) **Clone** and enter the folder:
```bash
git clone https://github.com/your-username/text2img-streamlit-local.git
cd text2img-streamlit-local
```

2) (Optional) **Create a virtual env** and install dependencies:
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3) **Provide a local model** (Diffusers format):
- Put it anywhere on your disk (e.g., `models/sd-local`), and set that path in the app sidebar.
- The app is configured with `local_files_only=True` and will not download anything.

> Tip: If you have a `.safetensors` file, convert it to Diffusers format using the official script from the Diffusers repo, then point the app to that folder.

4) **Run the app:**
```bash
streamlit run app.py
```

5) **Use the app:**
- Enter a prompt
- Choose resolution, steps, guidance, and batch size
- Click **Generate** → Download PNG

---

## ⚡ Performance
- **GPU recommended**. Works with NVIDIA CUDA or Apple Silicon (MPS). CPU will be slow.
- Use **512×512** and fewer steps for faster results.

## 📁 Structure
```
text2img-streamlit-local/
├─ app.py
├─ requirements.txt
├─ README.md
└─ models/              # (empty placeholder — drop your local Diffusers model here if you like)
```

## 🔒 Privacy
Everything stays on your machine. No prompts or images leave your device.

## 🛡️ Safety
Safety checker is disabled by default to keep the demo minimal. Add one if your use case requires it.
