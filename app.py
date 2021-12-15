import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
from eda_app import run_eda_app
# 이건 자동으로 생겼어from eda_app import run_eda_app

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



if __name__ =='__main__' : main()
