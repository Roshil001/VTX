import cv2
import numpy as np

def extract_spectral_fingerprint(image_bytes):
    # Load and Grayscale
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (512, 512))

    # Calculate FFT
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    
    # Magnitude Spectrum (The "Fingerprint" visualization)
    magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)
    
    # High-pass filter to isolate the 'noise'
    rows, cols = img.shape
    crow, ccol = rows//2, cols//2
    fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
    
    # Reconstruct noise map
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.abs(np.fft.ifft2(f_ishift))
    
    return img_back, magnitude_spectrum
