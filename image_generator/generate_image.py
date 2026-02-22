from PIL import Image, ImageDraw, ImageFont
import json
import os


TEMPLATE_PATH = "templates/news_template.png"
OUTPUT_DIR = "data/generated_images"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_image(text, index):

    img = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 48)

    draw.multiline_text(
        (100, 400),
        text,
        fill="white",
        font=font,
        align="center"
    )

    output_path = f"{OUTPUT_DIR}/news_{index}.png"
    img.save(output_path)

    print("✅ Image Created:", output_path)


def generate_images():

    with open("data/summarized_news.json", "r", encoding="utf-8") as f:
        news = json.load(f)

    for i, item in enumerate(news):
        create_image(item["summary"], i)


if __name__ == "__main__":
    generate_images()