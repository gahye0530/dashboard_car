import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
from eda_app import run_eda_app # 자동
from ml_app import run_ml_app # 자동

def main() :
    st.title('자동차 가격 예측')

    # 사이드바 메뉴
    menu=['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home' :
        st.write('Home을 클릭하셨습니다.')
        st.write('왼쪽의 사이드바에서 선택하세요.')
    elif choice == 'EDA' :
        run_eda_app()
    elif choice == 'ML' :
        run_ml_app()



if __name__ =='__main__' : main()
