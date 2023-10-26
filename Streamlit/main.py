import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time


st.title("St study lab")
st.write("I am going to make some thing very interesting today.")

st.write("Progress...")

bar = st.progress(0)
with st.empty():
    for i in range(100):
        st.write(i + 1, "%")
        time.sleep(0.1)
        bar.progress(i + 1)


st.sidebar.write("Wights Bar")
if st.sidebar.checkbox("Show the image"):
    img = Image.open("Piofiore no Banshou.jpg")
    st.image(img, caption="Ryouhei", use_column_width=True)

option = st.sidebar.selectbox("SELECT", ["sun", "light"])
st.write(option, "was selected.")

text = st.sidebar.text_area("Please input your state: ")
st.write("YOUR STATE IS ", text)

state_num = st.sidebar.slider("HOW DO U FEEL?", 0, 100, 50)
if state_num < 50:
    state = "not happy."
elif state_num == 50:
    state = "not bad."
else:
    state = "happy."
st.write("YOU FEEL ", state)

expander = st.expander("Where are you now?")
expander.write("I am in lanzhou.")

df_family = pd.DataFrame({
    "who": ["dad", "mom", "bro", "me"],
    "animal": ["rabbit", "rabbit", "tiger", "snake"],
    "state": ["warm", "happy", "full", "study"],
    "location": ["xining", "zhengzhou", "zhengzhou", "tokyo"],
    "heart_location": ["home", "home", "home", "home"],
})
st.write(df_family)
# st.dataframe(df.style.highlight_max(axis=0))  # width=200, height=200
# st.table(df_family)

"""
## Great Day
### Today I am going to meet my famliy.So exciting.
```python
import today as a good day.
```
"""
# df_location = pd.DataFrame(
#     np.random.rand(100, 2) + [100, 100],
#     columns=["lat", "lon"],
# )
# st.map(df_location)


df_data = pd.DataFrame(
    np.random.rand(20, 3),
    columns=["a", "b", "c"],
)
st.write(df_data)
st.line_chart(df_data)
st.bar_chart(df_data)
st.area_chart(df_data)
