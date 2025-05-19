import axios from "axios";
import host from "../shared/api.js";


function parseJwt(token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function (c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    return JSON.parse(jsonPayload);
}

export async function amILogged() {
    try {
        const user_jwt_token_payload = await axios.get(`${host}/auth/protected`, {withCredentials: true});
        const user_jwt_token = (await user_jwt_token_payload.data)['token']
        const token_payload = parseJwt(user_jwt_token);
        localStorage.setItem("role", token_payload.role);
        return true;
    } catch (error) {
        console.log(error);

        return false;
    }

}

export async function sendCode(code, phoneNumber) {
    return await axios.get(
        `${host}/auth/verify_code`,
        {
            withCredentials: true,
            params: {
                role: 'user',
                code: code,
                phone_number: phoneNumber
            }
        });
}

export async function getCode(phoneNumber) {
    return await axios.post(
        `${host}/auth/auth`, new URLSearchParams({
            phone_number: phoneNumber
        }),
        {
            withCredentials: true,
            "headers": {
                'accept': 'application/json'
            }
        }
    )
}

