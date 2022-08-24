-- 3. Write a query which prints out customers with the money they spend excluding customers without any orders

select 
  t_customer.first_name,
  t_customer.last_name,
  sum(sum) as total_money_spent
from `tiph-ricconoel.etaily.customer` t_customer
  inner join `tiph-ricconoel.etaily.order` t_order
    on t_order.fk_customer = t_customer.id
group by t_customer.first_name,t_customer.last_name
