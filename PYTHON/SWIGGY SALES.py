import pandas as pd

df = pd.read_excel(r"C:\swiggy_data.xlsx") 
print(df)

# print(df.head())B 

# print(df.tail())

# print("Rows & columns: ", df.shape)

# print('\n Column names')

# print(df.columns)

# print(df.info) dont print this
# df.info()
# df.describe()
# print(df["Price (INR)"].mean())
# print("no of rows: ", df.shape[0])
# print("no of columns: ", df.shape[1])
# print(df.dtypes)
# df.describe()

# KPI'S to be calculated:
# 1 TOTAL SALES

# total_sales = df["Price (INR)"].sum()
# print("Total Sales (INR): ", round(total_sales, 2))

# 2 AVERAGE RATING
# average_rating = df["Rating"].mean()
# print("Average Rating: ", round(average_rating, 2))

# 3. AVERAGE ORDER VALUE
# average_order_value = df["Price (INR)"].mean()
# print("Average Order Value (INR): ", round(average_order_value, 2))

# 4.RATING COUNT
# rating_count = df["Rating Count"].sum()
# print("rating_count:" ,round(rating_count, 2))

# 5. TOTAL ORDERS
# total_orders = df.shape[0]
# print("Total Orders: ", total_orders)

# CHART DESIGN 
# 1. MONTHLY SALES TREND

# import pandas as pd
# import matplotlib.pyplot as plt

# # 1. Read Excel file
# df = pd.read_excel(r"C:/swiggy_data.xlsx")

# # 2. Convert Order Date to datetime
# df["Order Date"] = pd.to_datetime(df["Order Date"])

# # 3. Create Year-Month column
# df["YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)

# # 4. Calculate monthly revenue
# monthly_revenue = (
#     df.groupby("YearMonth")["Price (INR)"]
#     .sum()
#     .reset_index()
# )

# # 5. Plot Monthly Revenue Trend
# plt.figure(figsize=(10, 5))
# plt.plot(monthly_revenue["YearMonth"], monthly_revenue["Price (INR)"])
# plt.xticks(rotation=45)
# plt.xlabel("Month")
# plt.ylabel("Revenue (INR)")
# plt.title("Monthly Revenue Trend")
# plt.tight_layout()
# plt.show()
# plt.savefig("monthly_revenue_trend.png", dpi=300)
# plt.show()

# DAILY SALES TREND


# import pandas as pd
# import matplotlib.pyplot as plt

# # Read Excel file
# df = pd.read_excel(r"C:/swiggy_data.xlsx")

# # Convert Order Date to datetime and extract Day Name
# df["DayName"] = pd.to_datetime(df["Order Date"]).dt.day_name()

# # Calculate day-wise total revenue (Monday → Sunday order)
# daily_revenue = (
#     df.groupby("DayName")["Price (INR)"]
#     .sum()
#     .reindex([
#         "Monday",
#         "Tuesday",
#         "Wednesday",
#         "Thursday",
#         "Friday",
#         "Saturday",
#         "Sunday"
#     ])
# )

# # -------- ORANGE / PEACH THEME CHART --------
# plt.figure(figsize=(10, 4), facecolor="#fdeee4")  # peach background

# bars = plt.bar(
#     daily_revenue.index,
#     daily_revenue.values,
#     color="#f28c28",      # orange bars
#     edgecolor="#c45a00",
#     width=0.55
# )

# plt.title("Daily Sales Trend", fontsize=14, fontweight="bold", color="#333333")

# # Clean look (remove borders)
# for spine in plt.gca().spines.values():
#     spine.set_visible(False)

# # Remove Y-axis
# plt.yticks([])
# plt.ylabel("")

# # X-axis styling
# plt.xticks(color="#555555", fontsize=10)

# # Value labels on bars
# for bar, value in zip(bars, daily_revenue.values):
#     plt.text(
#         bar.get_x() + bar.get_width() / 2,
#         value,
#         f"₹{value/1e6:.1f}M",
#         ha="center",
#         va="bottom",
#         fontsize=10,
#         fontweight="bold",
#         color="#333333"
#     )

# plt.tight_layout()

# # Save chart FIRST
# plt.savefig("daily_revenue_trend.png", dpi=300)

# # Show chart
# plt.show()


# SALES BY FOOD TYPE(VEG / NON-VEG)
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.io as pio
# pio.renderers.default = "browser"


# df = pd.read_excel(r"C:/swiggy_data.xlsx")
# # print("df loaded", df)

# non_veg_keywords = [
#     "chicken","mutton","lamb","beef","pork",
#     "fish","prawn","shrimp","crab",
#     "egg","eggs","omelette",
#     "keema","kebab","kabab","tikka","seekh",
#     "sausage","pepperoni","salami","ham","bacon",
#     "turkey","duck","quail",
#     "seafood","lobster","octopus","squid",
#     "anchovy","tuna","salmon","non veg"
# ]

# df["Food category"] = np.where(
#     df["Dish Name"]
#       .str.lower()
#       .str.contains("|".join(non_veg_keywords), na=False, regex=True),
#     "Non-Veg",
#     "Veg"
# )

# food_revenue = (
#     df.groupby("Food category")["Price (INR)"]
#     .sum()
#     .reset_index()
# )

# total_revenue = food_revenue["Price (INR)"].sum()

# fig = px.pie(
#     food_revenue,
#     names="Food category",
#     values="Price (INR)",
#     hole=0.5,
#     title="Revenue Contribution: Veg vs Non-Veg",
#     color="Food category",
#     color_discrete_map={
#         "Veg": "#2ecc71",
#         "Non-Veg": "#e74c3c"
#     }
# )

# fig.update_traces(textinfo="percent+label", pull=[0.05, 0])

# fig.update_layout(
#     height=500,
#     title_x=0.5,
#     margin=dict(t=60, b=40, l=40, r=40),
# #     annotations=[dict(
# #         text=f"₹{total_revenue/1e6:.1f}M<br>Total",
# #         x=0.5, y=0.5,
# #         font_size=14,
# #         showarrow=False
# #     )]
# # )

# # fig.write_html("veg_nonveg_revenue.html")

# # fig.show()


# # STATE-WISE SALES ANALYSIS
# import pandas as pd   
# import matplotlib.pyplot as plt
# import numpy as np

# # ===== LOAD DATA =====
# df = pd.read_excel(r"C:/swiggy_data.xlsx")

# # ===== DATA CLEANING =====

# # remove spaces
# df["State"] = df["State"].str.strip()

# # fix case (Delhi vs delhi)
# df["State"] = df["State"].str.title()

# # remove null states
# df = df.dropna(subset=["State"])

# # ===== GROUP DATA =====
# state_revenue = (
#     df.groupby("State")["Price (INR)"]
#     .sum()
#     .reset_index()
#     .sort_values(by="Price (INR)", ascending=False)
# )

# # ===== COLORFUL COLORS =====
# colors = plt.cm.tab20(np.linspace(0, 1, len(state_revenue)))

# # ===== PLOT =====
# plt.figure(figsize=(12, 6))

# bars = plt.bar(
#     state_revenue["State"],
#     state_revenue["Price (INR)"],
#     color=colors,
#     edgecolor="black"
# )

# plt.title("State-wise Sales Analysis", fontsize=14, fontweight="bold")

# # remove spines
# for spine in plt.gca().spines.values():
#     spine.set_visible(False)

# plt.yticks([])
# plt.xticks(rotation=45, fontsize=10)

# # ===== VALUE LABELS =====
# for bar, value in zip(bars, state_revenue["Price (INR)"]):
#     plt.text(
#         bar.get_x() + bar.get_width()/2,
#         value,
#         f"₹{value/1e6:.1f}M",
#         ha="center",
#         va="bottom",
#         fontsize=9,
#         fontweight="bold"
#     )

# plt.tight_layout()

# # SAVE
# plt.savefig("state_wise_sales_colorful.png", dpi=300)

# plt.show()

# Quarterly Performance Summary
# import pandas as pd

# # LOAD DATA
# df = pd.read_excel(r"C:/swiggy_data.xlsx")

# # DATE CLEANING
# df["Order_Date"] = pd.to_datetime(df["Order Date"])

# # CREATE QUARTER COLUMN
# df["Quarter"] = df["Order_Date"].dt.to_period("Q").astype(str)

# # QUARTERLY SUMMARY
# quarterly_summary = (
#     df.groupby("Quarter", as_index=False)
#       .agg(
#           Total_Sales=("Price (INR)", "sum"),
#           Avg_Rating=("Rating", "mean"),
#           Total_Orders=("Order_Date", "count")
#       )
#       .sort_values("Quarter")
# )

# # ROUNDING (for clean report)
# quarterly_summary["Total_Sales"] = quarterly_summary["Total_Sales"].round(0)
# quarterly_summary["Avg_Rating"] = quarterly_summary["Avg_Rating"].round(2)

# # SHOW RESULT
# print(quarterly_summary)

# Top 5 Cities by Sales

# import pandas as pd
# import plotly.express as px

# # LOAD DATA
# df = pd.read_excel(r"C:/swiggy_data.xlsx")

# # TOP 5 CITIES BY SALES
# top_5_cities = (
#     df.groupby("City", as_index=False)["Price (INR)"]
#       .sum()
#       .nlargest(5, "Price (INR)")
#       .sort_values("Price (INR)", ascending=True)
# )

# # COLORFUL HORIZONTAL BAR CHART
# fig = px.bar(
#     top_5_cities,
#     x="Price (INR)",
#     y="City",
#     orientation="h",
#     title="Top 5 Cities by Sales (INR)",
#     color="Price (INR)",
#     color_continuous_scale="Rainbow"
# )

# # CLEAN LOOK
# fig.update_layout(
#     template="plotly_dark",
#     title_x=0.5
# )

# fig.show()



