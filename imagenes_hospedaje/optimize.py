import os
from PIL import Image

def optimize_images(directory):
    count = 0
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(directory, filename)
            try:
                img = Image.open(filepath)
                # Convert to RGB to avoid issues with alpha channels when saving
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                    
                target_filename = os.path.splitext(filename)[0] + '.webp'
                target_filepath = os.path.join(directory, target_filename)
                
                # Check if it already exists to avoid redundant work
                if not os.path.exists(target_filepath):
                    img.save(target_filepath, 'webp', optimize=True, quality=80)
                    print(f"Optimized: {filename} -> {target_filename}")
                    count += 1
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    print(f"Total {count} images optimized to WebP.")

if __name__ == "__main__":
    optimize_images(".")
