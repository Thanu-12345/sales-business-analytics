Query 1 — Total Sales
SELECT
    SUM(Sales) AS Total_Sales
FROM sales;
Query 2 — Total Profit
SELECT
    SUM(Profit) AS Total_Profit
FROM sales;
Query 3 — Total Orders
SELECT
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM sales;
Query 4 — Sales by Region
SELECT
    Region,
    SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;
Query 5 — Profit by Category
SELECT
    Category,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Category
ORDER BY Total_Profit DESC;
Query 6 — Top 10 Products
SELECT
    Product,
    SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Product
ORDER BY Total_Sales DESC
LIMIT 10;
Query 7 — Customer Segment Performance
SELECT
    Customer_Segment,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM sales
GROUP BY Customer_Segment
ORDER BY Total_Sales DESC;
Query 8 — Monthly Sales
SELECT
    DATE_FORMAT(Order_Date, '%Y-%m') AS Month,
    SUM(Sales) AS Monthly_Sales
FROM sales
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY Month;
Query 9 — Profit Margin by Category
SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND(
        (SUM(Profit) / SUM(Sales)) * 100,
        2
    ) AS Profit_Margin_Percentage
FROM sales
GROUP BY Category
ORDER BY Profit_Margin_Percentage DESC;
Query 10 — Best Performing Region
SELECT
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Region
ORDER BY Total_Profit DESC
LIMIT 1;