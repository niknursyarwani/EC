import streamlit as st
import pandas as pd

# Default values
DEFAULT_CO_R = 0.8  # Default Crossover Rate
DEFAULT_MUT_R = 0.2  # Default Mutation Rate

# Sidebar inputs for parameters
st.sidebar.header("Genetic Algorithm Parameters")
co_r = st.sidebar.slider(
    "Crossover Rate (CO_R)", 
    min_value=0.0, 
    max_value=0.95, 
    value=DEFAULT_CO_R, 
    step=0.01,
    help="Adjust the crossover rate for the genetic algorithm (default: 0.8)"
)
mut_r = st.sidebar.slider(
    "Mutation Rate (MUT_R)", 
    min_value=0.01, 
    max_value=0.05, 
    value=DEFAULT_MUT_R, 
    step=0.001,
    help="Adjust the mutation rate for the genetic algorithm (default: 0.2)"
)

# Main Interface
st.title("TV Scheduling using Genetic Algorithm")
st.write("### Genetic Algorithm Parameters")
st.write(f"- **Crossover Rate (CO_R)**: {co_r}")
st.write(f"- **Mutation Rate (MUT_R)**: {mut_r}")

# Upload CSV File
st.write("### Upload Program Ratings CSV")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    # Read and display the uploaded CSV file
    data = pd.read_csv(uploaded_file)
    st.write("#### Program Ratings Data")
    st.dataframe(data)

    # Example of Genetic Algorithm Schedule Generation (Replace with your implementation)
    st.write("#### Generated Schedule")
    schedule = data.sample(frac=1).reset_index(drop=True)  # Example: Randomized schedule
    st.dataframe(schedule)
