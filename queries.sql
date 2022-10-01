insert into home (address, num_of_rooms, num_of_bathrooms, square_feet) values
('1 fake street calgary', 1, 1, 600),
('2 fake street airdrie', 2, 1.5, 950),
('3 fake street lethbridge', 2, 2, 1000),
('4 fake street red deer', 2, 1, 850),
('5 fake street edmonton', 1, 3, 1250);

call rooms(2)

select address 
from home h
where address like ('%calgary%');

call search_city('red deer')