from numpy import place
import streamlit as st
import pandas as pd

st.write('# Thank you ✌️')
st.write('## For participation in the seremonial activity of me becoming a data-app developer.')

st.write("Don't believe me? Then why does my app have all this data (which is really dataframes 🤯)")

st.write('This is just a regular dataframe that I created in python.')
df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
st.write(df)
st.write('Cool, huh?')
st.button(label='Umm...yes?', on_click=lambda: st.balloons())

st.write('## But wait, there\'s more...')
st.write('What if I told you that I can render any csv available on the internet, through a dataframe?')
st.write("""Well, check this out;

The code that I write is simply

```python
st.write(pd.read_csv(<your_url>))
```""")
st.write('The code that I write is simply')

fetch_url = st.text_input(
    'Url to CSV', placeholder='https://some-url.com/sample.csv', key='fetch_url', value='https://people.sc.fsu.edu/~jburkardt/data/csv/snakes_count_1000.csv')
st.warning('It\'s prefilled with some _really_ cool data!')


if st.session_state.get('fetch_url'):
    st.write(pd.read_csv(st.session_state.get('fetch_url')))
