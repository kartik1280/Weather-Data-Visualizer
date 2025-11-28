# 🌤️ Weather Data Visualizer

Analyzes Delhi weather data (2013-2018) to create insightful visualizations for climate awareness using Pandas, NumPy, and Matplotlib.

![Delhi Weather Dashboard](weather_plots_combined.png)

## 📋 Table of Contents
- [Dataset](#-dataset)
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Key Insights](#-key-insights)
- [File Structure](#-file-structure)

## 📊 Dataset
**Daily Delhi Climate Dataset** from Kaggle (1576 records, 2013-2018) [web:33]
- Columns: `date`, `meantemp`, `humidity`, `wind_speed`, `meanpressure`
- Source: [Kaggle Daily Delhi Climate](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/daily-delhi-climate)

## ✨ Features
- ✅ **Data loading & inspection** (Pandas)
- ✅ **Data cleaning** (missing values, datetime conversion)
- ✅ **Statistical analysis** (NumPy: mean, std, min/max)
- ✅ **4 Professional visualizations** (Matplotlib subplots - Bonus!)
- ✅ **Grouping & aggregation** (monthly/seasonal analysis)
- ✅ **Automated exports** (CSV, PNG plots, Markdown report)

## 🎮 Demo
Run the script → **4 plots generated instantly**:

| Plot Type | Description |
|-----------|-------------|
| Line Chart | Daily temperature trends (2013-2018) |
| Bar Chart | Monthly average temperatures |
| **Scatter Plot** | Humidity vs Temperature correlation |
| Line Chart | Daily wind speed patterns |

![Monthly Temperature](monthly_temp_bar.png)

## 🛠 Installation

1. **Clone the repo**
git clone https://github.com/kartik1280/Weather-Data-Visualizer.git
cd Weather-Data-Visualizer


2. **Install dependencies**
pip install pandas numpy matplotlib


3. **Download dataset**
- Get `delhi_weather.csv` from [Kaggle](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/daily-delhi-climate)
- Place in project root

## 🚀 Usage
python main.py


**Output**: 6 files + 4 plots generated automatically! 🎉

## 📈 Key Insights (From Analysis)
-Average temperature: 25.22°C (peaks >38°C in summer)
-High year-round humidity (60% avg)
-Monsoon season: Highest temperature variability
-Wind speeds peak during transitional months


**Full report**: [report.md](report.md)

## 📁 File Structure
weather-data-visualizer-yourname/
├── main.py # Main analysis script
├── delhi_weather.csv # Original dataset (Kaggle)
├── cleaned_delhi_weather.csv # Cleaned data (auto-generated)
├── daily_statistics.csv # Stats export
├── monthly_aggregates.csv # Monthly analysis
├── weather_plots_combined.png # 4 subplots (Bonus!)
├── monthly_temp_bar.png # Monthly bar chart
├── report.md # Analysis summary
└── README.md # You're reading it! 📖


## 👨‍💻 Author
**Kartik Sharma** - KR Mangalam University CSE (Data Science) 

## 📚 Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat&logo=matplotlib&logoColor=white)

## 📄 License
This project is for **academic submission only**. Cite dataset source in your report.

---

