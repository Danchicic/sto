import React, { useEffect, useState } from 'react';
import { Table, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import axios from 'axios';
import host from "../shared/api.js";
function BuyerList() {
    const [buyers, setBuyers] = useState([]);

    useEffect(() => {
        axios.get(`${host}/buyers/`).then(res => setBuyers(res.data['buyers']));
    }, []);

    const deleteBuyer = (id) => {
        axios.delete(`${host}/buyers/${id}`).then(() => {
            setBuyers(buyers.filter(b => b.id !== id));
        });
    };

    return (
        <div>
            <h2>Список покупателей</h2>
            <Link to="/buyers/add" className="btn btn-success mb-3">Добавить покупателя</Link>
            <Table striped bordered>
                <thead>
                <tr>
                    <th>ФИО</th>
                    <th>Широта</th>
                    <th>Долгота</th>
                    <th>Компания</th>
                    <th>Модель</th>
                    <th>Состояние</th>
                    <th>Макс. цена</th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {buyers.map(b => (
                    <tr key={b.id}>
                        <td>{b.fio}</td>
                        <td>{b.latitude}</td>
                        <td>{b.longitude}</td>
                        <td data-company-id={b.company.id}>{b.company.name}</td>
                        <td data-model-id={b.model.id}>{b.model.name}</td>
                        <td data-auto_type-id={b.auto_type.id}>{b.auto_type.name}</td>
                        <td>{b.cost}</td>
                        <td><Button variant="danger" onClick={() => deleteBuyer(b.id)}>Удалить</Button></td>
                    </tr>
                ))}
                </tbody>
            </Table>
        </div>
    );
}

export default BuyerList;