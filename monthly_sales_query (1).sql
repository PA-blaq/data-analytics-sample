
-- Monthly Sales Summary Query
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS Month,
    SUM(total_amount) AS Total_Sales,
    COUNT(DISTINCT customer_id) AS Unique_Customers
FROM 
    sales_orders
WHERE 
    order_date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY 
    Month
ORDER BY 
    Month;
