# the file will ingest data, clean it, generate summary statistics and produce two plots at the end
#import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Data Loading
def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: Loaded data.
    """
    return pd.read_csv(file_path)

#Data Cleaning
def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the data by removing missing values.

    Parameters:
    data (pd.DataFrame): Input data.

    Returns:
    pd.DataFrame: Cleaned data.
    """
    return data.dropna()

#Data Analysis
def analyze_data(data: pd.DataFrame) -> dict:
    """
    calculating summary statistics

    Parameters:
    data (pd.DataFrame): Input data.

    Returns:
    dict: Summary statistics.
    """
    summary_stats = {
        'mean': data.mean(),
        'median': data.median(),
        'std': data.std()
    }
    return summary_stats

#Data Visualization
def visualize_data(summary_stats: dict) -> None:
    """
    Visualize summary statistics

    Parameters:
    summary_stats (dict): Summary statistics.

    Returns:
    None
    """
    plt.bar(summary_stats.keys(), summary_stats.values())
    plt.xlabel('Statistics')
    plt.ylabel('Values')
    plt.title('Summary Statistics')
    plt.show()

#Correlation Plot
def correlation_plot(data: pd.DataFrame) -> None:
    """
    correlation plot for the data.

    Parameters:
    data (pd.DataFrame): Input data.

    Returns:
    None
    """
    corr_matrix = data.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Plot')
    plt.show()

#execution
if __name__ == "__main__":
    #Load data
    file_path = 'data.csv'
    data = load_data(file_path)

    #Clean data
    cleaned_data = clean_data(data)

    #Analyze data
    summary_stats = analyze_data(cleaned_data)
    print("Summary Statistics:")
    print(summary_stats)

    #Visualize data
    visualize_data(summary_stats)

    #Generate correlation plot
    correlation_plot(cleaned_data)
