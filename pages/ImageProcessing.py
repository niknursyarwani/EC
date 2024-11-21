import cv2
print(cv2.__version__)

import streamlit as st
import cv2
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas

# Sidebar controls
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")
)
realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Function to create a drawable canvas
def create_canvas_draw_instance(background_image, key):
    try:
        bg_img = Image.open(background_image)
    except FileNotFoundError:
        st.error(f"Background image {background_image} not found.")
        return None
    
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        background_image=bg_img,
        update_streamlit=realtime_update,
        drawing_mode=drawing_mode,
        width=275,
        height=184,
        key=key,
    )
    return canvas_result

# Main application
def main():
    canvas_r = create_canvas_draw_instance("bg_image_r.png", key="red")

    if canvas_r and st.button("Save Image"):
        if canvas_r.image_data is not None:
            # Save the drawn canvas image
            cv2.imwrite("test_image.png", cv2.cvtColor(canvas_r.image_data, cv2.COLOR_RGBA2BGR))
            st.success("Image saved successfully!")
        else:
            st.error("No drawing data to save.")

if __name__ == "__main__":
    main()
