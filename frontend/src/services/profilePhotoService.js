import api from "../api/axios";

export async function uploadProfilePhoto(studentId, file) {
  const formData = new FormData();

  formData.append("file", file);

  const response = await api.post(
    `/students/${studentId}/profile-photo`,
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
}