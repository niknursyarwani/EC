import streamlit as st
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Title
st.title("Fourier Transform in Image Processing")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load image using OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    # Display the original image
    st.subheader("Original Image")
    st.image(img, caption="Uploaded Image", use_column_width=True, channels="GRAY")

    # Compute Fourier Transform
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))

    # Create subplots for visualization
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Show original image
    ax[0].imshow(img, cmap="gray")
    ax[0].set_title("Original Image")
    ax[0].axis("off")

    # Show Fourier Transform
    ax[1].imshow(magnitude_spectrum, cmap="gray")
    ax[1].set_title("Magnitude Spectrum (Frequency Domain)")
    ax[1].axis("off")

    # Render the plots
    st.pyplot(fig)

    # Allow user to select inverse transform
    if st.checkbox("Show Inverse Fourier Transform"):
        # Compute Inverse Fourier Transform
        f_ishift = np.fft.ifftshift(fshift)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)

        # Display the reconstructed image
        st.subheader("Reconstructed Image (Inverse Transform)")
        st.image(img_back, caption="Reconstructed Image", use_column_width=True, channels="GRAY")
