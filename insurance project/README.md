Car Insurance Claim Prediction

This project aims to predict whether a customer will file a claim on their car insurance using logistic regression. The goal is to identify the single most predictive feature from a dataset of customer attributes.

Project Overview

The dataset includes various features such as age, gender, driving experience, education, income, credit score, vehicle ownership, vehicle year, marital status, number of children, annual mileage, vehicle type, number of speeding violations, DUIs, and past accidents. The target variable is whether the customer filed a claim.

Steps

Data Exploration: Loaded and examined the dataset for data types, missing values, and distributions.
Data Cleaning: Filled missing values using the median.
Feature Encoding: Converted categorical variables to numeric using LabelEncoder.
Model Building: Built logistic regression models for each feature.
Performance Measurement: Calculated the accuracy of each model.
Best Feature Identification: Identified "driving experience" as the most predictive feature with an accuracy of 0.7771.
Results

The feature "driving experience" was found to be the best predictor for whether a customer will file a claim, achieving an accuracy of 77.71%. This insight can help insurance companies improve their risk assessment and resource allocation strategies.

Implications

Understanding that driving experience significantly impacts claim likelihood enables insurers to tailor their policies and pricing strategies better, leading to more efficient and targeted risk management.
