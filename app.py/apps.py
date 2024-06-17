
from dotenv import load_dotenv
load_dotenv() ##load all the environment variables


import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## Configure Genai Key

#genai.configure(api_key=os.getenv("AIzaSyDqZlqSQKvWmfUgFjBDD4k1cyCjxgRiu0I"))
genai.configure(api_key='AIzaSyDqZlqSQKvWmfUgFjBDD4k1cyCjxgRiu0I')

#function to load google gemini model and provide sql query as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql1,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql1)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows
## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]


## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The REsponse is")
    for row in response:
        print(row)
        st.header(row)