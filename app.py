from logging import debug
from flask import Flask, jsonify, request
from flask_cors import CORS
from usuario import Usuario
from CRUD_Usuario import CRUD_Usuario
from doctor import Doctor
from CRUD_Doctor import CRUD_Doctor
from paciente import Paciente
from CRUD_Paciente import CRUD_Paciente
from enfermero import Enfermero
from CRUD_Enfermero import CRUD_Enfermero
from medicamento import Medicamento
from CRUD_Medicamento import CRUD_Medicamento

medicamentos = CRUD_Medicamento()
enfermeros = CRUD_Enfermero()
pacientes = CRUD_Paciente()
usuarios = CRUD_Usuario()
doctores = CRUD_Doctor()
app = Flask(__name__)
CORS(app)



@app.route('/usuario', methods=['PUT'])
def insertarUsuario():
    nombre = request.json["nombre"]     
    apellido = request.json["apellido"]
    fecha_nacimiento = request.json["fecha_nacimiento"]
    sexo = request.json["sexo"]
    nombre_usuario = request.json["nombre_usuario"]
    pwd = request.json["pwd"]
    telefono = request.json["telefono"]
    
    id = usuarios.insertar(nombre, apellido, fecha_nacimiento, sexo, nombre_usuario, pwd, telefono)
    return jsonify({ "mensaje": "OK",
     "usuario": {"id": id, "nombre": nombre, "apellido": apellido, "fecha_nacimiento": fecha_nacimiento, "sexo": sexo, "nombre_usuario": nombre_usuario, "pwd": pwd, "telefono": telefono}
    }), 200

@app.route('/doctor', methods=['PUT'])
def insertarDoctor():
    nombre = request.json["nombre"]
    apellido = request.json["apellido"]
    fecha_nacimiento = request.json["fecha_nacimiento"]
    sexo = request.json["sexo"]
    nombre_usuario = request.json["nombre_usuario"]
    pwd = request.json["pwd"]
    especialidad = request.json["especialidad"]
    telefono = request.json["telefono"]
    
    id = doctores.insertar(nombre, apellido, fecha_nacimiento, sexo, nombre_usuario, pwd, especialidad, telefono)
    return jsonify({ "mensaje": "OK",
     "doctor": {"id": id, "nombre": nombre, "apellido": apellido, "fecha_nacimiento": fecha_nacimiento, "sexo": sexo, "nombre_usuario": nombre_usuario, "pwd": pwd, "especialidad": especialidad, "telefono": telefono}
    }), 200

@app.route('/usuario/login', methods=['POST'])
def logIn():
    nombre_usuario = request.json["nombre_usuario"]
    pwd = request.json["pwd"]
    nombre_usuario1 = request.json["nombre_usuario"]
    pwd1 = request.json["pwd"]
    nombre_usuario2 = request.json["nombre_usuario"]
    pwd2 = request.json["pwd"]
    nombre_usuario3 = request.json["nombre_usuario"]
    pwd3 = request.json["pwd"]
    usuariopeciente = pacientes.login(nombre_usuario1, pwd1)
    usarioenfermero = enfermeros.login(nombre_usuario2, pwd2)
    usuariodoc = doctores.login(nombre_usuario3, pwd3)
    usuario = usuarios.login(nombre_usuario, pwd)
    
    if usuario:
        return jsonify({ "mensaje": "OK", "usuario": usuario}), 200
    elif usuariopeciente: 
        return jsonify({ "mensaje": "OK", "usuario": usuariopeciente}), 200
    elif usarioenfermero:
        return jsonify({ "mensaje": "OK", "usuario": usarioenfermero}), 200
    elif usuariodoc: 
        return jsonify({ "mensaje": "OK", "usuario": usuariodoc}), 200
    else:
        return jsonify({ "mensaje": "Credenciales inválidas"}), 404



    
    
    
    


@app.route('/doctor/carga-masiva', methods=['POST'])
def cargaMasiva():
    doctoresCM = request.json["doctor"]
    print (doctoresCM)
    res = doctores.cargaMasiva(doctoresCM)
    if res == "OK":
        return jsonify({ "mensaje": "OK", "data": doctores.obtener_todos()}), 200
    else:
        return jsonify({ "mensaje": "Hubo un error al realizar la carga masiva"}), 404

@app.route('/paciente/carga-masiva', methods=['POST'])
def cargaMasivaPaciente():
    pacienteCM = request.json["paciente"]
    print (pacienteCM)
    res = pacientes.cargaMasiva(pacienteCM)
    if res == "OK":
        return jsonify({ "mensaje": "OK", "data": pacientes.obtener_todos()}), 200
    else:
        return jsonify({ "mensaje": "Hubo un error al realizar la carga masiva"}), 404

@app.route('/enfermero/carga-masiva', methods=['POST'])
def cargaMasivaEnfermeros():
    enfermerosCM = request.json["enfermero"]
    print (enfermerosCM)
    res = enfermeros.cargaMasiva(enfermerosCM)
    if res == "OK":
        return jsonify({ "mensaje": "OK", "data": enfermeros.obtener_todos()}), 200
    else:
        return jsonify({ "mensaje": "Hubo un error al realizar la carga masiva"}), 404
    
@app.route('/medicamento/carga-masiva', methods=['POST'])
def cargaMasivaMedicamentos():
    medicamentosCM = request.json["medicamento"]
    print (medicamentosCM)
    res = medicamentos.cargaMasiva(medicamentosCM)
    if res == "OK":
        return jsonify({ "mensaje": "OK", "data": medicamentos.obtener_todos()}), 200
    else:
        return jsonify({ "mensaje": "Hubo un error al realizar la carga masiva"}), 404


@app.route('/doctor', methods=['GET'])
def getDoctores():
    return jsonify({"mensaje": "OK", "data": doctores.obtener_todos()}), 200

@app.route('/medicamento', methods=['GET'])
def getMedicamento():
    return jsonify({"mensaje": "OK", "data": medicamentos.obtener_todos()}), 200

@app.route('/paciente', methods=['GET'])
def getPacientes():
    return jsonify({"mensaje": "OK", "data": pacientes.obtener_todos()}), 200

@app.route('/enfermero', methods=['GET'])
def getEnfermeros():
    return jsonify({"mensaje": "OK", "data": enfermeros.obtener_todos()}), 200

# Recuperar todos los usuarios
@app.route('/usuario', methods=['GET'])
def getUsuarios():
    return jsonify({"mensaje": "OK", "data": usuarios.obtener_todos()}), 200

# Recuperar usuario por id
@app.route('/usuario/<string:id_usuario>', methods=['GET'])
def getUsuarioID(id_usuario):
    usuario = usuarios.obtener_porid(int(id_usuario))
    
    if usuario:
        return jsonify({"mensaje": "OK", "data": usuario}), 201
    else:
        return jsonify({"mensaje": "No se encontró el usuario"}), 404

@app.route('/doctor/<string:id_doctor>', methods=['DELETE'])
def getDoctorID(id_doctor):
    doctor = doctores.obtener_porid(int(id_doctor))
    
    if doctor:
        return jsonify({"mensaje": "OK", "data": doctor}), 201
    else:
        return jsonify({"mensaje": "No se encontró el usuario"}), 404

@app.route('/enfermero/<string:id_enfermero>', methods=['DELETE'])
def getEnfermeroID(id_enfermero):
    enfermero = enfermeros.obtener_porid(int(id_enfermero))
    
    if enfermero:
        return jsonify({"mensaje": "OK", "data": enfermero}), 201
    else:
        return jsonify({"mensaje": "No se encontró el usuario"}), 404

@app.route('/paciente/<string:id_paciente>', methods=['DELETE'])
def getPacienteID(id_paciente):
    paciente = pacientes.obtener_porid(int(id_paciente))
    
    if paciente:
        return jsonify({"mensaje": "OK", "data": paciente}), 201
    else:
        return jsonify({"mensaje": "No se encontró el usuario"}), 404

@app.route('/medicamento/<string:id_medicamento>', methods=['DELETE'])
def getMedicamentoID(id_medicamento):
    medicamento = medicamentos.obtener_porid(int(id_medicamento))
    
    if medicamento:
        return jsonify({"mensaje": "OK", "data": medicamento}), 201
    else:
        return jsonify({"mensaje": "No se encontró el usuario"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=4000)

