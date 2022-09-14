import streamlit

streamlit.title('My parents new healthy diner')

streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗Omasaki Burger')
streamlit.text('🐔Hearty Cereal')
streamlit.text('🥑🍞Fish and Chips made from UK London original')
streamlit.text('🥑Avocado king fisher french fries')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
