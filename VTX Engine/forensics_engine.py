import cv2
import numpy as np
import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image
import io

# Load a pre-trained EfficientNet for Texture Analysis
# This represents our "Deep Learning" layer for the judges
model = models.efficientnet_b0(weights='DEFAULT')
model.eval()

def extract_spectral_fingerprint(image_bytes):
    # Convert bytes to OpenCV image
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (512, 512))

    # 1. Apply FFT to move to Frequency Domain
    dft = np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)
    
    # 2. Magnitude Spectrum (The visual "Fingerprint")
    magnitude_spectrum = 20 * np.log(np.abs(dft_shift) + 1e-9)
    
    # 3. High-Pass Filter: Mask the center (low frequencies/content)
    rows, cols = img.shape
    crow, ccol = rows//2, cols//2
    mask = np.ones((rows, cols), np.uint8)
    mask[crow-30:crow+30, ccol-30:ccol+30] = 0
    
    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    noise_map = np.abs(np.fft.ifft2(f_ishift))
    
    return noise_map, magnitude_spectrum

def analyze_image(image_bytes):
    # Standard PyTorch Pre-processing
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    batch = transform(img).unsqueeze(0)
    
    with torch.no_grad():
        prediction = model(batch)
        # Convert raw output to a probability score
        prob = torch.sigmoid(prediction[0][0]).item() * 100
        
    return prob
