import os
import subprocess
import glob

assets_dir = 'assets'
opt_dir = os.path.join(assets_dir, 'opt')
os.makedirs(opt_dir, exist_ok=True)

# Find all images
images = glob.glob(os.path.join(assets_dir, '*.jpg')) + glob.glob(os.path.join(assets_dir, '*.jpeg')) + glob.glob(os.path.join(assets_dir, '*.png'))

for img in images:
    filename = os.path.basename(img)
    opt_path = os.path.join(opt_dir, filename)
    
    # Aggressively resize to max 1200px and compress to 40% quality
    # PNGs will just be copied or resized. Since sips preserves format by default:
    cmd = ['sips', '-Z', '1000', '-s', 'formatOptions', '40', img, '--out', opt_path]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Optimized {filename}")

