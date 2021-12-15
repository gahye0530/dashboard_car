import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_app() :

    st.subheader('EDA 화면입니다.')
    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')
    radio_menu = ['데이터프레임', '통계치', '컬럼 정보']
    selected_radio = st.radio('선택하세요', radio_menu)

    if selected_radio == '데이터프레임' :
        st.dataframe(df)
    elif selected_radio =='통계치' :
        st.dataframe(df.describe())
    elif selected_radio == '컬럼 정보' :
        st.dataframe(df.columns)

    # 컬럼을 선택하면 해당 컬럼들만 데이터프레임 표시하는 화면
    # print(df.columns)
    selected_columns = st.multiselect('컬럼을 선택하세요', df.columns)
    if len(selected_columns) != 0 :
        st.dataframe(df[selected_columns])
    else :
        st.write('선택한 컬럼이 없습니다.')

    # 상관관계 분석을 위한 상관계수 보여주는 화면 개발
    st.subheader('상관계수')
    # st.dataframe(df.corr())
    df_corr = df.iloc[:,3:]
    selected_corr = st.multiselect('상관계수 컬럼선택', df_corr.columns)

    # 유저가 1개라도 컬럼을 선택했을 경우
    if len(selected_corr) != 0 :
        st.dataframe(df[selected_corr].corr())
        # 상관계수를 수치로도 구하고, 차트로도 표시하라.
        fig = sns.pairplot(data = df_corr[selected_corr])
        st.pyplot(fig)

    # 유저가 컬럼을 선택하지 않은 경우
    else : st.write('선택한 컬럼이 없습니다.')

    # 유저가 컬럼을 선택하면,
    # 해당 컬럼의 min과 max에 해당하는 사람이 누구인지
    # 그 사람의 데이터를 화면에 보여주는 기능 개발
    # print(df.columns)
    # print(df.dtypes!=object)
    number_columns = df.columns[df.dtypes!=object]
    selected_maxmin = st.selectbox('컬럼 선택', number_columns)
    # selected_maxmin은 컬럼을 선택한 상태
    
    if selected_maxmin is not None :
        st.text('최대값')
        # 선택한 컬럼의 최소값에 해당되는 사람의 데이터 출력
        st.dataframe(df.loc[df[selected_maxmin]==df[selected_maxmin].max(),])
        st.text('최소값')
        # 선택한 컬럼의 최대값에 해당하는 사람의 데이터 출력
        st.dataframe(df.loc[df[selected_maxmin]==df[selected_maxmin].min(),])