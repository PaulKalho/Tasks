//Axios config file
import axios from "axios";

export const api = axios.create({
  baseURL: process.env.VUE_APP_BACKEND_URL,
  headers: {
    "Content-Type": "application/json",
    // Authorization: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzMjk3ODk1LCJpYXQiOjE2ODMyMTE0OTUsImp0aSI6IjgwOTUzMWQxNDk4MjRiYTliNDM3ZjBkN2FkYTA4OTFiIiwidXNlcl9pZCI6MX0.HgODr817N8nKaWHN-LBvPHYme2amZi8GYjONZiTNVx8`,
  },

  //Todo: interceptors
});
