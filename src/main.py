import data_loader as dl
import data_formatting as dformat
import visualization as visualize
import model

if __name__ == "__main__":
    # Load Dataset
    df = dl.load_data()
    print("Dataset Loaded:\n", df.head())  # Print the first few rows

    # Preprocess Data
    df = dformat.rename_columns(df)
    df = dformat.handle_missing_values(df)
    df = dformat.create_additional_columns(df)

    print(df.head()) # Print first few rows

    # Exploratory Data Analysis
    visualize.plot_health_status_pie(df)
    visualize.plot_gender_distribution(df)
    visualize.plot_correlation_heatmap(df)
    visualize.plot_pairplot(df)
    visualize.plot_age_vs_health_status(df)
    visualize.plot_cholesterol_vs_health_status(df)

    # Split data into Training, Validation, and Test Sets
    X_train, X_val, X_test, y_train, y_val, y_test = model.split_data(df)

    # Train and Evaluate the Model
    trained_model = model.train_model(X_train, y_train)
    model.evaluate_model(trained_model, X_val, y_val)
