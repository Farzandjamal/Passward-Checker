#lets build passward checker
import re
import streamlit as st
def passcheck(passward):
  p_length=len(passward)>=8
  d1= re.search(r'\d',passward)
  d2=re.search(r'[A-Z]',passward)
  d3=re.search(r'[a-z]',passward)
  d4=re.search(r"[@$!%*?&#]",passward)
  score=sum([
  p_length, 
  bool(d1),
  bool(d2),
  bool(d3),
  bool(d4)
])
  if score==5:
   st.success(f'**{passward}** is strong passward ✅')
  elif score>=3:
   st.warning(f'**{passward}** is medium passward ⚠️')
  else:
   st.error(f'**{passward}** is weak passward ❌')
#lets use streamlit 
st.set_page_config(layout='wide')
st.title('🔒password checker')
st.caption('Mr.jamal')
with st.form('form'):
 passward=st.text_input('🔑 Password Query',placeholder='enter passward here')
 button=st.form_submit_button('Check',type='primary')
if passward and button:
 passcheck(passward)
elif button:
  st.success('Enter passward first')
  
#lets add instruction
with st.expander("💡 Click here for Strength Instructions"):
    st.markdown("""
    - **Length:** 8 or more characters
    - **Numbers:** At least one digit (0-9)
    - **Casing:** Mix of UPPER and lower case
    - **Symbols:** Include chars like @, #, $, %
    """)
  