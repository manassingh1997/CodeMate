import axios from 'axios';

const API = axios.create({
    baseURL: 'http://127.0.0.1:8000',
});

export const loginUser = async (email, password) => {
    const response = await API.post("/auth/login/", {
        email, 
        password,
    });
    return response.data;
}

export const registerUser = async (email, password) => {
    const res = await API.post("/auth/register/", {
        email: email,
        password: password,
    });
    return res
};