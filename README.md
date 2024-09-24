# Well Being Watch

Well Being Watch is a machine learning project aimed at predicting mental health conditions. The project uses a logistic regression model trained with `numpy`, `pandas`, and `scikit-learn`, and is deployed using Flask for the client-side interface.

## Table of Contents

- Introduction
- Features
- Installation
- Usage

## Introduction

Mental health is a critical aspect of overall well-being. Early identification of potential mental health issues can lead to timely intervention and support. Well Being Watch leverages machine learning to predict mental health conditions based on various features.

**Note:** The dataset used for training the model is limited, which means the predictions may also be limited in accuracy and scope.

## Features

- **Data Preprocessing**: Handling missing values, encoding categorical variables, and scaling features.
- **Exploratory Data Analysis (EDA)**: Understanding data distribution, relationships, and key insights through visualizations.
- **Model Building**: Implementing logistic regression using `scikit-learn`.
- **Model Evaluation**: Assessing model performance using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.
- **Web Interface**: A Flask-based client-side interface for interacting with the model.

## Installation

To run this project, you need to have Python installed. Follow these steps to set up the project:

1. Clone the repository:
    ```bash
    https://github.com/Ashmil114/Well-Being-Watch.git
    cd Well-Being-Watch
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Train the model:
    Use Jupyter Notebook (dataset/Train Model.ipynb)

2. Run the Flask app:
    ```bash
    python app.py
    ```

3. Open your browser and go to `http://127.0.0.1:5000` to interact with the web interface.



