# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 12:39:43 2023

@author: Siddhesh
"""

import streamlit as st
import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect('survey_responses.db')
c = conn.cursor()

# Create a table to store survey responses if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS survey_responses (
        response_id INTEGER PRIMARY KEY AUTOINCREMENT,
        q1 TEXT,
        q2 TEXT,
        q3 TEXT,
        q4 TEXT,
        q5 TEXT,
        q6 TEXT,
        q7 TEXT,
        q8 TEXT,
        q9 TEXT,
        q10 TEXT,
        q11 TEXT,
        q12 TEXT,
        q13 TEXT,
        q14 TEXT,
        q15 TEXT
          
    )
''')
conn.commit()

# Streamlit app title
st.title("Australian Prefabrication Supply Chain Survey")
st.write('')
st.write('')
st.write('')
st.write('')

st.video('https://www.youtube.com/watch?v=akKgTf3cb-4')

st.write('')
st.write('')
st.write('')
st.write('')

st.image('divider.png', use_column_width=True)
st.header('Company information')
st.write('')
st.write('')
st.write('')
st.write('')
# Survey questions and input fields
q1 = st.text_input("1. What is your Business Name")
st.write('')

q2 = st.text_input("2. What is the year in which you business started operations?")
st.write('')

q3 = st.selectbox("3. What is the type of your business closes to the description below?", ("Material processessor", "product manufacuter", 'Wholesale distributor', 'frame fabricator', 'warehouse and logistics facilitator', 'construction company', 'design company', 'engineering services'))
st.write('')

q4 = st.selectbox("4. What level of customer value chain do you operate at?",('Engineer to order', 'make to order', 'assemble to order', 'make to stock'))
st.write('')

q5 = st.select_slider("5. What proportion of your business is in Prefab?", ('Less than 10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%'))

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

st.image('divider.png', use_column_width=True)
st.header('Product information')
st.write('')
st.write('')
st.write('')
st.write('')
q6 = st.select_slider("6. What is your approx annual revenue", ('Less than $1M', '$1M-$5M', '$5M-$10M', '$10M-$20M', '$20M-$50M', '$50M-$100M', '$100M-$200M', '$200M-$500M', '$500M-$1B', 'More than $1B'))
st.write('')

q7 = st.multiselect('7. What industry segment do you serve?', ('Residential', 'Commercial/retail', 'Industrial/warehouse/heavy', 'Institutional (Schools, hospitals)', 'Public infrastructure', 'Building services/speciality trades (electrical MEP, HVAC, carpentry, masonry, roofing'))
st.write('')
q7 = ', '.join(q7)


q8 = st.multiselect('8. What type of prefab products do you manufacture/supply?', ('Cat-1: Volumetric modules with internal fitouts', 'Cat-2: 3D Volumetric module skeletons', 'Cat-3: 2D panelised systems with multiplie subsystems',
                                                                                   'Cat-4: 2D panels without sub-systems', 'Cat-5: Linear elements precut to sizes', 'Cat-6: Processed building materials and equipment'))
q8 = ', '.join(q8)
st.image('product_category.png', use_column_width=True)

st.write('')

q9 = st.text_input("9. What compliances and certifications have you obtained for your products? (Ex., CodeMark, WaterMark, ISO, etc.)")
st.write('')

q10 = st.multiselect("10. What type of materials do you use in your modular builds? (if applicable)", ('Resilient floor coverings', 'Waterproofing membranes', 'Sanitaryware tiles', 'Epoxies','Levelling compounds','Timber','Light gauge steel',
                                                                                                       'Structural steel','XPS board','Concrete', 'FRP/GFRP composites'))
q10 = ', '.join(q10)

st.write('')

q11 = st.select_slider('11. What is the average lead time for a typical order?', ('Instant','<15 days','< 1 month','<2 months','<3 months','<8 months','<1 year'))

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

st.image('divider.png', use_column_width=True)
st.header('Supply chain information')
st.write('')
st.write('')
st.write('')
st.write('')

col1, col2, col3 = st.columns([1,1,1])
with col1:
    q121 = st.number_input('What is the typical maximum through put of your company?')
with col2:
    q122 = st.text_input('Enter the units of the number')
with col3:
    q123 = st.text_input('Enter the time period of the throughput, Ex. per day, per week, per month, per year')

q12 = str(q121) + ' ' + str(q122) + ' per ' + str(q123)
st.write(q12)

st.write('')
q13 = st.text_input('What product warranties and support do you provide?')

st.write('')
q14 = st.multiselect('What are your key value offerings as a business?', ('Reduced environmental impact','Locally sourced materials','Compliance with sustainable and ecofriendly practices','Gender inclusive workforce','Higher robotic automation','Other'))
q14 = ', '.join(q14)


st.write('')
q15 = st.text_area('What are the key challenges when constructing using prefab in your business?')

# Submit response button
if st.button("Submit Response"):
    # Insert the response into the database

    c.execute('''
        INSERT INTO survey_responses (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15))
    conn.commit()
    st.success("Response submitted successfully. Thank you!")

# Close the database connection
conn.close()

# Fetch number of responses in the database received so far
conn = sqlite3.connect('survey_responses.db')
c = conn.cursor()
c.execute("SELECT COUNT(*) FROM survey_responses")
num_responses = c.fetchone()[0]
conn.close()

st.sidebar.subheader("Previous Survey Responses")
st.sidebar.header(num_responses)



