-- Payment Analytics Portfolio Project
-- Synthetic dataset: transactions.csv

-- 1. Total transaction volume
SELECT
    SUM(amount) AS total_payment_volume
FROM transactions
WHERE status = 'Success';


-- 2. Total commission revenue
SELECT
    SUM(commission) AS total_commission_revenue
FROM transactions
WHERE status = 'Success';


-- 3. Transaction count by status
SELECT
    status,
    COUNT(*) AS transaction_count
FROM transactions
GROUP BY status
ORDER BY transaction_count DESC;


-- 4. Active users
SELECT
    COUNT(DISTINCT user_id) AS active_users
FROM transactions
WHERE status = 'Success';


-- 5. Average transaction amount
SELECT
    ROUND(AVG(amount), 2) AS average_transaction_amount
FROM transactions
WHERE status = 'Success';


-- 6. Analytics by category
SELECT
    category,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount,
    SUM(commission) AS total_commission,
    ROUND(AVG(amount), 2) AS average_amount
FROM transactions
WHERE status = 'Success'
GROUP BY category
ORDER BY total_amount DESC;


-- 7. Daily transaction dynamics
SELECT
    transaction_date,
    COUNT(*) AS transaction_count,
    SUM(amount) AS daily_volume,
    SUM(commission) AS daily_commission
FROM transactions
WHERE status = 'Success'
GROUP BY transaction_date
ORDER BY transaction_date;


-- 8. Top users by payment volume
SELECT
    user_id,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM transactions
WHERE status = 'Success'
GROUP BY user_id
ORDER BY total_amount DESC;


-- 9. Transaction success rate
SELECT
    ROUND(
        100.0 * SUM(CASE WHEN status = 'Success' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS success_rate_percent
FROM transactions;
