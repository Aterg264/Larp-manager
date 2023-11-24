import streamlit as st

def preprocess(img):
    bytes_data = np.asarray(bytearray(img.read()), dtype=np.uint8)
    img = cv2.imdecode(bytes_data, cv2.IMREAD_COLOR)
    return img

def sketch(img):
    img = preprocess(img)
    _, sketch_img = cv2.pencilSketch(
        img, sigma_s=60, sigma_r=0.07, shade_factor=0.1
    )
    return sketch_img

picture = st.camera_input("First, take a picture...")
if picture:
    st.image(sketch(picture), channels="BGR")