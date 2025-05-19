import React, {useContext} from 'react';
import {Navigate, Route, Routes} from "react-router-dom";
import {userRoutes} from "../routes/index.js";
import {AuthContext} from "../context/index.js";

function checkRouterByAuth(route, index, isAuth, userRole) {
    if (userRole === null) {
        return <Route key={index} path={route.path} element={<Navigate to="/auth/login"/>} exact={route.exact}/>;
    }
    if (route.path.includes("permission")) {
        return <Route key={index} path={route.path} element={<route.component/>} exact={route.exact}/>;
    }
    if (route.path.includes("auth") && isAuth) {
        // if logged user want to auth twice
        return <Route key={index} path={route.path} element={<Navigate to="/"/>} exact={route.exact}/>;
    } else if (route.public || (!route.public && isAuth)) {
        //routes for logged user, public + private, exclude auth routers
        if (route.roles.includes(userRole)) {
            // routes if role in accepted roles for this route
            return <Route key={index} path={route.path} element={<route.component/>} exact={route.exact}/>;
        }
        // redirect to auth if user role doesn't match with route role
        return <Route key={index} path={route.path} element={<Navigate to="/no_permission"/>} exact={route.exact}/>;


    } else if (!route.public && !isAuth) {
        //routes for unlogged user
        return <Route key={index} path={route.path} element={<Navigate to="/auth/login"/>} exact={route.exact}/>;
    }
}

const AppRouter = () => {
    const {isAuth} = useContext(AuthContext);
    const userRole = localStorage.getItem("role");
    return (
        <div className="container mt-4">
            <Routes>
                {userRoutes.map((route, index) => (checkRouterByAuth(route, index, isAuth, userRole)))}
            </Routes>
        </div>
    );
};

export default AppRouter;