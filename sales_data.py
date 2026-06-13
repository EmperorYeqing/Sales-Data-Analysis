# %% [markdown]
# # Project 03: Sales Data Analysis
# 
# ## Business Scenario
# 
# Aim: Understand Business problem, hired by a retail company
# 
# Objectives: Management want to understand:
# 1. Which product sells the most?
# 2. which product generates the most revenue?
# 3. Which category performs best?
# 4. what are the monthly sales trends?
# 5. which month was the best?
# 6. Which month was the worst?
# 7. Which products should receive more marketing investment?

# %% [markdown]
# ## STEP 01: Import

# %%
#Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %% [markdown]
# ## STEP 02: Load the dataset

# %%
df = pd.read_csv(r"sales_data.csv")
df

# %% [markdown]
# ## STEP 03: Understand the dataset

# %%
df.head()
df.info()
df.describe()

# %% [markdown]
# The dataset 10 rows and 5 columns with each rows describing sales details for a particular date, each columns(product, quantity, category,unit_price) provide individual description of each day sales. There are 2 columns with integer datatype (Quantity and Unit _price) and 3 columns with string datatype (Category, Product, Date).
# Note: Date as a string will be converted to a datetime datatype later.

# %% [markdown]
# ## STEP 04: Create KPIs - Feature Engineering

# %% [markdown]
# ### KPI 1: Revenue
# Revenue = quantity x Unit_Price

# %%
df["Revenue"] = df["Quantity"] * df["Unit_Price"]
df

# %% [markdown]
# ### KPI 1: Month
# Convert Date to datetime

# %%
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month_name()
df["Month_Num"] = df["Date"].dt.month
df

# %% [markdown]
# Converted Date which is initially a string to a datetime datatype, then get the months name and pass the values to a new KPI column (Month) created

# %% [markdown]
# ## STEP 05: Exploratory Data Analysis (EDA)

# %% [markdown]
# ### First Analysis: Product Performance
# Questions
# 1. Most profitable product?
# 2. Least profitable product?

# %%
df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

# %% [markdown]
# Answers:
# 
# 1. Phone is the most profitable product and it generated a total revenue of 18000
# 2. Chair is the product that generated the lowest revenue of 3960

# %% [markdown]
# ### Second Analysis: Category Performance
# Questions
# 1. Best category?
# 2. Lowest category?

# %%
df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

# %% [markdown]
# Answers:
# 
# 1. Electronics category performed the best with a revenue generation of 32400
# 2. Furniture performed the lowest with a revenue generation of 8460

# %% [markdown]
# ### Third Analysis: Monthly Trend
# Questions
# 1. Best month?
# 2. Worst month?
# 3. Is revenue increasing overtime?

# %%
monthly_rev = df.groupby(["Month_Num","Month"])["Revenue"].sum()
monthly_rev
Growth_percent = monthly_rev.pct_change() * 100
Growth_percent

# %% [markdown]
# Answers:
# 
# 1. May is the best month with the highest revenue generation of 12600
# 2. February is the month that has the worst revenue generation of 3800
# 3. No, There is a volatile fluctuation across Months with March and May having high increase in revenue and February and April having sharp revenue declines. Nevertheless, revenue ended at a higher value than the starting value

# %% [markdown]
# ### Fourth Analysis: Sales Performance - Quantity Analysis
# Questions
# 1. Highest quantity sold?
# 2. Lowest quantity sold?
# 3. Is there any relationship between sales volume and revenue generation?

# %%
df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)

df[["Quantity", "Revenue"]].corr()

# %% [markdown]
# correlation = 1 - Perfect positive correlation
# correlation = -0.2 - weak negative correlation
# there is no relationship between both column

# %% [markdown]
# Answers:
# 
# 1. Phone has the highest sales volume as the most sold product
# 2. Table has the lowest sales volume as the least sold product
# 3. There is weak or no relationship between Quantity and revenue generated( from the result of the correlation analysis)

# %% [markdown]
# ## STEP 06: Visualization

# %% [markdown]
# ### Revenue by Product

# %%
df.groupby("Product")["Revenue"].sum().plot(kind="barh",ylabel="Revenue",color="Orange")
plt.title("Total Revenue by Product")
plt.show()

# %% [markdown]
# ### Revenue by Category

# %%
df.groupby("Category")["Revenue"].sum().plot(kind="barh",ylabel="Revenue",color="Green")
plt.title("Total Revenue by Category")
plt.show()

# %% [markdown]
# ### Monthly Revenue Trend

# %%
monthly_rev.plot(kind="line",ylabel="Revenue",xlabel="Month",marker="o",grid=True,mfc="Green",mec="Green")
plt.title("Monthly Revenue Trend")
plt.show()

# %% [markdown]
# ## STEP 07: Key Insights
# 1. Phone is the most sold product and the product with the highest generated revenue and it generated a total revenue of 18000 and laptop is the second best product slightly behind phone in generated revenue.
# 2. Chair is the product that generated the lowest revenue of 3960
# 3. Electronics category performed the best with a revenue generation of 32400
# 4. Furniture performed the lowest with a revenue generation of 8460
# 6. May is the best month with the highest revenue generation of 12600
# 7. February is the month that has the worst revenue generation of 3800
# 8. There is a volatile fluctuation across Months with March and May having high increase in revenue and February and April having sharp revenue declines. 
# 10. Despite the fluctuation in revenue across, revenue ended at a higher value than the starting value.
# 11. March has the highest percentage revenue transition from previous month despite falling  slightly behind May in total revenue.
# 12. Chair is the second most sold product despite having the least generated revenue.

# %% [markdown]
# ## STEP 08: Executive Recommendation

# %% [markdown]
# Based on the Analysis done within the limit of available dataset, i would like to make the following recommendation:
# 1. More phone and laptop product should be purchased since they are most profitable among all product.
# 2. investigation should be made on both phone and laptop product to know what factors and marketing strategy that drives their high profitability, and also to check if the methods can be used in boosting the low performing products.
# 3. investigation should also be made into the volatile fluctuation of sales record to assess the causes and to prepare future mitigative method in managing such volatility.
# 4. Customer preference should also be investigated before future purchases to know which product category is trending. more also, the factors behind the trend of electronic products should be analyze to know if future purchase should be heavily invested in the category.
# 5. Causes and factors surrounding low performance of furniture product should also be assessed for future actions.


