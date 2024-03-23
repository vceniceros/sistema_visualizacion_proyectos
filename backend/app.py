from proyectos import Proyecto
from database import Database
from flask import Flask, jsonify, request

#constantes
ID_PROYECTO_INDEX = PROYECTO_INDIVIDUAL = 0
NOMBRE_INDEX = 1
IMAGEN_INDEX = 2
DESCRIPCION_INDEX = 3
UBICACION_INDEX = 4
TIPO_INMUEBLE_INDEX = 5
TIPO_CONTRATO_INDEX = 6
PRECIO_INDEX = 7
ANCHO_INDEX = 8
LARGO_INDEX = 9

app = Flask(__name__)
db = Database(usuario='root', clave='toor', bd='svpi', host='localhost', port='3306')

def generar_proyecto(proyecto):
    """
    PRE:
    POST: genera un objeto del tipo proyecto
    """
    proyecto_obj = Proyecto( 
                proyecto[ID_PROYECTO_INDEX], 
                proyecto[NOMBRE_INDEX],  
                proyecto[IMAGEN_INDEX],  
                proyecto[DESCRIPCION_INDEX],  
                proyecto[UBICACION_INDEX],  
                proyecto[TIPO_INMUEBLE_INDEX],  
                proyecto[TIPO_CONTRATO_INDEX],  
                proyecto[PRECIO_INDEX],  
                proyecto[ANCHO_INDEX],   
                proyecto[LARGO_INDEX])
    return proyecto_obj

def generar_proyecto_individual(proyecto):
        """
        PRE:el objeto se encuenta dentro de una tupla de un solo objeto
        POST: genera un objeto del tipo proyecto
        """
        proyecto_obj = Proyecto( 
            proyecto[PROYECTO_INDIVIDUAL][ID_PROYECTO_INDEX], 
            proyecto[PROYECTO_INDIVIDUAL][NOMBRE_INDEX],  
            proyecto[PROYECTO_INDIVIDUAL][IMAGEN_INDEX],  
            proyecto[PROYECTO_INDIVIDUAL][DESCRIPCION_INDEX],  
            proyecto[PROYECTO_INDIVIDUAL][UBICACION_INDEX],  
            proyecto[PROYECTO_INDIVIDUAL][TIPO_INMUEBLE_INDEX],  
            proyecto[PROYECTO_INDIVIDUAL][TIPO_CONTRATO_INDEX],  
            proyecto[PROYECTO_INDIVIDUAL][PRECIO_INDEX],  
            proyecto[PROYECTO_INDIVIDUAL][ANCHO_INDEX],   
            proyecto[PROYECTO_INDIVIDUAL][LARGO_INDEX])
        return proyecto_obj

def corroborar_integridad(proyecto):
    """
    PRE:
    POST: devuelve el proyecto en formato json o un 404 en su defecto
    """
    if proyecto:
        re_proyecto = jsonify(proyecto)
    else: 
        re_proyecto = jsonify({'mensaje': 'Proyecto no encontrado'}), 404
    return re_proyecto

def corroborar_integridad_individual(proyecto):
    """
    PRE: el objeto se encuentra en una tupla de un solo objeto
    POST: devuelve el proyecto en formato json o un 404 en su defecto
    """
    if proyecto:
        proyecto = generar_proyecto_individual(proyecto)
        re_proyecto = jsonify(proyecto.devolver_informacion_completa())
    else:
        re_proyecto = jsonify({'mensaje': 'Proyecto no encontrado'}), 404
    return re_proyecto


@app.route('/proyectos',methods=['POST'])
def crear_proyecto():
    """
    PRE: 
    POST: crea un proyecto en la base de datos
    """
    proyecto_data = request.json
    
    required_fields = ['nombre', 'imagen', 'descripcion', 'ubicacion', 'tipo_inmueble', 'tipo_contrato', 'precio', 'ancho', 'largo']
    if not all(field in proyecto_data for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos'}), 400
    
    nuevo_proyecto = Proyecto(
        None,
        nombre=proyecto_data['nombre'],
        imagen=proyecto_data['imagen'],
        descripcion=proyecto_data['descripcion'],
        ubicacion=proyecto_data['ubicacion'],
        tipo_inmueble=proyecto_data['tipo_inmueble'],
        tipo_contrato=proyecto_data['tipo_contrato'],
        precio=proyecto_data['precio'],
        ancho=proyecto_data['ancho'],
        largo=proyecto_data['largo']
    )
    
    db.conectar()
    
    query_and_values = ("INSERT INTO proyectos (nombre, imagen, descripcion, ubicacion, tipo_inmueble, tipo_contrato, precio, ancho, largo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                        (nuevo_proyecto.nombre, nuevo_proyecto.imagen, nuevo_proyecto.descripcion, nuevo_proyecto.ubicacion, nuevo_proyecto.tipo_inmueble, nuevo_proyecto.tipo_contrato, nuevo_proyecto.precio, nuevo_proyecto.ancho, nuevo_proyecto.largo))
    db.execute_query_values(query_and_values)

    db.desconectar()
    
    return jsonify({'mensaje': 'Proyecto creado correctamente'}), 201

@app.route('/proyectos', methods=['GET'])
def obtener_proyectos():
    """
    PRE:
    POST: devuelve todos los proyectos
    """
    db.conectar()
    query = "SELECT * FROM proyectos"
    proyectos = db.execute_query(query)
    proyectos_dict = []
    for proyecto in proyectos:
        proyecto_obj = generar_proyecto(proyecto)
        proyectos_dict.append(proyecto_obj)
    
    db.desconectar()
    
    return jsonify([proyecto.devolver_informacion_completa() for proyecto in proyectos_dict])


@app.route('/proyectos/<int:id_proyecto>', methods=['GET'])
def obtener_proyecto_por_id(id_proyecto):
    """
    PRE: se pasa por url un id como entero
    POST: devuelve un unico poryecto por id
    """
    db.conectar()
    query = "SELECT * FROM proyectos WHERE id_proyectos = %s"
    query_and_values = (query, (id_proyecto,))
    
    proyecto = db.execute_query_values(query_and_values)
    
    db.desconectar()
    
    
    return corroborar_integridad_individual(proyecto)
    
    
@app.route('/proyectos/superficie/<int:superficie_maxima>', methods=['GET'])
def buscar_proyectos_por_superficie(superficie_maxima):
    """
    PRE: se ingresa una superficie como entero por parametros
    POST: devuelve todos los proyectos con una superficie menor o igual a la ingresada por parametros
    """
    db.conectar()
    query = "SELECT * FROM proyectos"
    proyectos = db.execute_query(query)
    db.desconectar()  
    
    proyectos_dict = []
    
    for proyecto in proyectos:
        proyecto_obj = generar_proyecto(proyecto)
        if proyecto_obj.superficie() <= superficie_maxima:
             proyectos_dict.append(proyecto_obj.devolver_informacion_completa())

    return corroborar_integridad(proyectos_dict)

@app.route('/proyectos/precio/<int:precio_maximo>', methods=['GET'])
def buscar_proyectos_por_precio(precio_maximo):
    """
    PRE: se pasa un precio maximo como entero por parametro
    POST: devuelve todos los proyectos cuyo precio sea menor o igual al precio maximo dado
    """
    db.conectar()
    query = "SELECT * FROM proyectos"
    proyectos = db.execute_query(query)
    db.desconectar()
    
    proyectos_dict = []
    for proyecto in proyectos:
        proyecto_obj = generar_proyecto(proyecto)
        if proyecto_obj.devolver_precio() <= precio_maximo:  
            proyectos_dict.append(proyecto_obj.devolver_informacion_completa())
    
    return corroborar_integridad(proyectos_dict)

@app.route('/proyectos/nombre/<string:nombre>', methods=['GET'])
def buscar_proyectos_por_nombre(nombre):
    """
    PRE: recibe un nombre como string por parametros
    POST: devuelve un proyecto por nombre
    """
    db.conectar()
    query = "SELECT * FROM proyectos WHERE nombre = %s"
    query_values = (query, (nombre,))
    proyecto = db.execute_query_values(query_values)
    db.desconectar()
    re_proyecto = corroborar_integridad_individual(proyecto)
        
    return re_proyecto


@app.route('/proyectos/tipo_contrato/<string:tipo_contrato>', methods=['GET'])
def buscar_proyectos_por_tipo_contrato(tipo_contrato):
    """
    PRE: recibe un tipo de contrato como string por parametros
    POST: devuelve todos los proyectos con dicho tipo de contrato
    """
    
    db.conectar()
    query = "SELECT * FROM proyectos WHERE tipo_contrato = %s"
    query_value = (query, (tipo_contrato,))
    proyectos =  db.execute_query_values(query_value)
    db.desconectar()
    
    proyectos_dict = []
    for proyecto in proyectos:
        proyecto_obj = generar_proyecto(proyecto)
        proyectos_dict.append(proyecto_obj.devolver_informacion_completa())
    
    return corroborar_integridad(proyectos_dict)


@app.route('/proyectos/tipo_inmueble/<string:tipo_inmueble>', methods=['GET'])
def buscar_proyectos_por_tipo_inmueble(tipo_inmueble):
    """
    PRE: recibe un tipo de inmueble como string por parametros
    POST: devuelve todos los proyectos con dicho tipo de inmueble
    """
    
    db.conectar()
    query = "SELECT * FROM proyectos WHERE tipo_inmueble = %s"
    query_values = (query, (tipo_inmueble,))
    proyectos = db.execute_query_values(query_values)
    db.desconectar()
    
    proyectos_dict = []
    for proyecto in proyectos:
        proyecto_obj = generar_proyecto(proyecto)
        proyectos_dict.append(proyecto_obj.devolver_informacion_completa())
    
    return corroborar_integridad(proyectos_dict)

if __name__ == "__main__":
    app.run(debug=True)
