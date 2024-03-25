import axios from "axios";
import Proyecto from "../models/Proyectos";

const API_URL = "http://127.0.0.1:5000";

const ProyectoService = {
  obtenerProyectos: async (): Promise<Proyecto[]> => {
    /**
     * PRE:
     * POST: devuelve en un json todos los proyectos
     */
    try {
      const response = await axios.get(`${API_URL}/proyectos`);
      return response.data as Proyecto[];
    } catch (error) {
      throw new Error("Error al obtener los proyectos");
    }
  },
  obtenerProyectosPorId: async (id: number): Promise<Proyecto[]> => {
    /**
     * PRE: recibe un id como numero
     * POST: retorna el proyecto que cumpla con ese id
     */
    try {
      const response = await axios.get(`${API_URL}/proyectos/${id}`);
      return response.data as Proyecto[];
    } catch (error) {
      throw new Error("Error al obtener los proyectos");
    }
  },
  obtenerProyectoPorNombre: async (nombre: string): Promise<Proyecto[]> => {
    /**
     * PRE: recibe un nombre como string
     * POST: retorna el proyecto con ese nombre
     */
    try {
      const response = await axios.get(`${API_URL}/proyectos/nombre/${nombre}`);
      return response.data as Proyecto[];
    } catch (error) {
      throw new Error("Error al obtener los proyectos");
    }
  },
  obtenerProyectosPorSuperficie: async (
    superficie: number
  ): Promise<Proyecto[]> => {
    /**
     * PRE: recibe una superficie maxima como numero
     * POST: retorna todos los proyectos cuya superficie sea menor
     */
    try {
      const response = await axios.get(
        `${API_URL}/proyectos/superficie/${superficie}`
      );

      return response.data as Proyecto[];
    } catch (error) {
      throw new Error("Error al obtener los proyectos");
    }
  },
  obtenerProyectosPorContrato: async (
    contrato: string
  ): Promise<Proyecto[]> => {
    /**
     * PRE: recibe un tipo de contrato como string
     * POST: devuelve todos los proyectos con ese tipo de contrato
     */
    try {
      const response = await axios.get(
        `${API_URL}/proyectos/tipo_contrato/${contrato}`
      );

      return response.data as Proyecto[];
    } catch (error) {
      throw new Error("Error al obtener los proyectos");
    }
  },
  obtenerProyectosPorInmueble: async (
    inmueble: string
  ): Promise<Proyecto[]> => {
    /**
     * PRE: recibe un inmueble como string
     * POST: retorna todos los proyectos que sean ese tipo de inmueble
     */
    try {
      const response = await axios.get(
        `${API_URL}/proyectos/tipo_inmueble/${inmueble}`
      );

      return response.data as Proyecto[];
    } catch (error) {
      throw new Error("Error al obtener los proyectos");
    }
  },
  obtenerProyectosPorPrecio: async (precio: number): Promise<Proyecto[]> => {
    /**
     * PRE: recibe un precio maximo como numero
     * POST: retorna los proyectos cuyo precio sea menor o igual al recibido
     */
    try {
      const response = await axios.get(`${API_URL}/proyectos/precio/${precio}`);

      return response.data as Proyecto[];
    } catch (error) {
      throw new Error("Error al obtener los proyectos");
    }
  },
};
export default ProyectoService;
