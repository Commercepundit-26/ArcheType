import os
from PIL import Image

images = [
    "assets/opt/material_cordura.jpg",
    "assets/opt/material_tegris.jpg",
    "assets/opt/material_mesh.jpg",
    "assets/opt/material_clips.jpg",
    "assets/opt/material_fasteners.jpg",
    "assets/opt/material_magnets.jpg",
    "assets/cinematic_holster.jpg"
]

for img_path in images:
    if os.path.exists(img_path):
        img = Image.open(img_path)
        
        # Target size for slider images: 800x1200
        # Wait, for cinematic_holster it's a wide hero background! We shouldn't crop cinematic_holster to 2:3!
        if "cinematic_holster" in img_path:
            # Maybe just resize it down to 1920px wide?
            w, h = img.size
            if w > 1920:
                new_h = int(1920 * h / w)
                img = img.resize((1920, new_h), Image.Resampling.LANCZOS)
                img.save(img_path, "JPEG", quality=60)
                print(f"Resized {img_path} to 1920w")
        else:
            # Crop to 800x1200 for material cards
            w, h = img.size
            target_aspect = 800 / 1200.0
            aspect = w / h
            if aspect > target_aspect:
                # Image is too wide
                new_w = int(target_aspect * h)
                offset = (w - new_w) // 2
                img = img.crop((offset, 0, offset + new_w, h))
            else:
                # Image is too tall
                new_h = int(w / target_aspect)
                offset = (h - new_h) // 2
                img = img.crop((0, offset, w, offset + new_h))
            
            img = img.resize((800, 1200), Image.Resampling.LANCZOS)
            img.save(img_path, "JPEG", quality=60)
            print(f"Cropped and resized {img_path} to 800x1200")

