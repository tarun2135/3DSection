import streamlit as st
import pandas as pd

def main():
    # Set page layout to wide (full screen)
    st.set_page_config(layout="wide")

    file_path = r"Section - D.xlsx"
    df = load_data(file_path, section='D')  # Load data for section D
    if df is not None:
        # Convert dataframe to HTML table and render it using markdown
        st.markdown(get_table_html(df), unsafe_allow_html=True)
    else:
        st.write("No data to display.")

def get_table_html(df):
    # Convert DataFrame to HTML table string
    table_html = df.to_html(index=False, escape=False, classes=["dataframe"])

    # Modify HTML string to set table width to 100% and center align text
    table_html = table_html.replace('<table', '<table style="width:100%; text-align:center;"')

    return table_html

def load_data(file_path, section):
    try:
        df = pd.read_excel(file_path)
        # Filter dataframe based on section
        df_section = df[df['Section'] == section]
        return df_section
    except Exception as e:
        st.error(f"An error occurred while loading the data: {e}")
        return None

if __name__ == "__main__":
    main()
