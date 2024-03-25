import json


class Proyecto:
    def __init__(self, id_proyecto, nombre, imagen, descripcion, latitud, longitud, tipo_inmueble, tipo_contrato, precio, ancho, largo):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.imagen = imagen
        self.descripcion = descripcion
        self.latitud = latitud
        self.longitud = longitud
        self.tipo_inmueble = tipo_inmueble
        self.tipo_contrato = tipo_contrato
        self.precio = precio
        self.ancho = ancho
        self.largo = largo
        
   
    def superficie(self):
         """
         PRE:
         POST: devuelve la superficie    
         """
         return self.ancho * self.largo
      
        
    def darme_su_ubicacion(self):
        """
        PRE: 
        POST: Devuelve la ubicación de algún proyecto en forma de lista [latitud, longitud].
        """
        ubicacion = [self.latitud, self.longitud]
        return ubicacion

    def devolver_precio(self):
        """
        PRE:
        POST: Devuelve el precio
        """
        return self.precio
    
    def devolver_informacion_basica(self):
        """
        PRE:
        POST: devuelve informacion basica 
        """
        datos_basicos = {
            "nombre": self.nombre,
            "imagen": self.imagen,
            "latitud": self.latitud,
            "longitud": self.longitud
        }
        return datos_basicos
       
    
    def devolver_informacion_completa(self):
        """
        PRE:n
        POST: Devuelve la información completa.
        """
        informacion_completa = {
            "id_proyecto": self.id_proyecto,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "latitud": self.latitud,
            "longitud": self.longitud,
            "tipo_inmueble": self.tipo_inmueble,
            "tipo_contrato": self.tipo_contrato,
            "precio": self.precio,
            "superficie": self.superficie(),  
        }
        return informacion_completa


def proyectos_test():
    proyecto = Proyecto(1, "prueba", "prueba", "prueba", 0, 0, "prueba", "prueba", 100, 38, 25)
    print("la superficie es: ", proyecto.superficie())  
    print("La ubicacion es: ", proyecto.darme_su_ubicacion())  
    info_basica =   json.dumps(proyecto.devolver_informacion_basica())
    print("la info basica es: ", info_basica)
    info_avanzada = json.dumps(proyecto.devolver_informacion_completa())
    print("la info avanzada es: ", info_avanzada)
    print(proyecto.devolve_precio() == 100)


#proyectos_test()