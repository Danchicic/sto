import React, {useEffect, useState} from 'react';
import {BrowserRouter as Router} from 'react-router-dom';
import Navbar from './components/Navbar';
import {AuthContext} from "./context/index.js";

import AppRouter from "./components/AppRouter.jsx";
import "./App.css"
import {amILogged} from "./api/Auth.js";

function App() {
    const [isAuth, setIsAuth] = useState(false);
    useEffect(() => {
        async function fetchApi() {
            try {
                const backendAuth = await amILogged();
                setIsAuth(backendAuth);
            } catch (e) {
                switch (e.code) {
                    case 401:
                        //try to refresh token
                        break;
                }
                console.log(e);
            }
        }

        fetchApi()
    })
    return (
        <AuthContext.Provider value={{
            isAuth,
            setIsAuth,
        }}>
            <Router>
                <Navbar/>
                <AppRouter/>
            </Router>
        </AuthContext.Provider>
    );
}

export default App;