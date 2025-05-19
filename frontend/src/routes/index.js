import Auth from "../pages/Auth.jsx";
import NotFound404 from "../pages/NotFound404.jsx";
import AddCarForm from "../pages/AddCarForm.jsx";
import HomePage from "../pages/HomePage.jsx";
import CarList from "../pages/CarList.jsx";
import BuyerList from "../pages/BuyerList.jsx";
import DealerList from "../pages/DealerList.jsx";
import QueriesPage from "../pages/QueriesPage.jsx";
import NoPermission from "../pages/NoPermission.jsx";

const privateRoutes = [
    {path: "/", component: HomePage, exact: false, roles: ["admin", "user", "shop"]},
    {path: "/cars/add", component: AddCarForm, exact: false, roles: ["admin", "shop"]},
    {path: "/cars", component: CarList, exact: false, roles: ["admin", "shop", "user"]},
    {path: "/buyers", component: BuyerList, exact: false, roles: ["admin", "shop"]},
    {path: "/buyers/add", component: BuyerList, exact: false, roles: ["admin"]},
    {path: "/dealers", component: DealerList, exact: false, roles: ["admin"]},
    {path: "/queries", component: QueriesPage, exact: false, roles: ["admin", "user", "shop"]},
]

const publicRoutes = [
    {path: "/auth/login", component: Auth, exact: false, roles: ["admin", "user", "shop"]},
    {path: "/no_permission", component: NoPermission, exact: false, roles: ["admin", "user", "shop"]},
    {path: "*", component: NotFound404, exact: false, roles: ["admin", "user", "shop"]},
]

privateRoutes.forEach(
    (route) =>
        route.public = false
)
publicRoutes.forEach(route => route.public = true);
export const userRoutes = privateRoutes.concat(publicRoutes);
