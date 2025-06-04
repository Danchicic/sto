import React from 'react';
import {Table} from 'react-bootstrap';

function HomePage() {

    return (
        <div>
            <h1>Добро пожаловать в систему продажи автомобилей</h1>
            <h3>
                Укажите ваши требования к автомобилю
            </h3>
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
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td>
                        <div className="input-group">
                            <input id="company_name" style={{marginLeft: 10}} type="text" placeholder="Company name"/>

                        </div>
                    </td>
                    <td>
                        <div className="input-group">
                            <input id="model_name" style={{marginLeft: 10}} type="text" placeholder="Model name"/>

                        </div>
                    </td>
                    <td>
                        <div className="input-group">
                            <input id="year" style={{marginLeft: 10}} type="text" placeholder="year"/>
                        </div>
                    </td>
                    <td>
                        <div className="input-group">
                            <input id="engine_power" style={{marginLeft: 10}} type="text" placeholder="Engine power"/>
                        </div>
                    </td>
                    <td>
                        <div className="input-group">
                            <input id="transmission_type" style={{marginLeft: 10}} type="text"
                                   placeholder="Transmisson type"/>
                        </div>
                    </td>
                    <td>
                        <div className="input-group">
                            <input id="auto_type" style={{marginLeft: 10}} type="text"
                                   placeholder="Auto type"/>
                        </div>
                    </td>
                    <td>
                        <div className="input-group">
                            <input id="cost" style={{marginLeft: 10}} type="text"
                                   placeholder="cost"/>
                        </div>
                    </td>

                </tr>
                </tbody>
            </Table>
        </div>
    );
}

export default HomePage;