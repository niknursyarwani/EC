import streamlit as st
import pandas as pd

# Set default values
DEFAULT_CO_R = 0.8
DEFAULT_MUT_R = 0.2

# Sidebar for Genetic Algorithm Parameters
st.sidebar.header("Genetic Algorithm Parameters")
co_r = st.sidebar.slider("Crossover Rate (CO_R)", 0.0, 0.95, DEFAULT_CO_R, 0.01)
mut_r = st.sidebar.slider("Mutation Rate (MUT_R)", 0.01, 0.05, DEFAULT_MUT_R, 0.001)

# Main Interface
st.title("TV Scheduling using Genetic Algorithm")
st.write(f"Crossover Rate: {co_r}")
st.write(f"Mutation Rate: {mut_r}")

# Example of displaying a CSV file (replace with your genetic algorithm output)
uploaded_file = st.file_uploader("Upload Program Ratings CSV", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.dataframe(data)

    # Simulate genetic algorithm output
    st.write("### Generated Schedule")
    schedule = data.sample(frac=1).reset_index(drop=True)  # Randomized schedule
    st.dataframe(schedule)
