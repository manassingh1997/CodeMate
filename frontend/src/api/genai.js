import { API } from "./axios";

export const getRecommendations = async () => {
  const res = await API.get("/genai/recommendations/");
  return res.data;
};
