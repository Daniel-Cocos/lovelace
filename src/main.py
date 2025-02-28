import data_loader as dl
import data_formatting as dformat

if __name__ == "__main__":
    # Load Dataset
    df = dl.load_data()
    print("Dataset Loaded:\n", df.head())  # Print the first few rows

    # Preprocess Data
    df = dformat.rename_columns(df)
    df = dformat.handle_missing_values(df)
    df = dformat.create_additional_columns(df)

    print(df.head()) # Print first few rows
