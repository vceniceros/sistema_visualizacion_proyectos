class Proyecto {
    id_proyecto: number;
    nombre: string;
    imagen: string;
    descripcion: string;
    latitud: number;
    longitud: number;
    tipo_inmueble: string;
    tipo_contrato: string;
    precio: number;
    superficie: number; 
    
    constructor(id_proyecto: number, nombre: string, imagen: string, descripcion: string, latitud: number, longitud: number, tipo_inmueble: string, tipo_contrato: string, precio: number, superficie: number) {
        this.id_proyecto = id_proyecto;
        this.nombre = nombre;
        this.imagen = imagen;
        this.descripcion = descripcion;
        this.latitud = latitud;
        this.longitud = longitud;
        this.tipo_inmueble = tipo_inmueble;
        this.tipo_contrato = tipo_contrato;
        this.precio = precio;
        this.superficie = superficie; 
    }

    darme_su_ubicacion(): [number, number] {
        /*
         PRE: 
         POST: Devuelve la ubicación de algún proyecto.
         */
        
        return [this.latitud, this.longitud];
    }

    devolver_precio(): number {
        /*
         PRE:
         POST: Devuelve el precio
         */
        return this.precio;
    }

    
}

export default Proyecto;
