import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';
import axios from 'axios';
import host from "../shared/api.js";

function DealerList() {
    const [dealers, setDealers] = useState([]);

    useEffect(() => {
        axios.get(`${host}/shops`).then(res => setDealers(res.data));
    }, []);

    return (
        <div>
            <h2>Список магазинов</h2>
            <Table striped bordered>
                <thead>
                <tr>
                    <th>ID</th>
                    <th>Название</th>
                </tr>
                </thead>
                <tbody>
                {dealers.map(d => (
                    <tr key={d.id}>
                        <td>{d.id}</td>
                        <td>{d.name}</td>
                    </tr>
                ))}
                </tbody>
            </Table>
        </div>
    );
}

export default DealerList;