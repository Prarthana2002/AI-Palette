import streamlit as st
from PIL import Image
import requests
import time
from io import BytesIO

# Hugging Face API endpoint and API key
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
API_KEY = "Hugging_face_api"

def generate_image(prompt, retries=3, delay=5):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "inputs": prompt,
        "num_inference_steps": 50,
        "guidance_scale": 7.5
    }

    for attempt in range(retries):
        try:
            response = requests.post(API_URL, json=data, headers=headers, timeout=60)
            response.raise_for_status()
            return Image.open(BytesIO(response.content))
        except requests.exceptions.HTTPError as e:
            if response.status_code == 503 and attempt < retries - 1:
                st.write(f"Service unavailable. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                st.error(f"Error: {e}")
                return None

# Streamlit Interface
st.title("DreamCanvas: AI Art Generator")

# Pre-load styles and characters
styles = ["Realistic", "Comic", "Anime", "Watercolor", "Pixel Art"]
characters = ["Superhero", "Villain", "Cartoon", "Fantasy Creature", "Animal"]

# Dropdown for style and character selection
selected_style = st.selectbox("Choose Art Style:", styles)
selected_character = st.selectbox("Choose Character Type:", characters)

# Aspect ratio and background options
aspect_ratios = ["1:1 (Square)", "16:9 (Wide)", "4:3 (Standard)", "9:16 (Portrait)"]
selected_aspect_ratio = st.selectbox("Choose Aspect Ratio:", aspect_ratios)
background_options = ["Plain", "Landscape", "Cityscape", "Abstract"]
selected_background = st.selectbox("Choose Background Style:", background_options)

# Text input for custom prompt
prompt = st.text_input("Enter your custom image prompt (optional):")

# Button to generate the image
if st.button("Generate"):
    if selected_style and selected_character and selected_aspect_ratio:
        st.write("Generating image...")

        # Combine prompt with style, character, aspect ratio, and background
        full_prompt = f"A {selected_character} in {selected_style} style with a {selected_background} background, aspect ratio {selected_aspect_ratio}. {prompt}"
        image = generate_image(full_prompt)

        if image:
            st.image(image, caption='Generated Image', use_column_width=True)

            # Create a download button for the generated image
            img_byte_arr = BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()

            st.download_button(
                label="Download Image",
                data=img_byte_arr,
                file_name="generated_image.png",
                mime="image/png"
            )
