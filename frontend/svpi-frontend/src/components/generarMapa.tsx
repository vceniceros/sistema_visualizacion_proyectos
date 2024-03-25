import { useEffect, useState } from "react";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import ProyectoService from "../services/proyectosService";
import Proyecto from "../models/Proyectos";

const CENTRO_CABA: [number, number] = [-34.59941391638913, -58.389579319955196];

// Función para mapear los datos de proyectos a instancias de Proyecto
function intanciarProyecto(proyectosData: any[]): Proyecto[] {
  return proyectosData.map((proyectoData) => {
    return new Proyecto(
      proyectoData.id_proyecto,
      proyectoData.nombre,
      proyectoData.imagen,
      proyectoData.descripcion,
      proyectoData.latitud,
      proyectoData.longitud,
      proyectoData.tipo_inmueble,
      proyectoData.tipo_contrato,
      proyectoData.precio,
      proyectoData.superficie
    );
  });
}

// Función para mostrar el contenido del marcador al hacer hover
function mostrarPopUpAlhover(marker: L.Marker, proyecto: Proyecto) {
  const popupContent = `
    <div>
      <h3>${proyecto.nombre}</h3>
      <p>${proyecto.descripcion}</p>
    </div>
  `;
  marker.setPopupContent(popupContent).openPopup();
}

// Función para mostrar la información completa al hacer clic en el marcador
function mostrarCompletoAlCliquear(marker: L.Marker, proyecto: Proyecto) {
  const popupContent = `
    <div>
      <h2>${proyecto.nombre}</h2>
      <p><strong>Descripción:</strong> ${proyecto.descripcion}</p>
      <p><strong>Latitud:</strong> ${proyecto.latitud}</p>
      <p><strong>Longitud:</strong> ${proyecto.longitud}</p>
      <p><strong>Tipo de inmueble:</strong> ${proyecto.tipo_inmueble}</p>
      <p><strong>Tipo de contrato:</strong> ${proyecto.tipo_contrato}</p>
      <p><strong>Precio:</strong> ${proyecto.precio}</p>
      <p><strong>Superficie:</strong> ${proyecto.superficie}</p>
    </div>
  `;
  marker.setPopupContent(popupContent).openPopup();
}

function GenerarMapa() {
  const [proyectos, setProyectos] = useState<Proyecto[]>([]);
  const [filtroId, setFiltroId] = useState<number>(0);
  const [filtroSuperficie, setFiltroSuperficie] = useState<number>(0);
  const [filtroNombre, setFiltroNombre] = useState<string>("");

  useEffect(() => {
    const map = L.map("map").setView(CENTRO_CABA, 10);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);

    async function obtenerProyectosPorId(id: number) {
      try {
        const proyectosData = await ProyectoService.obtenerProyectosPorId(id);
        const proyectosInstancias = intanciarProyecto([proyectosData]);
        return proyectosInstancias;
      } catch (error) {
        console.error("Error al obtener proyectos por ID:", error);
        return [];
      }
    }


    async function obtenerProyectoPorNombre(nombre: string) {
      try {
        const proyectosData = await ProyectoService.obtenerProyectoPorNombre(
          nombre
        );
        const proyectosInstancias = intanciarProyecto([proyectosData]);
        return proyectosInstancias;
      } catch (error) {
        console.error("Error al obtener proyectos por nombre:", error);
        return [];
      }
    }

    async function obtenerTodosLosProyectos() {
      try {
        const proyectosData = await ProyectoService.obtenerProyectos();
        const proyectosInstancias = intanciarProyecto(proyectosData);
        return proyectosInstancias;
      } catch (error) {
        console.error("Error al obtener todos los proyectos:", error);
        return [];
      }
    }

    async function obtenerLosProyectos() {
      try {
        let proyectosInstancias = [];
        if (filtroId !== 0 && !filtroNombre) {
          proyectosInstancias = await obtenerProyectosPorId(filtroId);
        } else if (filtroNombre !== "" && !filtroId ) {
          proyectosInstancias = await obtenerProyectoPorNombre(filtroNombre);
        } else {
          proyectosInstancias = await obtenerTodosLosProyectos();
        }

        console.log("Proyectos:", proyectosInstancias);
        setProyectos(proyectosInstancias);

        proyectosInstancias.forEach((proyecto) => {
          const marker = L.marker(proyecto.darme_su_ubicacion()).addTo(map);
          marker.bindPopup(
            `<b>${proyecto.nombre}</b><br/>${proyecto.descripcion}`
          );
          marker.on("mouseover", () => mostrarPopUpAlhover(marker, proyecto));
          marker.on("click", () => mostrarCompletoAlCliquear(marker, proyecto));
        });
      } catch (error) {
        console.error("Error al obtener proyectos:", error);
      }
    }

    obtenerLosProyectos();
    return () => {
      map.remove();
    };
  }, [filtroId, filtroNombre]);

  const handleIdChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFiltroId(parseInt(e.target.value));
  };

  
  const handleNombreChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFiltroNombre(e.target.value);
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // Realizar la solicitud de proyectos al presionar el botón
  };

  return (
    <div>
      <div id="map" style={{ width: "100%", height: "400px" }}></div>
      <form onSubmit={handleSubmit} className="formulario">
        <label htmlFor="filtroId">Id</label>
        <input
          type="number"
          value={filtroId}
          onChange={handleIdChange}
          placeholder="ID"
        />
        <label htmlFor="filtroNombre">Nombre</label>
        <input
          type="text"
          value={filtroNombre}
          onChange={handleNombreChange}
          placeholder="Nombre"
        />
      </form>
    </div>
  );
}

export default GenerarMapa;
