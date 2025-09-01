import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api', // Adjust the base URL as needed
});

// User authentication
export const signup = async (userData) => {
  const response = await api.post('/users/signup', userData);
  return response.data;
};

export const login = async (credentials) => {
  const response = await api.post('/users/login', credentials);
  return response.data;
};

// Media items
export const fetchItems = async () => {
  const response = await api.get('/items');
  return response.data;
};

export const fetchItemById = async (id) => {
  const response = await api.get(`/items/${id}`);
  return response.data;
};

export const createItem = async (itemData) => {
  const response = await api.post('/items', itemData);
  return response.data;
};

export const updateItem = async (id, itemData) => {
  const response = await api.put(`/items/${id}`, itemData);
  return response.data;
};

export const deleteItem = async (id) => {
  const response = await api.delete(`/items/${id}`);
  return response.data;
};

// Recommendations
export const fetchRecommendations = async () => {
  const response = await api.get('/recommendations');
  return response.data;
};