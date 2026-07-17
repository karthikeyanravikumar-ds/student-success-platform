import api from "../api/axios";

export async function getStudentResults(studentId) {
  const response = await api.get(`/results/student/${studentId}`);
  return response.data;
}