import streamlit as st
from PIL import Image
import pickle
with open('iris_pickle','rb') as f:
    mp=pickle.load(f)

def prediction(sepal_length,sepal_width,petal_length,petal_width):
    result=mp.predict([[sepal_length,sepal_width,petal_length,petal_width]])
    return result

def main():
  st.title("Iris Flower prediction")
  st.header('Model used - Random forest classifier with 98% accuracy')

  setosa = Image.open('setosa.png')
  versicolor=Image.open('versicolor.png')
  verginica=Image.open('virginica.png')

  sepal_length=st.number_input('Sepal Length')
  sepal_width = st.number_input('Sepal Width')
  petal_length = st.number_input('Petal Length')
  petal_width= st.number_input('Petal_width')

  if st.button("Predict"):
      res=prediction(sepal_length,sepal_width,petal_length,petal_width)
      st.success(res)
      if(res==['setosa']):
          st.image(setosa)
      elif(res==['virginica']):
          st.image(verginica)
      else:
          st.image(versicolor)





if __name__ == '__main__':
    main()