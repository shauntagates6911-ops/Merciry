from PIL import Image, ImageDraw, ImageFont

def create_favicon():
    # Create 64x64 image for clean scaling
    size = (64, 64)
    image = Image.new("RGBA", size, color=(30, 41, 59, 255)) # Dark slate blue background
    draw = ImageDraw.Draw(image)

    # Load default font or custom font
    try:
        font = ImageFont.truetype("arialbd.ttf", 26)
    except IOError:
        font = ImageFont.load_default()

    # Center text
    bbox = draw.textbbox((0, 0), "Mer", font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((64 - w) / 2, (64 - h) / 2 - 2), "Mer", fill=(255, 255, 255), font=font)

    # Save as ICO containing standard favicon dimensions
    image.save("favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])

create_favicon()
