import React from 'react';
import { Link } from 'react-router-dom';
import { Navbar, Nav, Container } from 'react-bootstrap';

function NavigationBar() {
    return (
        <Navbar bg="dark" variant="dark" expand="lg">
            <Container>
                <Navbar.Brand as={Link} to="/">Автосалон</Navbar.Brand>
                <Nav className="me-auto">
                    <Nav.Link as={Link} to="/cars">Автомобили</Nav.Link>
                    <Nav.Link as={Link} to="/buyers">Покупатели</Nav.Link>
                    <Nav.Link as={Link} to="/dealers">Магазины</Nav.Link>
                    <Nav.Link as={Link} to="/queries">Запросы</Nav.Link>
                </Nav>
            </Container>
        </Navbar>
    );
}

export default NavigationBar;