import pandas as pd

def print_csv_summary():
    print("Printing CSV summary...")
    pass

def df_has_labeled_rows_and_columns(df):
    has_labeled_rows = not df.index.is_numeric()
    has_labeled_columns = not df.columns.is_numeric()
    return has_labeled_rows and has_labeled_columns