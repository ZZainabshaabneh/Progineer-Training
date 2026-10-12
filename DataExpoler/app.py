
import streamlit as st
import pandas as pd
from data_utils import load_csv, get_missing_values, get_summary_statistics
st.title("Data Explorer")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        df = load_csv(uploaded_file)

        if df.empty or len(df.columns) == 0:
            st.error("The uploaded CSV file is empty.")
        else:
            st.subheader("First 5 Rows")
            st.dataframe(df.head())

            st.subheader("Dataset Shape")
            st.write(
                f"{df.shape[0]} rows × {df.shape[1]} columns"
            )

            st.subheader("Column Types")
            st.write(df.dtypes.astype(str))

            st.subheader("Missing Values")
            st.write(get_missing_values(df))
            
            st.subheader("Summary Statistics")
            summary = get_summary_statistics(df)

            if not summary.empty:
                st.write(summary)
            else:
                st.info("No numeric columns available.")

            column = st.sidebar.selectbox(
                "Choose a column",
                df.columns.tolist()
            )

            chart_type = st.sidebar.selectbox(
                "Choose chart type",
                ["Bar Chart", "Histogram", "Line Chart"]
            )

            st.subheader(f"{chart_type} - {column}")

            if chart_type == "Bar Chart":
                chart_data = df[column].value_counts().head(20)
                st.bar_chart(chart_data)

            elif chart_type == "Histogram":
                if pd.api.types.is_numeric_dtype(df[column]):
                    histogram_data = df[column].dropna()
                    st.bar_chart(
                        histogram_data.value_counts().sort_index()
                    )
                else:
                    st.warning(
                        "Histogram is available for numeric columns only."
                    )

            elif chart_type == "Line Chart":
                if pd.api.types.is_numeric_dtype(df[column]):
                    st.line_chart(df[column].dropna())
                else:
                    st.warning(
                        "Line Chart is available for numeric columns only."
                    )



    except (pd.errors.ParserError, UnicodeDecodeError, ValueError):
        st.error(
            "Unable to read this file. Please upload a valid CSV file."
        )
