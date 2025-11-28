"""
Weather Data Visualizer - Programming for Problem Solving Assignment
Student: Kartik Sharma
Dataset: Daily Delhi Climate (Kaggle) [https://www.kaggle.com/datasets/sukhmandeepsinghbrar/daily-delhi-climate](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/daily-delhi-climate)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os  
from datetime import datetime


def load_and_inspect_data(file_path):
    """Task 1: Load CSV and inspect structure"""
    print("=== TASK 1: DATA ACQUISITION ===")
    df = pd.read_csv(file_path)
    print(f"Dataset shape: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nData info:")
    print(df.info())
    print("\nDescriptive stats:")
    print(df.describe())
    return df

def clean_data(df):
    """Task 2: Clean and process data"""
    print("\n=== TASK 2: DATA CLEANING ===")
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna()
    
    relevant_cols = ['date', 'meantemp', 'humidity', 'wind_speed', 'meanpressure']
    df = df[relevant_cols]
    df.set_index('date', inplace=True)
    print(f"Cleaned dataset shape: {df.shape}")
    print("Columns:", df.columns.tolist())
    return df

def statistical_analysis(df):
    """Task 3: NumPy statistical computations"""
    print("\n=== TASK 3: STATISTICAL ANALYSIS ===")
    daily_stats = df.agg(['mean', 'min', 'max', 'std']).round(2)
    print("Daily Statistics:")
    print(daily_stats)
    monthly_stats = df.resample('M').agg(['mean', 'min', 'max', 'std']).round(2)
    print("\nMonthly Statistics (first 5):")
    print(monthly_stats.head())
    yearly_stats = df.resample('Y').agg(['mean', 'min', 'max']).round(2)
    print("\nYearly Statistics:")
    print(yearly_stats.head())
    return daily_stats, monthly_stats, yearly_stats

def create_visualizations(df):
    """Task 4: Matplotlib visualizations (Bonus: Subplots)"""
    print("\n=== TASK 4: VISUALIZATIONS ===")
    plt.style.use('default')
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Delhi Weather Analysis - Key Insights', fontsize=16, fontweight='bold')
    
    # Plot 1: Daily Temperature
    axes[0,0].plot(df.index, df['meantemp'], color='red', linewidth=1)
    axes[0,0].set_title('Daily Temperature Trends', fontweight='bold')
    axes[0,0].set_xlabel('Date')
    axes[0,0].set_ylabel('Mean Temperature (°C)')
    axes[0,0].grid(True, alpha=0.3)
    
    # Plot 2: Monthly Temperature Bar
    monthly_temp = df['meantemp'].resample('M').mean()
    axes[0,1].bar(range(1,13), monthly_temp.groupby(monthly_temp.index.month).mean(), 
                  color='orange', edgecolor='black')
    axes[0,1].set_title('Average Temperature by Month', fontweight='bold')
    axes[0,1].set_xlabel('Month')
    axes[0,1].set_ylabel('Temperature (°C)')
    axes[0,1].set_xticks(range(1,13))
    
    # Plot 3: Humidity vs Temperature
    axes[1,0].scatter(df['meantemp'], df['humidity'], alpha=0.6, color='green', s=20)
    axes[1,0].set_title('Humidity vs Temperature', fontweight='bold')
    axes[1,0].set_xlabel('Temperature (°C)')
    axes[1,0].set_ylabel('Humidity (%)')
    axes[1,0].grid(True, alpha=0.3)
    
    # Plot 4: Wind Speed
    axes[1,1].plot(df.index, df['wind_speed'], color='blue', linewidth=1)
    axes[1,1].set_title('Daily Wind Speed Trends', fontweight='bold')
    axes[1,1].set_xlabel('Date')
    axes[1,1].set_ylabel('Wind Speed (km/h)')
    axes[1,1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('weather_plots_combined.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Main function - Run entire pipeline"""
    print("🚀 Weather Data Visualizer - Starting Analysis")
    print("="*50)
    
    DATA_FILE = 'delhi_weather.csv'
    
    if not os.path.exists(DATA_FILE):  
        print(f"❌ ERROR: {DATA_FILE} not found!")
        print("1. Download from: https://www.kaggle.com/datasets/sukhmandeepsinghbrar/daily-delhi-climate")
        print("2. Save as 'delhi_weather.csv' in this folder")
        return
    
    # Run pipeline
    df = load_and_inspect_data(DATA_FILE)
    df_clean = clean_data(df)
    statistical_analysis(df_clean)
    create_visualizations(df_clean)
    print("\n🎉 ANALYSIS COMPLETE! Check your folder for PNG files + CSVs")

if __name__ == "__main__":
    main()

