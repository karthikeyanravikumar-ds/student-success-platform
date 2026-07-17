import api from "../api/axios";

export async function getStudentDashboard() {
  const response = await api.get("/dashboard/student");
  return response.data;
}