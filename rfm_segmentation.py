
import pandas as pd

# Load the sales data
data = pd.read_csv("sales_data.csv")

# Perform RFM Analysis
rfm = data.groupby('CustomerID').agg({
    'OrderDate': lambda x: (pd.to_datetime('2024-12-31') - pd.to_datetime(x).max()).days,
    'OrderID': 'count',
    'TotalAmount': 'sum'
})

# Rename columns for clarity
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Segment customers based on their Monetary Value
rfm['Segment'] = pd.cut(
    rfm['Monetary'],
    bins=[0, 500, 1000, 5000, float('inf')],
    labels=['Low-Value', 'Mid-Value', 'High-Value', 'VIP']
)

# Display the segmented RFM table
print("Customer Segmentation Results:\n")
print(rfm)

# Export the result to a CSV file
rfm.to_csv('rfm_segmented_customers.csv')

print("\nSegmentation results have been saved to 'rfm_segmented_customers.csv'.")
