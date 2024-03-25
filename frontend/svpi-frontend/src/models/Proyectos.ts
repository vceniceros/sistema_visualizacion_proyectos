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
    superficie: number; // Cambiado de 'ancho' y 'largo'

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
        this.superficie = superficie; // Cambiado de 'ancho' y 'largo'
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

    devolver_informacion_basica(): { nombre: string, imagen: string } {
        /*
         PRE:
         POST: devuelve informacion basica 
         */
        const datos_basicos = {
            nombre: this.nombre,
            imagen: this.imagen,
        };
        return datos_basicos;
    }

    devolver_informacion_completa(): { id_proyecto: number, nombre: string, descripcion: string, latitud: number, longitud: number, tipo_inmueble: string, tipo_contrato: string, precio: number, superficie: number } {
        /*
         PRE:n
         POST: Devuelve la información completa.
         */
        const informacion_completa = {
            id_proyecto: this.id_proyecto,
            nombre: this.nombre,
            descripcion: this.descripcion,
            latitud: this.latitud,
            longitud: this.longitud,
            tipo_inmueble: this.tipo_inmueble,
            tipo_contrato: this.tipo_contrato,
            precio: this.precio,
            superficie: this.superficie,
        };
        return informacion_completa;
    }
}

export default Proyecto;
