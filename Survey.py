# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 12:39:43 2023

@author: Siddhesh
"""

import streamlit as st
import sqlite3
import pandas as pd
import pandas as pd

# read data from the csv file 'Aus_postcodes_cleaned.csv'
df_postcodes = pd.read_csv('Aus_postcodes_cleaned.csv')

# Define the style class
class style():
      
    h1color = 'darkblue'
    h2color = 'Black'
    h3color = 'Black'
    h4color = 'grey'
    btextcolor = 'Black'
    
    h1size = 20
    h2size = 20
    h3size= 16 
    h4size = 12 
    btextsize = 16

# Define custom CSS styles for the container
container_styles = """
<style>
    .custom-container {
        background-color: #f0f0f0; /* Grey background color */
        padding: 20px; /* Adjust padding as needed */
        border-radius: 10px; /* Add rounded corners */
    }
</style>
"""

def AllInputsFilled(survey_inputs):
    """
    Check if all the inputs are filled
    """
    for i in survey_inputs:
        if i == '':
            return False
    return True



# Create or connect to the SQLite database
database_name = 'survey_responses_06OCT2023.db'
conn = sqlite3.connect(database_name)
c = conn.cursor()

# Create a table to store survey responses if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS survey_responses (
        response_id INTEGER PRIMARY KEY AUTOINCREMENT,
        q1 TEXT,
        q2 TEXT,
        q2_1 TEXT,
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
        q15 TEXT,
        q16 TEXT
          
    )
''')
conn.commit()



#====================================================================
# HEADER PAGE CONTENT
#====================================================================
col1, colmid, col2 = st.columns([1,5, 1])
with col1:
    # Define the URL you want to link to
    link_url = "https://www.prefabaus.org.au/"
    st.image('PrefabAUS_logo.png', use_column_width=True)
    
with col2:
    st.image('Unimelb_logo.png', use_column_width=True)

# Streamlit app title
st.title("Australian Prefabrication Supply Chain Survey")
st.write('')
st.write('')
st.write('')
st.write('')


Q = 'PrefabAUS and the University of Melbourne are collaborating on a comprehensive survey aimed at gaining valuable insights into the prefabricated construction supply chain within Australia. \
This research initiative seeks to better understand the dynamics, challenges, and opportunities that shape the prefabrication sector.\
By participating in this survey, you are contributing to a collective effort to enhance the efficiency, sustainability, \
and innovation within the construction industry. '
fstring1 = '<p style = "color:' + str(style.h4color) + '; font-size: ' + str(16) + 'px;text-align:left;" > <b>' + str(Q) + '</b> </p>'
st.markdown(fstring1, unsafe_allow_html=True)

Q = 'Your firsthand knowledge and experiences as a supply chain partner are crucial in helping us identify best practices, \
areas for improvement, and future trends in prefabricated construction. Your input will not only aid in strengthening the industrys\
capabilities but also inform policy decisions and educational initiatives. We value your expertise and invite you to share your perspectives and recommendations. \
Together, we can shape a more resilient, efficient, and sustainable future for construction in Australia.Thank you for your participation in this important survey, which will undoubtedly play a pivotal \
role in advancing the prefabrication sector in our country.'
fstring1 = '<p style = "color:' + str(style.h4color) + '; font-size: ' + str(16) + 'px;text-align:left;" > <b>' + str(Q) + '</b> </p>'
st.markdown(fstring1, unsafe_allow_html=True)

#====================================================================
# END OF HEADER PAGE CONTENT
#====================================================================

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

c1 = 1
c2 = 2

col1, col2 = st.columns([c1,c2])
with col1:
    # Question string
    st.write('')
    Q = 'What is your Business Name?'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
with col2:
    q1 = st.text_input('',key='q1')
st.write('')


col1, col2 = st.columns([c1,c2])
with col1:
    st.write('')
    Q = 'In which year did the company start its operations?'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
with col2:
    q2 = st.text_input("", key= 'q2')
st.write('')


col1, col2 = st.columns([c1,c2])
with col1:
    st.write('')
    Q = 'Please enter your postcode'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
    st.markdown('<p style = "color:' + str(style.h3color) + '; font-size: ' + str(13) + 'px;" >'  + '(for approximate mapping purposes only)'+  '</p>',unsafe_allow_html=True)
with col2:
    q2_1 = st.text_input("", key= 'q2_1')

    if q2_1 == '':
        q2_1 = 3000
    else:
        if q2_1.isnumeric() == True:
            # check if input q2_1 is in the 'postcode' column
            if int(q2_1) in df_postcodes['postcode'].values:
                q2_1 = int(q2_1)
            else:
                st.error('Please enter a valid postcode')
                q2_1 = 3000
        else:
            st.error('Please enter a valid postcode')
            q2_1 = 3000

# read data from the csv file 'Aus_postcodes_cleaned.csv'
df_postcodes = pd.read_csv('Aus_postcodes_cleaned.csv')  
# collect lat and long for the entered postcode
if q2_1 == '':
    lat = -37.814
    long = 144.96332
else:
    lat = df_postcodes[df_postcodes['postcode'] == int(q2_1)]['lat'].values[0]
    long = df_postcodes[df_postcodes['postcode'] == int(q2_1)]['long'].values[0]
# display the map in the sidebar
st.sidebar.map(pd.DataFrame({'lat':[lat], 'lon':[long]}))

st.write('')



col1, col2 = st.columns([c1,c2])
with col1:
    st.write('')
    Q = 'What best descibes your business from the options below?'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
with col2:
    q3 = st.selectbox('', ("Processesed material producer/supplier", 'Wholesale distributor','Volumetric modular building/units/pods manufacturer', 'Panelised unit manufacturer', 'frame fabricator', 'warehouse and logistics facilitator', 'builder/construction company', 'design studio', 'engineering services'))
st.write('')


col1, col2 = st.columns([c1,c2])
with col1:
    st.write('')
    Q = 'What level of customer value chain do you operate at?'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
with col2:
    q4 = st.selectbox(" ",('Engineer to order', 'make to order', 'assemble to order', 'make to stock'))
st.write('')



col1, col2 = st.columns([c1,c2])
with col1:
    st.write('')
    Q = 'What proportion of your business is in Prefab?'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
with col2:
    q5 = st.select_slider(" ", ('Less than 10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%'))

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


col1, col2 = st.columns([c1,c2])
with col1:
    st.write('')
    Q = 'What is your approx annual revenue'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
with col2:
    q6 = st.select_slider(" ", ('Less than $1M', '$1M-$5M', '$5M-$10M', '$10M-$20M', '$20M-$50M', '$50M-$100M', '$100M-$200M', '$200M-$500M', '$500M-$1B', 'More than $1B'))
st.write('')



col1, col2 = st.columns([c1,c2])
with col1:
    st.write('')
    Q = 'What industry segment do you serve?'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
with col2:
    q7 = st.multiselect('', ('Residential', 'Commercial/retail', 'Industrial/warehouse/heavy', 'Institutional (Schools, hospitals)', 'Public infrastructure', 'Building services/speciality trades (electrical MEP, HVAC, carpentry, masonry, roofing'))
st.write('');st.write('');st.write('');st.write('')
q7 = ', '.join(q7)


Q = 'What type of prefab products do you manufacture/supply?'
fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
st.markdown(fstring1, unsafe_allow_html=True)

st.image('product_category.png', use_column_width=True)

q8 = st.multiselect('', ('Cat-1: Volumetric modules with internal fitouts', 'Cat-2: 3D Volumetric module skeletons', 'Cat-3: 2D panelised systems with multiplie subsystems',
                                                                                   'Cat-4: 2D panels without sub-systems', 'Cat-5: Linear elements precut to sizes', 'Cat-6: Processed building materials and equipment'))
q8 = ', '.join(q8)
st.write('');st.write('');st.write('');st.write('')



col1, col2 = st.columns([c1,c2])
with col1:
    st.write('')
    Q = 'What compliances and certifications have you obtained for your products?'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
with col2:
    q9 = st.multiselect("9.  (Ex., CodeMark, WaterMark, ISO, etc.)", ('CodeMark', 'WaterMark', 'Australian Made Certification','GECA (Good Environmental Choice Australia)', 
                                                                                                                                'ISO 9001:2015 (Quality Management Systems)', 'ISO 14001:2015 (Environmental Management Systems)', 'ISO 45001:2018 (Occupational Health and Safety Management Systems)', 'Other'))
# if other is chosen as one of the options in q9, then offer a text field to insert the other certification
if 'Other' in q9:
    q9_other = st.text_input('Enter the other certifications (comma (,) separated)', key='q9_other')
    q9.append(q9_other)
q9 = ', '.join(q9)
st.write('');st.write('');st.write('');st.write('')



col1, col2 = st.columns([c1,c2])
with col1:
    st.write('')
    Q = 'What type of materials do you use in your modular builds?'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
with col2:
    q10 = st.multiselect("10.  (if applicable)", ('Resilient floor coverings', 'Waterproofing membranes', 'Sanitaryware tiles', 'Epoxies','Levelling compounds','Timber','Light gauge steel',
                                                                                                       'Structural steel','XPS board','Concrete', 'FRP/GFRP composites', 'Other'))
if 'Other' in q10:
    q10_other = st.text_input('Enter the other materials (comma (,) separated', key='q10_other')
    q10.append(q10_other)
q10 = ', '.join(q10)
st.write('');st.write('');st.write('');st.write('')


col1, col2 = st.columns([c1,c2])
with col1:
    st.write('')
    Q = 'What is the average lead time for a typical order?'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
with col2:
    q11 = st.select_slider('', ('Instant','<15 days','< 1 month','<2 months','<3 months','<8 months','<1 year'))

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

Q = 'Enter your typical throughput capacity in the units of your choice'
fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
st.markdown(fstring1, unsafe_allow_html=True)

Ex = 'Example: 1000 m3 per day, 1000 kgs per week, 1000 m2 per month, 1000 units per year'
fstring1 = '<p style = "color:' + str(style.h4color) + '; font-size: ' + str(style.h4size) + 'px;" > <b>' + str(Ex) + '</b> </p>'
st.markdown(fstring1, unsafe_allow_html=True)

Ex = 'Enter combined capacity of all your facilities and SKUs. If SKUs are of different nature, choose your main SKU.'
fstring2 = '<p style = "color:' + str(style.h4color) + '; font-size: ' + str(style.h4size) + 'px;" > <b>' + str(Ex) + '</b> </p>'
st.markdown(fstring2, unsafe_allow_html=True)



st.write('')

col1, col2 = st.columns([c1,c2])
with col1:
    st.write('Enter quantity')
with col2:
    q12_1 = st.number_input('',key='q12-qty')

col1, col2 = st.columns([c1,c2])
with col1:
    st.write('Enter units')
with col2:
    q12_2 = st.text_input('',key='q12-unt')

col1, col2 = st.columns([c1,c2])
with col1:
    st.write('Enter period')
with col2:
    q12_3 = st.text_input('',key='q12-time')

q12 = str(q12_1) + ' ' + str(q12_2) + ' per ' + str(q12_3)
st.write('you have entered:',q12)
st.write(''); st.write(''); st.write(''); st.write('')




col1, col2 = st.columns([c1,c2])
with col1:
    st.write('')
    Q = 'What product warranties and support do you provide?'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
with col2:
    q13 = st.multiselect('', ('Statutary warranty','Manufacturer warranty','Design life warranty','Implied warranties (Ex. Australian Consumer Law)','Product specific warranties','Other'))
if 'Other' in q13:
    q13_other = st.text_input('Enter the other types of warranties', key='q13_other')
    q13.append(q13_other)
q13 = ', '.join(q13)
st.write(''); st.write(''); st.write(''); st.write('')



col1, col2 = st.columns([c1,c2])
with col1:
    st.write('')
    Q = 'What are your key value offerings as a business?'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
with col2:
    q14 = st.multiselect('', ('Reduced environmental impact','Locally sourced materials','Compliance with sustainable and ecofriendly practices','Gender inclusive workforce','Higher robotic automation','Other'))
if 'Other' in q14:
    q14_other = st.text_input('Enter the other value offerings', key='q14_other')
    q14.append(q14_other)
q14 = ', '.join(q14)
st.write(''); st.write(''); st.write(''); st.write('')





Q = 'What are the top challenges in your prefab business that PrefabAUS can advocate for on your behalf?'
fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(style.h3size) + 'px;" > <b>' + str(Q) + '</b> </p>'
st.markdown(fstring1, unsafe_allow_html=True)
q15 = st.text_area('')
st.write(''); st.write(''); st.write(''); st.write('')


col1, col2 = st.columns([1,10])
with col2:
    Q = 'Indicate if you would like to be a part of PrefabAUS industry partner ecosystem and Supply Chain Directory. By checking this box, you \
    indicate your interest in being contacted by PrefabAUS to discuss your business and its capabilities in more detail. You will also be \
        invited to join the PrefabAUS Supply Chain Directory, which will be launched in 2024. The directory will be a searchable database of \
            Australian prefabrication supply chain partners, which will be made available to PrefabAUS members and the broader construction industry. \
                The directory will be a valuable resource for connecting with other supply chain partners and identifying new business opportunities. \
                    Please note that the directory will only be available to PrefabAUS members and will not be made publically available.'
    fstring1 = '<p style = "color:' + str(style.h3color) + '; font-size: ' + str(14) + 'px;" > ' + str(Q) + ' </p>'
    st.markdown(fstring1, unsafe_allow_html=True)
with col1:
    q16 = st.checkbox('')

st.write(''); st.write(''); st.write(''); st.write('')
st.write(''); st.write(''); st.write(''); st.write('')
st.write(''); st.write(''); st.write(''); st.write('')


# Collate all inputs in a list
survey_inputs = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q12, q13, q14, q15, q16]



col1, colm, col2 = st.columns([1,3,1])
with col1:
    # on clicking Display inputs button, display the dataframe
    if st.button("Display inputs"):
        st.write(survey_inputs)



with colm:
    # Submit response button
    if st.button("Submit Response", type = 'primary', use_container_width=True):
        # Insert the response into the database
        if AllInputsFilled(survey_inputs):
            query = ''' INSERT INTO  survey_responses (q1, q2, q2_1, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            c.execute(query, (q1, q2, q2_1, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16))
            conn.commit()
            st.success("Response submitted successfully. Thank you!")
        else:
            st.error("Oh! You might have missed answering some questions. Please fill in missing details before submitting.")

# Close the database connection
conn.close()

# Fetch number of responses in the database received so far
conn = sqlite3.connect(database_name)
c = conn.cursor()
c.execute("SELECT COUNT(*) FROM survey_responses")
num_responses = c.fetchone()[0]
conn.close()

st.sidebar.subheader("Previous Survey Responses")
st.sidebar.header(num_responses)



#====================================================================
# Footer PAGE CONTENT
#====================================================================
st.write('');st.write('');st.write('');st.write('');st.write('');st.write('');st.write('');st.write('')
st.write('');st.write('');st.write('');st.write('');st.write('');st.write('');st.write('');st.write('')
st.write('');st.write('');st.write('');st.write('');st.write('');st.write('');st.write('');st.write('')
Q = '2023 Australian prefabrication supply chain survey By PrefabAUS and the University of Melbourne'


# Apply custom CSS styles
st.markdown(container_styles, unsafe_allow_html=True)

# Create a container-like effect with grey background
st.markdown('<div class="custom-container"> ' + Q + '</div>', unsafe_allow_html=True)

col1, colmid, col2 = st.columns([1,5, 1])
with col1:
    # Define the URL you want to link to
    link_url = "https://www.prefabaus.org.au/"
    st.image('PrefabAUS_logo.png', use_column_width=True)
    
with col2:
    st.image('Unimelb_logo.png', use_column_width=True)
