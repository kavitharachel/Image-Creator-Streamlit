# app.py
import os
from io import BytesIO

import streamlit as st
from PIL import Image
from huggingface_hub import InferenceClient

APP_TITLE = "Text → Image (Streamlit + Hugging Face Inference)"
DEFAULT_MODEL = "stabilityai/stable-diffusion-xl-base-1.0"

def get_hf_token() -> str | None:
    # Prefer Streamlit secrets, fallback to env var
    token = None
    try:
        token = st.secrets.get("HF_TOKEN", None)  # type: ignore[attr-defined]
    except Exception:
        token = None
    if not token:
        token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
    return token

@st.cache_resource(show_spinner=False)
def get_client(model_name: str) -> InferenceClient:
    token = get_hf_token()
    if not token:
        raise RuntimeError(
            "Missing Hugging Face token. Set HF_TOKEN in Streamlit secrets "
            "or HUGGINGFACEHUB_API_TOKEN as an environment variable."
        )
    return InferenceClient(model=model_name, token=token)

def main():
    st.set_page_config(page_title=APP_TITLE, page_icon="🎨", layout="wide")
    st.title(APP_TITLE)
    st.caption("Fast, simple demo. Uses Hugging Face Inference API under the hood.")

    # Sidebar controls
    with st.sidebar:
        st.header("⚙️ Settings")
        model_name = st.selectbox(
            "Model",
            [
                "stabilityai/stable-diffusion-xl-base-1.0",
                "stabilityai/stable-diffusion-2-1",
                "runwayml/stable-diffusion-v1-5",
            ],
            index=0,
            help="Pick a text-to-image model available on the Hugging Face Inference API."
        )
        steps = st.slider("Steps", min_value=4, max_value=50, value=30, help="Number of denoising steps.")
        guidance = st.slider("Guidance scale", min_value=1.0, max_value=15.0, value=7.5, step=0.1,
                             help="How strongly the image should follow the prompt.")
        size = st.selectbox("Resolution", ["512x512", "768x768", "1024x1024"], index=0)
        width, height = map(int, size.split("x"))
        n_images = st.slider("Images to generate", 1, 4, 1)

        st.markdown("---")
        st.subheader("🔐 Secrets")
        st.write("This app requires a Hugging Face API token:")
        st.code("HF_TOKEN = 'hf_xxx...'", language="toml")
        st.caption("On Streamlit Cloud: **App → Settings → Secrets**. Locally: set env var HUGGINGFACEHUB_API_TOKEN or create .streamlit/secrets.toml.")

    # Prompt UI
    prompt = st.text_area("Prompt", placeholder="A watercolor cat astronaut walking on the moon, stars in the background",
                          height=100)
    negative = st.text_input("Negative prompt (optional)", placeholder="low quality, blurry, distorted")

    gen = st.button("🎨 Generate", type="primary", use_container_width=True, disabled=not prompt)

    if gen:
        try:
            client = get_client(model_name)
        except Exception as e:
            st.error(str(e))
            st.stop()

        cols = st.columns(n_images)
        for i in range(n_images):
            with st.spinner(f"Generating image {i+1}/{n_images}…"):
                try:
                    img = client.text_to_image(
                        prompt=prompt,
                        negative_prompt=negative or None,
                        height=height,
                        width=width,
                        num_inference_steps=steps,
                        guidance_scale=guidance,
                    )
                except Exception as e:
                    st.error(f"Generation error: {e}")
                    st.stop()

            buf = BytesIO()
            img.save(buf, format="PNG")
            cols[i].image(img, caption=f"{width}×{height}", use_column_width=True)
            cols[i].download_button(
                "⬇️ Download PNG",
                data=buf.getvalue(),
                file_name="text2image.png",
                mime="image/png",
                use_container_width=True,
            )

    with st.expander("ℹ️ Tips"):
        st.markdown(
            "- Add style cues: *photo, studio lighting, watercolor, Pixar style, isometric, 8k, bokeh, cinematic*.\n"
            "- Use **negative prompts** to avoid artifacts: *blurry, deformed, extra fingers, watermark*.\n"
            "- If you hit rate limits, lower resolution or steps, or try later."
        )

if __name__ == '__main__':
    main()
