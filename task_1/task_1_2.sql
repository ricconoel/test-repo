-- 2. Write a query which prints out all customer names with the number of orders they did

select 
  t_customer.first_name,
  t_customer.last_name,
  count(t_order.order_nr) as order_count
from `tiph-ricconoel.etaily.customer` t_customer
  inner join `tiph-ricconoel.etaily.order` t_order
    on t_order.fk_customer = t_customer.id
group by t_customer.first_name,t_customer.last_name
