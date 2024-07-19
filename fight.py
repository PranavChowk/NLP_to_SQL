from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
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
    The SQL database has the name profile and has the following columns - NAME, WON, LOST, DRAW, KO_RATE, STANCE, AGE, COUNTRY\n\nFor example,\nExample 1 - How many entries of fighters are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM profile  ;
    \nExample 2 - Tell me all the fighters who have a 100% KO_RATE?, 
    the SQL command will be something like this SELECT * FROM profile 
    where KO_RATE = '100%'; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App

st.set_page_config(page_title="Boxing Encyclopedia")
st.header("The Boxers")

question=st.text_input("Input: ",key="input")

submit=st.button("Search")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"fighter.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
