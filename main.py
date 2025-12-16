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
st.dataframe({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})
st.line_chart([1, 2, 3, 4, 5])
st.bar_chart([5, 3, 6, 2, 4])
st.map({"lat": [37.76, 37.77, 37.78], "lon": [-122.4, -122.41, -122.42]})
st.sidebar.title("Sidebar")
st.sidebar.button("Sidebar Button")
st.sidebar.selectbox("Sidebar Selectbox:", ["A", "B", "C"])
st.cache
def expensive_computation(x):
    return x * x
st.write("Expensive computation result:", expensive_computation(10))
st.form("my_form")
with st.form("my_form"):
    name = st.text_input("Enter your name in the form:")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Hello, {name}!")