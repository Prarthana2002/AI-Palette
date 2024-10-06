# AI-Palette

AI Art Generator
It's is a web-based AI-powered tool that allows users to generate custom images based on their preferences for art style, character, background, and more. This app uses a pre-trained model from Hugging Face to generate stunning images from text prompts.

Features
Select from a variety of art styles (e.g., Realistic, Anime, Watercolor).
Choose a character type (e.g., Superhero, Villain, Cartoon).
Customize the background and aspect ratio of the image.
Provide a custom text prompt for unique results.
Download the generated image directly in PNG format.
Requirements
To run DreamCanvas locally, you'll need the following installed:

Python 3.7 or higher
Required Python libraries listed below.
Libraries Used:
streamlit: For building the web interface.
Pillow: For handling image manipulation and display.
requests: For API calls to Hugging Face.

Usage
Select Art Style: Choose from different art styles like Realistic, Anime, Comic, etc.
Choose Character Type: Select a character type such as Superhero, Villain, or Animal.
Customize Background and Aspect Ratio: Tailor your image’s background and aspect ratio to your preference.
Enter Prompt: Optionally, provide a custom text prompt to guide the AI in generating the image.
Generate Image: Click on the "Generate" button to create your unique artwork.
Download: After previewing the image, download it as a PNG file.
Example
After selecting the style, character, aspect ratio, and background, you’ll see your generated image displayed on the screen. You can download the image by clicking the "Download Image" button.

API Information
This app uses the Hugging Face API for the image generation model. You will need to provide a valid API key for the app to work. The API key is embedded in the code for easy access, but you can replace it with your own.
