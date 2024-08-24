# Import necessary libraries
import pandas as pd

# Step 1: Load the financial data from the CSV file
# Read the CSV file into a pandas DataFrame
df = pd.read_csv("Financial Data BCG.csv")

# Step 2: Convert necessary columns to numeric types for calculations
df['Total Revenue'] = pd.to_numeric(df['Total Revenue'], errors='coerce')
df['Net Income'] = pd.to_numeric(df['Net Income'], errors='coerce')

# Step 3: Define a function to calculate key financial metrics
def calculate_metrics(df):
    # Calculate revenue growth year-over-year
    df['Revenue Growth'] = df.groupby('Company')['Total Revenue'].pct_change() * 100
    # Calculate net income growth year-over-year
    df['Net Income Growth'] = df.groupby('Company')['Net Income'].pct_change() * 100
    return df

# Apply the function to the DataFrame
df = calculate_metrics(df)

# Step 4: Define the chatbot function with predefined queries
def financial_chatbot(user_query):
    # Predefined responses based on queries
    if user_query == "What is the total revenue of Microsoft?":
        revenue = df.loc[df['Company'] == 'Microsoft', 'Total Revenue'].sum()
        return f"The total revenue of Microsoft is ${revenue:.2f}."
    elif user_query == "What is the net income growth of Apple in 2023?":
        growth = df.loc[(df['Company'] == 'Apple') & (df['Fiscal Year'] == 2023), 'Net Income Growth'].values[0]
        return f"Apple's net income growth in 2023 was {growth:.2f}%."
    elif user_query == "How has Tesla's revenue changed over the last year?":
        revenue_growth = df.loc[(df['Company'] == 'Tesla'), 'Revenue Growth'].iloc[-1]
        return f"Tesla's revenue growth over the last year was {revenue_growth:.2f}%."
    elif user_query == "What is the total revenue of Apple?":
        revenue = df.loc[df['Company'] == 'Apple', 'Total Revenue'].sum()
        return f"The total revenue of Apple is ${revenue:.2f}."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Example of using the chatbot with predefined queries
user_query = "What is the total revenue of Microsoft?"
response = financial_chatbot(user_query)
print(response)

user_query = "What is the net income growth of Apple in 2023?"
response = financial_chatbot(user_query)
print(response)

user_query = "How has Tesla's revenue changed over the last year?"
response = financial_chatbot(user_query)
print(response)
