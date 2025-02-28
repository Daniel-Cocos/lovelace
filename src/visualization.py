import matplotlib.pyplot as plt
import seaborn as sns


def plot_health_status_pie(df):
    plt.figure(figsize=(6, 6))
    df["health_status"].value_counts().plot.pie(
        autopct="%1.1f%%", startangle=90, cmap="coolwarm"
    )
    plt.title("Health Status Distribution")
    plt.ylabel("")  # Hide the y-label
    plt.show()


def plot_gender_distribution(df):
    plt.figure(figsize=(6, 6))
    sns.countplot(data=df, x="gender")
    plt.title("Gender Distribution")
    plt.show()


def plot_correlation_heatmap(df):
    plt.figure(figsize=(10, 8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()


def plot_pairplot(df):
    sns.pairplot(df, hue="health_status", palette="coolwarm")
    plt.show()


def plot_age_vs_health_status(df):
    sns.boxplot(data=df, x="health_status", y="age", palette="coolwarm")
    plt.title("Age vs Health Status")
    plt.show()


def plot_cholesterol_vs_health_status(df):
    sns.boxplot(x="health_status", y="cholesterol", data=df, palette="coolwarm")
    plt.title("Cholesterol vs Health Status")
    plt.show()
