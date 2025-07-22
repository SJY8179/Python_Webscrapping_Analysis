# streamlit run streamlit_korea.py
import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

data = pd.read_csv('data/data_draw_korea.csv')
seoul_df = data.loc[data['광역시도'] == '서울특별시']

st.title(" Pandas DataFrame & 행정구역")
st.dataframe(seoul_df)

# font name을 알고 있다면 생략가능
#한글폰트 path 설정
plt.rc('font', family="Malgun Gothic")

# 시각화
st.subheader(" Seaborn 그래프")
fig, axes1 = plt.subplots(figsize=(18, 12))
axes1.set_title("행정구역별 인구수")
sns.barplot(x='행정구역',y='인구수',data=seoul_df.sort_values(by='인구수',ascending=False),ax=axes1, hue='행정구역')

st.pyplot(fig)