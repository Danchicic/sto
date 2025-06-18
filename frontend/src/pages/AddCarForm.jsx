import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import host from "../shared/api.js";

function AddCarForm() {
    const [form, setForm] = useState({});
    const navigate = useNavigate();

    const handleChange = e => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = e => {
        e.preventDefault();
        console.log(form);
        axios.post(`${host}/cars/cars`, form).then(() => navigate('/cars'));
    };

    return (
        <div>
            <h2>Добавить автомобиль</h2>
            <Form onSubmit={handleSubmit}>
                {['firm', 'model', 'year', 'power', 'gearbox', 'condition', 'features', 'price', 'auto_type'].map(field => (
                    <Form.Group key={field} className="mb-3">
                        <Form.Label>{field}</Form.Label>
                        <Form.Control name={field} onChange={handleChange} />
                    </Form.Group>
                ))}
                <Button type="submit">Сохранить</Button>
            </Form>
        </div>
    );
}

export default AddCarForm;