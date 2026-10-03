import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.title("Iris classifier")

iris = load_iris()
model = RandomForestClassifier().fit(iris.data, iris.target)

inputs = [st.slider(name, float(col.min()), float(col.max()), float(col.mean()))
          for name, col in zip(iris.feature_names, iris.data.T)]

st.write("Prediction:", iris.target_names[model.predict([inputs])[0]])
