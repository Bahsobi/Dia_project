
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import statsmodels.api as sm

# ---------- Custom Styling (Blue Theme) ----------
st.markdown(
    """
    <style>
        .stApp {
            background-color: #e0f7fa;  /* Light Blue */
        }
        .stSidebar {
            background-color: #b2ebf2;  /* Sidebar Blue */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Header ----------
st.markdown(
    """
    <div style='display: flex; justify-content: center; align-items: center; flex-direction: column;'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/8/83/TUMS_Signature_Variation_1_BLUE.png' width='200' style='margin-bottom: 10px;'/>
    </div>
    """,
    unsafe_allow_html=True
)

st.title('🤖🩺 Machine Learning APP for Predicting Retinopathy Diabetes Risk')
st.info('Predict the **Diabetes Retinopathy** status based on health data using xgboost and Logistic Regression.')








