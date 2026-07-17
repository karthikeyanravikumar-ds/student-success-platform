import api from "../api/axios";

export const getMyProfile = async () => {
  const response = await api.get("/students/me");
  return response.data;
};