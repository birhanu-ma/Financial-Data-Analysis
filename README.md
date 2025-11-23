# Financial-Data-Analysis

📈 Nova Financial Insights: Project Setup
This repository contains the complete analysis pipeline for the Nova Financial Insights project. The primary objective is to establish a robust, reproducible, and modular development environment to model the correlation between technical stock signals and financial news sentiment.

🎯 Project Business Objectives
The project is designed to enhance predictive analytics capabilities by focusing on two core tasks:

Quantitative Analysis (Task 1): Measure stock momentum using indicators (MACD, RSI) and identify technical divergence and trend strength across core tech stocks.

Correlation Modeling (Task 2 & 3): Establish the statistical relationship between calculated news sentiment (TextBlob Polarity) and stock price movements, accounting for the non-stationary volatility in the news time series.

📁 Complete Repository Structure
The project adheres to a standard package structure, treating the code in src/ as a reusable library.

├── .github/
│   └── workflows/  # GitHub Actions CI/CD workflows
├── .venv/          # Virtual environment directory (ignored by Git)
├── notebooks/      # Exploratory Data Analysis (EDA) and analysis reports
│       ├── AAPL.ipynb      # Quantitative Analysis Report
│       ├── AMZN.ipynb
│       ├── GOOG.ipynb
│       ├── META.ipynb
│       ├── MSFT.ipynb
│       ├── NVDA.ipynb
│       └── sentiment_analysis.ipynb # Sentiment and Time Series Analysis
├── src/            # Custom Python modules (e.g., data cleaning functions)
│       └── loadData.py     # Placeholder for data loading functions
├── scripts/        # Utility scripts (e.g., model execution)
├── tests/          # Unit and integration tests
├── .gitignore      # Ensures environment files (.venv, *.egg-info) are excluded
├── requirements.txt # Lists all external and local dependencies
└── setup.py        # Defines the project as an importable package
⚙️ Reproducing the Environment
To ensure a robust and identical development environment, follow these three steps to install all dependencies and configure the local package.

A. Clone the Repository
Bash

git clone https://github.com/[your-username]/nova-financial-insights.git
cd nova-financial-insights
B. Create and Activate a Virtual Environment
Bash

# 1. Create the environment
python -m venv .venv

# 2. Activate the environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows (Command Prompt):
.venv\Scripts\activate
C. Install Dependencies
The requirements.txt file is configured to install all external dependencies and the local src/ directory in editable mode (-e .).

Bash

# This command installs all required libraries and configures the 'src' package
pip install -r requirements.txt
🧩 Usage
1. Run Analysis Notebooks
Start the Jupyter server from the project root directory and navigate to the notebooks/ folder to view the completed analysis reports.

Bash

jupyter notebook
2. Run Tests
Verify the functionality of your reusable code modules located in src/.

Bash

pytest tests/
3. Run Utility Scripts
Example: To run a placeholder script for future modeling:

Bash

python scripts/run_model.py