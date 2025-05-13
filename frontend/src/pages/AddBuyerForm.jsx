import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function AddBuyerForm() {
    const [form, setForm] = useState({});
    const navigate = useNavigate();

    const handleChange = e => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = e => {
        e.preventDefault();
        axios.post('/api/buyers', form).then(() => navigate('/buyers'));
    };

    return (
        <div>
            <h2>Добавить покупателя</h2>
            <Form onSubmit={handleSubmit}>
                {['name', 'contact', 'requirements', 'maxPrice'].map(field => (
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

export default AddBuyerForm;