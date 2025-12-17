class Test:
    def test_example(self):
        assert True
    def test_another_example(self):
        assert 1 + 1 == 2
import streamlit as st
st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")
st.button("Click me!")
st.text_input("Enter your name:")
st.slider("Select a value:", 0, 100, 50)
st.checkbox("I agree to the terms and conditions")
st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.radio("Select one:", ["Choice A", "Choice B", "Choice C"])
st.file_uploader("Upload a file:")
st.date_input("Pick a date:")
st.color_picker("Pick a color:")
st.progress(50)
st.balloons()
st.success("This is a success message!")
st.error("This is an error message!")
st.warning("This is a warning message!")
st.info("This is an informational message.")
st.metric("Temperature", "70 °F", "+3 °F")
