import streamlit as st
from calculation import charges
# st.write("Hello world")
# x=st.text_input("Favourite movie?")
# st.write(f"Your favourite movie is:{x}")
# is_clicked=st.button("Click me")
# st.write("##This is a H2 title!")
# st.link_button("Profile",url="/profile")
# st.info("hi")

regions={
    "southwest":"southwest",
    "southeast":"southeast",
    "northwest":"northwest",
    "northeast":"northeast"
  }


def main():
  st.title("Medical charges prediction")
  st.write("This model is built by Kanak Khaitan.It tells the Individual medical costs billed by health insurance")
  
  gender=st.radio("sex",["male","female"],horizontal=True)
  age=st.slider("age",18,64,30)
  children=st.selectbox(
    "No of children?",
    [0,1,2,3,4,5]
  )
  smoker=st.radio("smoker",["yes","no"],horizontal=True)
  region=st.selectbox(
    "region?",
    ["southwest","southeast","northwest","northeast"]
  )  
  
  c1,c2=st.columns(2)
  with c1:
    height=st.number_input("height(cm)",100,200,150)
    
  with c2:
    weight=st.number_input("weight(kg)",30,200,60)
    
  bmi = weight / (height / 100) ** 2
  st.text(f"Your BMI is {bmi:.2f}")
  
  
  if st.button("calculate"):
    with st.spinner("Calculating..."):
      result_dict = charges(
      age=age,
      bmi=bmi,
      children=children,
      smoker=smoker,
      sex=gender,
      region=region
    )
      
    st.success(f"Predicted charges: ${result_dict['charges_prediction']:.2f}")

      
  
  
  
if  __name__ == "__main__":
    main()
  