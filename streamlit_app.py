import streamlit as st
import pandas as pd 

# print out  TITLE TEXT
st.title('🎈 Snow Cheetah 🎈')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


st.sidebar.header('INPUT')
# printout text
st.write('Hello world!')

url_input = st.sidebar.text_input('URL', '')

if url_input:
    st.header('OUTPUT')
    st.info(f'Test info url input is {url_input}')
    st.write('URL of your data is ', url_input)
    df =  pd.read_csv(url_input)
    #print out data frame
    st.write(df)

    # aggregate all column data
    column_label = df.columns[-1]
    # st.info(f'column_label {column_label}')
    label_list = df[column_label].unique()
    # st.info(f'Label List {label_list}')

    col1, col2 = st.columns(2)

    # print specific column data
    with col1:
        st.info(f'FILTER DATA')
        class_select = st.radio(f'Please Select Class {column_label}', label_list)
        st.write(df[df[column_label]==class_select])


    # print summary data
    with col2:
        st.info(f'SUMMARY CLASS DATA')  
        df_agg = df.groupby(column_label).mean()

        st.info(f'aggregate by "{column_label}"')

        st.write(df_agg)
        st.bar_chart(df_agg)


    #get sub sample record
    


    # if genre == 'Comedy':
    #     st.write('You selected comedy.')
    # else:
    #     st.write("You didn't select comedy.")


else:
    st.error(f' NO input 👈👈👈 COPY & PASTE URL FIRST!!!')

#df =  pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv')


