import React, {useEffect, useState} from 'react';
import {Table, Button} from 'react-bootstrap';
import {Link} from 'react-router-dom';
import axios from 'axios';
import host from "../shared/api.js";

function CarList() {
    const [cars, setCars] = useState([]);
    const [reservedCars, setReservedCars] = useState(new Set()); // Храним ID забронированных авто
    const role = localStorage.getItem('role');

    useEffect(() => {
        async function loadCars() {
            let response = await axios.get(`${host}/cars/`);

            setCars(response.data.cars);
            response.data.cars.forEach(
                (car) => {
                    if (car.is_reserved) {
                        reservedCars.add(car.id)

                    }
                }
            )
        }

        loadCars();
    }, []);

    const deleteCar = (id) => {
        axios.delete(`${host}/cars/${id}`).then(() => {
            setCars(cars.filter(car => car.id !== id));
        });
    };

    const reserveCar = async (id) => {
        try {
            const response = await axios.patch(`${host}/cars/reserve_car/${id}`);
            if (response.status === 200) {
                // Успешно забронировано — добавляем в Set
                setReservedCars(prev => new Set(prev).add(id));
            }
        } catch (error) {
            console.error("Ошибка при бронировании", error);
        }
    };

    return (
        <div>
            <h2>Список автомобилей</h2>
            <Link to="/cars/add" className="btn btn-success mb-3">Добавить автомобиль</Link>
            <Table striped bordered>
                <thead>
                <tr>
                    <th>Фирма</th>
                    <th>Модель</th>
                    <th>Год</th>
                    <th>Мощность</th>
                    <th>Коробка</th>
                    <th>Состояние</th>
                    <th>Цена</th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {cars.map(car => (
                    <tr key={car.id}>
                        <td>{car.company.name}</td>
                        <td>{car.model.name}</td>
                        <td>{car.year}</td>
                        <td>{car.engine_power}</td>
                        <td>{car.transmission_type.name}</td>
                        <td>{car.auto_type.name}</td>
                        <td>{car.cost}</td>
                        {role === 'user' && (
                            <td>
                                <Button
                                    variant="info"
                                    onClick={() => reserveCar(car.id)}
                                    disabled={reservedCars.has(car.id)}
                                    style={{
                                        backgroundColor: reservedCars.has(car.id) ? '#6c757d' : '',
                                        borderColor: reservedCars.has(car.id) ? '#6c757d' : ''
                                    }}
                                >
                                    {reservedCars.has(car.id) ? 'Куплено' : 'Купить'}
                                </Button>
                            </td>
                        )}
                        {role === 'shop' && (
                            <td>
                                <Button variant="danger" onClick={() => deleteCar(car.id)}>Удалить</Button>
                            </td>
                        )}
                    </tr>
                ))}
                </tbody>
            </Table>
        </div>
    );
}

export default CarList;