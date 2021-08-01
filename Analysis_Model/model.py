import streamlit as st
import pandas as pd
import numpy as np


st.title('STREAMLIT DATA ANALYSIS ')



st.set_option('deprecation.showfileUploaderEncoding', False)

upload_file1, upload_file2 = st.beta_columns(2)
btn1, btn2 = st.beta_columns(2)
ch = ["None", "replace with Mean", "replace with Median", "replace with 0", "remove entire column",
      "remove entire row"]
uploaded_file1 = st.sidebar.file_uploader(label='', type=['csv'])
uploaded_file2 = st.sidebar.file_uploader(label=' ', type=['csv'])

if uploaded_file1 is not None:
    df1 = pd.read_csv(uploaded_file1, encoding='unicode_escape')
    upload_file1.success("Dataset 1 had been uploaded")
    col = btn1.checkbox("Descriptive statistics")
    if col:
        st.subheader("DESCRIPTIVE STATISTICS FOR DATASET 1")
        st.table(df1.describe())
    else:
        upload_file1.info("you didn't select any option")
    data_frame = df1
    miss_val = btn1.checkbox("Missing Values")
    if miss_val:
        select = st.sidebar.selectbox("Select any one for dataset 1", ch)
        if select == "replace with Mean":
            st.subheader("Metadata for dataset 1")
            mv_1 = df1.fillna(df1.mean())
            data_frame = mv_1
            st.write(mv_1)
        elif select == "replace with Median":
            st.subheader("Metadata for dataset 1")
            mv_1 = df1.fillna(df1.median())
            data_frame = mv_1
            st.write(mv_1)
        elif select == "replace with 0":
            st.subheader("Metadata for dataset 1")
            mv_1 = df1.fillna(0)
            data_frame = mv_1
            st.write(mv_1)
        elif select == "remove entire row":
            st.subheader("Metadata for dataset 1")
            mv_1 = df1.dropna()
            data_frame = mv_1
            st.write(mv_1)
        elif select == "remove entire column":
            st.subheader("Metadata for dataset 1")
            mv_1 = df1.dropna(axis=1)
            data_frame = mv_1
            st.write(mv_1)
        else:
            upload_file1.info("Please select any one")

    math_functions = btn1.checkbox("Apply math operation")
    if math_functions:
        math_function = ["None", "basic", "compare"]
        oper = st.sidebar.selectbox("select a function for dataset 1", math_function)
        if oper == "basic":
            st.subheader("basic operations for dataset 1")
            all_columns = data_frame.columns.tolist()
            col1 = st.sidebar.selectbox("choose the variable for A for dataset 1", all_columns)
            col2 = st.sidebar.selectbox('choose the variable for B for dataset 1', all_columns)
            option = ['None', 'Add', 'Sub', 'Mul', 'Div']
            arithmetic = st.sidebar.selectbox("select the arithmetic operator for dataset 1", option)

            if arithmetic == "Add":
                st.header("ADDITION")
                data_frame['ADDITION'] = data_frame[col1] + data_frame[col2]
                st.write(data_frame)


            elif arithmetic == "Sub":
                st.header("SUBTRACTION")
                data_frame['SUBTRACTION'] = data_frame[col1] - data_frame[col2]
                st.write(data_frame)

            elif arithmetic == "Mul":
                st.header("MULTIPLICATION")
                data_frame['MULTIPLICATION'] = data_frame[col1] * data_frame[col2]
                st.write(data_frame)

            elif arithmetic == "Div":
                st.header("DIVISION")
                data_frame['DIVISION'] = data_frame[col1] / data_frame[col2]
                st.write(data_frame)

        elif oper == "compare":
            st.subheader("comparison operations for dataset 1")
            all_columns = data_frame.columns.tolist()
            col3 = st.sidebar.selectbox("choose the variable for A for dataset 1", all_columns)
            col4 = st.sidebar.selectbox("choose the variable for B for dataset 1", all_columns)
            conditions = [data_frame[col3] > data_frame[col4],
                          data_frame[col3] < data_frame[col4],
                          data_frame[col3] == data_frame[col4]]

            # define choices
            choices = ['TRUE', 'FALSE', 'EQUAL']

            # create new column in DataFrame that displays results of comparisons
            data_frame['comparison'] = np.select(conditions, choices)
            data_frame['Diff'] = np.where(data_frame[col3] == data_frame[col4], 0, data_frame[col3] - data_frame[col4])
            st.write(data_frame)

if uploaded_file2 is not None:
    df2 = pd.read_csv(uploaded_file2, encoding='unicode_escape')
    upload_file2.success("Dataset 2 had been uploaded")
    col_2 = btn2.checkbox("Descriptive  statistics")
    if col_2:
        st.subheader("DESCRIPTIVE STATISTICS FOR DATASET 2")
        st.table(df2.describe())
    else:
        upload_file2.info("you didn't select any option")
    data_frame_2 = df2
    miss_val_1 = btn2.checkbox("Missing  Values")
    if miss_val_1:
        select_1 = st.sidebar.selectbox("Select any one for dataset 2", ch)
        if select_1 == "replace with Mean":
            st.subheader("Metadata for dataset 2")
            mv_2 = df2.fillna(df2.mean())
            data_frame_2 = mv_2
            st.write(mv_2)
        elif select_1 == "replace with Median":
            st.subheader("Metadata for dataset 2")
            mv_2 = df2.fillna(df2.median())
            data_frame_2 = mv_2
            st.write(mv_2)
        elif select_1 == "replace with 0":
            st.subheader("Metadata for dataset 2")
            mv_2 = df2.fillna(0)
            data_frame_2 = mv_2
            st.write(mv_2)
        elif select_1 == "remove entire row":
            st.subheader("Metadata for dataset 2")
            mv_2 = df2.dropna()
            data_frame_2 = mv_2
            st.write(mv_2)
        elif select_1 == "remove entire column":
            st.subheader("Metadata for dataset 2")
            mv_2 = df2.dropna(axis=1)
            data_frame_2 = mv_2
            st.write(mv_2)
        else:
            upload_file2.info("Please select any one")

    math_functions_1 = btn2.checkbox("Apply math operation ")
    if math_functions_1:
        math_function_1 = ["None", "basic", "compare"]
        oper_1 = st.sidebar.selectbox("select a function for dataset 2", math_function_1)
        if oper_1 == "basic":
            st.subheader("basic operations for dataset 2")
            all_columns_1 = data_frame_2.columns.tolist()
            col5 = st.sidebar.selectbox("choose the variable for A for dataset 2", all_columns_1)
            col6 = st.sidebar.selectbox('choose the variable for B for dataset 2', all_columns_1)
            option_1 = ['None', 'Add', 'Sub', 'Mul', 'Div']
            arithmetic_1 = st.sidebar.selectbox("select the arithmetic operator for dataset 2", option_1)

            if arithmetic_1 == "Add":
                st.header("ADDITION")
                data_frame_2['ADDITION'] = data_frame_2[col5] + data_frame_2[col6]
                st.write(data_frame_2)


            elif arithmetic_1 == "Sub":
                st.header("SUBTRACTION")

                data_frame_2['SUBTRACTION'] = data_frame_2[col5] - data_frame_2[col6]

                st.write(data_frame_2)

            elif arithmetic_1 == "Mul":
                st.header("MULTIPLICATION")

                data_frame_2['MULTIPLICATION'] = data_frame_2[col5] * data_frame_2[col6]

                st.write(data_frame_2)

            elif arithmetic_1 == "Div":
                st.header("DIVISION")

                data_frame_2['DIVISION'] = data_frame_2[col5] / data_frame_2[col6]

                st.write(data_frame_2)

        elif oper_1 == "compare":
            st.subheader("comparison operations for dataset 2")
            all_columns_1 = data_frame_2.columns.tolist()
            col7 = st.sidebar.selectbox("choose the variable for A for dataset 2", all_columns_1)
            col8 = st.sidebar.selectbox("choose the variable for B for dataset 2", all_columns_1)
            conditions_1 = [data_frame_2[col7] > data_frame_2[col8],
                            data_frame_2[col7] < data_frame_2[col8],
                            data_frame_2[col7] == data_frame_2[col8]]

            # define choices
            choices_1 = ['TRUE', 'FALSE', 'EQUAL']

            # create new column in DataFrame that displays results of comparisons
            data_frame_2['comparison'] = np.select(conditions_1, choices_1)
            data_frame_2['Diff'] = np.where(data_frame_2[col7] == data_frame_2[col8], 0, data_frame_2[col7] - data_frame_2[col8])
            st.write(data_frame_2)
    # join two datasets
    st.subheader("JOIN TWO DATASETS")
    df_index = pd.merge(data_frame, data_frame_2, right_index=True, left_index=True)

    st.write(df_index)

else:
    st.info("**PLEASE UPLOAD A DATASET**")
