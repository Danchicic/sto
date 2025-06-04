import React, {useEffect, useState} from 'react';
import {Button, Table} from "react-bootstrap";
import axios from "axios";
import host from "../shared/api.js";


const Less30Table = () => {
    const [cars, setCars] = useState([]);
    useEffect(() => {
        async function loadCars() {
            let response = await axios.get(`${host}/cars/`);
            let temp_cars = [];

            response.data.cars.forEach((car) => {
                if (car.mileage <= 30000){
                    temp_cars.push(car)
                }
            })
            console.log(temp_cars)
            setCars(temp_cars);

        }

        loadCars();
    }, []);

    const deleteCar = (id) => {
        axios.delete(`${host}/cars/${id}`).then(() => {
            setCars(cars.filter(car => car.id !== id));
        });
    };
    return (
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
                <th>Пробег</th>
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
                    <td>{car.mileage}</td>
                    <td>
                        <Button variant="danger" onClick={() => deleteCar(car.id)}>Удалить</Button>
                    </td>
                </tr>
            ))}
            </tbody>
        </Table>
    );
};

export default Less30Table;