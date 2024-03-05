import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="THIS IS MY STREAMLIT APPPPPP!",
    page_icon="👋"
)

st.write("HELLOOOOOOOOOOOOOOOOOOOOOOOOOO")
st.markdown("This is _italics_ and this is **bold**")
st.title("This is my first title")
st.header("This is a header :)")

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
st.dataframe(df)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)