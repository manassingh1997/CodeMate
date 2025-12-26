import { API } from "./axios";

export const getMe = async () => {
  const response = await API.get("/users/me/");
  return response.data;
};

export const updateUserProfile = async (data) => {
  const response = await API.patch("/users/me/", data);
  return response.data;
};
