import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import CarList from './pages/CarList';
import AddCarForm from './pages/AddCarForm';
import BuyerList from './pages/BuyerList';
import AddBuyerForm from './pages/AddBuyerForm';
import DealerList from './pages/DealerList';
import QueriesPage from './pages/QueriesPage';

function App() {
    return (
        <Router>
            <Navbar />
            <div className="container mt-4">
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/cars" element={<CarList />} />
                    <Route path="/cars/add" element={<AddCarForm />} />
                    <Route path="/buyers" element={<BuyerList />} />
                    <Route path="/buyers/add" element={<AddBuyerForm />} />
                    <Route path="/dealers" element={<DealerList />} />
                    <Route path="/queries" element={<QueriesPage />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;