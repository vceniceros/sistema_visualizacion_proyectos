import axios from "axios";
import Proyecto from "../models/Proyectos";

const API_URL = "http://127.0.0.1:5000";

const ProyectoService = {
  obtenerProyectos: async (): Promise<Proyecto[]> => {
    try {
      const response = await axios.get(`${API_URL}/proyectos`);
      return response.data as Proyecto[];
    } catch (error) {
      throw new Error("Error al obtener los proyectos");
    }
  },
  obtenerProyectosPorId: async (id: number): Promise<Proyecto[]> => {
    try {
      const response = await axios.get(`${API_URL}/proyectos/${id}`);
      return response.data as Proyecto[];
    } catch (error) {
      throw new Error("Error al obtener los proyectos");
    }
  },
  obtenerProyectoPorNombre: async (nombre: string): Promise<Proyecto[]> => {
    try {
      const response = await axios.get(`${API_URL}/proyectos/nombre/${nombre}`);
      return response.data as Proyecto[];
    } catch (error) {
      throw new Error("Error al obtener los proyectos");
    }
  },
  obtenerProyectosPorSuperficie: async (superficie: number): Promise<Proyecto[]> => {
    try {

        const response = await axios.get(`${API_URL}/proyectos/superficie/${superficie}`);
        
        return response.data as Proyecto[];
    
      } catch (error) {
        throw new Error("Error al obtener los proyectos");
      }
  },
  obtenerProyectosPorContrato: async (contrato: string): Promise<Proyecto[]> => {
    try{
        const response = await axios.get(`${API_URL}/proyectos/tipo_contrato/${contrato}`);

        return response.data as Proyecto[];
    }catch (error) {
        throw new Error("Error al obtener los proyectos");
      }
  } 
};
export default ProyectoService;
