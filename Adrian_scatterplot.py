import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date
import numpy as np

def create_scatterplot(csv_file_path):

    try:
        df = pd.read_csv(csv_file_path)
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
        return
    
    df['Date'] = pd.to_datetime(df['Date'])
    df['Week'] = (df['Date'] - df['Date'].min()).dt.days /14
    
    latest_files = df.loc[df.groupby('Filename')['Date'].idxmax()]
    latest_files = latest_files.sort_values('Date')
    
    #colouring
    unique_authors = latest_files['Author'].unique()
    colors = plt.cm.Dark2(range(len(unique_authors)))
    author_color_map = {author: colors[i] for i, author in enumerate(unique_authors)}
    
    plt.figure(figsize=(10, 8))
    plt.xlabel('Files', fontsize=12)
    plt.ylabel('Week', fontsize=12)
    #mapping colours
    for author in unique_authors:
        author_data = latest_files[latest_files['Author'] == author]
        plt.scatter(range(len(author_data)), author_data['Week'], 
                   alpha=0.7, s=60, label=author, c=[author_color_map[author]])
    #plot formation
    
    plt.savefig('scatterplot.png', dpi=300, bbox_inches='tight')  
    plt.show()   

csv_file = 'data/file_rootbeer.csv'  # Update this path if needed

# Create enhanced scatter plot with author information
create_scatterplot(csv_file)