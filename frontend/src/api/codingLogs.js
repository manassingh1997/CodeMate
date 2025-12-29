import { API } from "./axios";

export const getCodingLogs = async (page = 1) => {
    const res = await API.get(`/coding/list/?page=${page}`);
    return res.data
};

export const createCodingLog = async (problem_link) => {
    const res = await API.post("/coding/log/", {
        problem_link,
    });
    return res.data;
};

export const updateCodingLog = async (id, notes) => {
    const res = await API.patch(`/coding/update/${id}/`, {
        notes,
    });
    return res.data;
}