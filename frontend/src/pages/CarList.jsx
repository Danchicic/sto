import React, {useEffect, useState} from 'react';
import {Table, Button} from 'react-bootstrap';
import {Link} from 'react-router-dom';
import axios from 'axios';
import host from "../shared/api.js";

function CarList() {
    const [cars, setCars] = useState([]);

    useEffect(() => {
        async function loadCars() {
            let cars = await axios.get(`${host}/cars/`);
            setCars(cars.data.cars)
            // console.log(cars.data['cars']);
        }
        loadCars();
    }, []);

    const deleteCar = (id) => {
        axios.delete(`${host}/cars/${id}`).then(() => {
            setCars(cars.filter(car => car.id !== id));
        });
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
                        <td>
                            <Button variant="danger" onClick={() => deleteCar(car.id)}>Удалить</Button>
                        </td>
                    </tr>
                ))}
                </tbody>
            </Table>
        </div>
    );
}

export default CarList;