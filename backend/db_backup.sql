insert into shops(id, name)
values (1, 'German cars shop'),
       (2, 'BMW Shop'),
       (3, 'Luxury Cars Shop');

insert into car_types(id, name)
values (1, 'new'),
       (2, 'used');

insert into company_names(id, name)
values (1, 'BMW'),
       (2, 'Audi'),
       (3, 'Mercedes'),
       (4, 'Toyota'),
       (5, 'Ford'),
       (6, 'Porsche'),
       (7, 'Lexus');

insert into cars_models(id, name)
values (1, 'M5'),
       (2, 'M4'),
       (3, 'Maybach'),
       (4, 'Q5'),
       (5, 'Supra'),
       (6, 'Mustang'),
       (7, '911 Turbo'),
       (8, 'RX-300'),
       (9, 'Cayenne');

insert into transmission_types(id, name)
values (1, 'Automatic'),
       (2, 'Manual');

insert into cars(id, company_id, model_id, transmission_type_id, auto_type_id, year, engine_power, features, cost,
                 mileage, shop_id)
values (1, 1, 1, 1, 1, 2024, 650, 'New bmw from germany', 25000000, 4, 1),
       (2, 3, 3, 1, 2, 2020, 500, 'Just mercedes', 15000000, 70000, 1),
       (3, 2, 4, 2, 2, 2020, 500, 'Rally audi quattro', 7000000, 30000, 1),
       -- BMW M5
       (4, 1, 1, 1, 1, 2023, 600, 'New BMW M5 with advanced features', 30000000, 0, 2),
       (5, 1, 1, 2, 2, 2018, 560, 'Used BMW M5 manual transmission', 18000000, 30000, 2),
       (6, 1, 1, 1, 1, 2022, 600, 'Demo BMW M5 with warranty', 32000000, 500, 2),

       -- BMW M4
       (7, 1, 2, 1, 1, 2023, 510, 'New BMW M4 coupe', 28000000, 0, 2),
       (8, 1, 2, 2, 2, 2019, 450, 'Used BMW M4 manual', 16000000, 40000, 2),

       -- Mercedes Maybach
       (9, 3, 3, 1, 1, 2023, 650, 'Luxury Mercedes Maybach S650', 50000000, 0, 3),
       (10, 3, 3, 1, 2, 2020, 600, 'Used Mercedes Maybach', 35000000, 20000, 3),

       -- Audi Q5
       (11, 2, 4, 1, 1, 2023, 300, 'New Audi Q5 with quattro', 25000000, 0, 1),
       (12, 2, 4, 2, 2, 2017, 250, 'Used Audi Q5 manual', 12000000, 60000, 1),

       -- Дополнительные автомобили
       (13, 1, 1, 1, 1, 2021, 550, 'Special edition BMW M5', 27000000, 10000, 3),
       (14, 3, 3, 1, 1, 2022, 700, 'Limited edition Mercedes Maybach', 55000000, 0, 3),
       (15, 2, 4, 1, 1, 2020, 320, 'Audi Q5 hybrid', 22000000, 15000, 3),
       (16, 1, 2, 1, 1, 2023, 520, 'BMW M4 convertible', 31000000, 0, 3),
       (17, 3, 3, 1, 1, 2019, 620, 'Mercedes Maybach GLS600', 45000000, 25000, 3),
       (18, 2, 4, 1, 1, 2021, 310, 'Audi Q5 sport package', 24000000, 5000, 3);

insert into buyers(id, company_id, model_id, auto_type_id, cost, fio, latitude, longitude, year)
values (1, 1, 1, 1, 30000000, 'Данек 52 52', 52.525252, 52.525252, 2024),
       -- Покупатели BMW M5
       (2, 1, 1, 1, 30000000, 'Иванов Иван Иванович', 55.755826, 37.6173, 2024),
       (3, 1, 1, 2, 18000000, 'Петров Петр Петрович', 55.761234, 37.623456, 2023),

       -- Покупатели BMW M4
       (4, 1, 2, 1, 28000000, 'Сидоров Сидор Сидорович', 55.771234, 37.634567, 2024),
       (5, 1, 2, 2, 16000000, 'Кузнецов Кузьма Кузьмич', 55.781234, 37.645678, 2022),

       -- Покупатели Mercedes Maybach
       (6, 3, 3, 1, 50000000, 'Александров Александр Александрович', 55.791234, 37.656789, 2024),
       (7, 3, 3, 2, 35000000, 'Николаев Николай Николаевич', 55.801234, 37.667890, 2023),

       -- Покупатели Audi Q5
       (8, 2, 4, 1, 25000000, 'Михайлов Михаил Михайлович', 55.811234, 37.678901, 2024),
       (9, 2, 4, 2, 12000000, 'Дмитриев Дмитрий Дмитриевич', 55.821234, 37.689012, 2021),

       -- Дополнительные покупатели
       (10, 1, 1, 1, 27000000, 'Федоров Федор Федорович', 55.831234, 37.690123, 2024),
       (11, 3, 3, 1, 55000000, 'Андреев Андрей Андреевич', 55.841234, 37.701234, 2023),
       (12, 2, 4, 1, 22000000, 'Владимиров Владимир Владимирович', 55.851234, 37.712345, 2022),
       (13, 1, 2, 1, 31000000, 'Сергеев Сергей Сергеевич', 55.861234, 37.723456, 2024),
       (14, 3, 3, 1, 45000000, 'Павлов Павел Павлович', 55.871234, 37.734567, 2023),
       (15, 2, 4, 1, 24000000, 'Артемьев Артем Артемович', 55.881234, 37.745678, 2021);

insert into roles(id, name)
values (1, 'user'),
       (2, 'admin'),
       (3, 'shop');