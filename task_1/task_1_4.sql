-- 4. Write a query which prints out the order nr of all orders with at least 2 items
with cte as (
select 
  t_order.order_nr,
  count(order_nr) as order_nr_count
from `tiph-ricconoel.etaily.order` t_order
  inner join `tiph-ricconoel.etaily.order_item` t_order_item
    on t_order.id = t_order_item.fk_order
group by t_order.order_nr
)

select 
* 
from cte 
where order_nr_count >= 2
