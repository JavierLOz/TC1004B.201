from flask import Flask, request, redirect, jsonify
from flask_expects_json import expects_json 
import mysql.connector


app = Flask(__name__)

alumno_schema = {
    'type': 'object',
    'properties': {
        'nombre' : {'type' : 'string'},
        'matricula': {'type' : 'string'}
    },
    'required': ['nombre', 'matricula']
}

cuarto_schema = {
    'type': 'object',
    'properties': {
        'numMaxPersonas': {'type': 'number'},
        'dimensiones': {'type': 'string'},
        'numActualPersonas': {'type': 'number'},
        'idSalon' : {'type': 'number'}
    },
    'required': ['numMaxPersonas', 'dimensiones', 'numActualPersonas', 'idSalon']
}

parametro_schema = {
    'type': 'object',
    'properties': {
        'min': {'type': "number"},
        'max': {'type': "number"}
    },
    'required': ['min', 'max']
}

medicion_schema = {
    'type': 'object',
    'properties': {
        'value': {'type': 'number'},
        'gasType': {'type': 'string'},
        'idCuarto': {'type': 'number'},
        'idParametro': {'type': 'number'},
        'idAlumno': {'type': 'number'}
    },
    'required': ['value', 'gasType', 'idCuarto', 'idParametro', 'idAlumno']
}

salon_schema = {
    'type': 'object',
    'properties': {
        'numSalon': {'type': 'number'}  
    },
    'required': ['numSalon']
}


@app.route('/')
def index():
    return "Main"

@app.route('/agregarAlumno', methods=["GET", "POST"])
@expects_json(alumno_schema)
def agregar_alumno():
    if request.method == "GET":
        return getAlumno()

    if request.method == "POST":
        nombre = request.json["nombre"]
        matricula = request.json["matricula"]

        try:
            #Conectar a la DB
            db = mysql.connector.connect(
                              host = "us-cdbr-east-04.cleardb.com",
                              user="bf26d23eee2a45",
                              password="13abc30a",
                              database ="heroku_a623e026293c263"
                              )
            
            cursor = db.cursor(buffered = True)

            #Commit al DB
            ad_alumno = ("INSERT INTO alumno (nombre, matricula) "
                   "VALUES (%s, %s)")
            values = (nombre, matricula)
            
            #Insertar
            cursor.execute(ad_alumno, values)
            db.commit()

            cursor.close()
            db.close()

            return redirect("/")

        except Exception  as e:
            print(e)
            return redirect("/")

@app.route('/agregarCuarto', methods=["GET", "POST"])
@expects_json(cuarto_schema)
def agregar_cuarto():

    if request.method == "GET":
        return getCuarto()

    if request.method == "POST":
        numMaxPersonas = request.json["numMaxPersonas"]
        dimensiones = request.json["dimensiones"]
        numActualPersonas = request.json["numActualPersonas"]
        idSalon = request.json["idSalon"]

        try:
            #Conectar a la DB
            db = mysql.connector.connect(
                              host = "us-cdbr-east-04.cleardb.com",
                              user="bf26d23eee2a45",
                              password="13abc30a",
                              database ="heroku_a623e026293c263"
                              )
            
            cursor = db.cursor(buffered = True)

            #Commit al DB
            ad_cuarto = ("INSERT INTO cuarto (numMaxPersonas, dimensiones,"
                         "numActualPersonas, idSalon) "
                         "VALUES (%s, %s, %s, %s)")
            values = (numMaxPersonas, dimensiones, numActualPersonas, idSalon)
            
            #Insertar
            cursor.execute(ad_cuarto, values)
            db.commit()

            cursor.close()
            db.close()

            return redirect("/")

        except Exception  as e:
            print("ERROR")
            return redirect("/")

@app.route('/agregarParametro', methods=["GET", "POST"])
@expects_json(parametro_schema)
def agregar_parametro():

    if request.method == "GET":
        return getParametro()

    if request.method == "POST":
        min = request.json["min"]
        max = request.json["max"]

        try:
            #Conectar a la DB
            db = mysql.connector.connect(
                              host = "us-cdbr-east-04.cleardb.com",
                              user="bf26d23eee2a45",
                              password="13abc30a",
                              database ="heroku_a623e026293c263"
                              )
            
            cursor = db.cursor(buffered = True)

            #Commit al DB
            ad_parametro = ("INSERT INTO parametro (min, max) "
                   "VALUES (%s, %s)")
            values = (min, max)
            
            #Insertar
            cursor.execute(ad_parametro, values)
            db.commit()

            cursor.close()
            db.close()

            return redirect("/")

        except Exception  as e:
            print("ERROR")
            return redirect("/")

@app.route('/agregarMedicion', methods=["GET", "POST"])
@expects_json(medicion_schema)
def agregar_medicion():

    if request.method == "GET":
        return getMedicion()

    if request.method == "POST":
        value = request.json["value"]
        gasType = request.json["gasType"]
        idAlumno = request.json["idAlumno"]
        idCuarto = request.json["idCuarto"]
        idParametro = request.json["idParametro"]

        try:
            #Conectar a la DB
            db = mysql.connector.connect(
                              host = "us-cdbr-east-04.cleardb.com",
                              user="bf26d23eee2a45",
                              password="13abc30a",
                              database ="heroku_a623e026293c263"
                              )
            
            cursor = db.cursor(buffered = True)

            #Commit al DB
            ad_medicion = ("INSERT INTO medicion (value, gasType,"
                         "idAlumno, idCuarto, idParametro) "
                         "VALUES (%s, %s, %s, %s, %s)")
            values = (value, gasType, idAlumno, idCuarto, idParametro)
            
            #Insertar
            cursor.execute(ad_medicion, values)
            db.commit()

            cursor.close()
            db.close()

            return redirect("/")

        except Exception  as e:
            print("ERROR")
            return redirect("/")

@app.route('/agregarSalon', methods=["GET", "POST"])
@expects_json(salon_schema)
def agregar_salon(): 

    if request.method == "GET":
        getSalon()
        return("get salon")


    if request.method == "POST":
        numSalon = request.json["numSalon"]
        
        try:
            #Conectar a la DB
            db = mysql.connector.connect(
                              host = "us-cdbr-east-04.cleardb.com",
                              user="bf26d23eee2a45",
                              password="13abc30a",
                              database ="heroku_a623e026293c263"
                              )
            
            cursor = db.cursor(buffered = True)

            #Commit al DB
            ad_salon = ("INSERT INTO salon (numSalon) "
                         "VALUES (%s)")
            values = (numSalon)
            
            #Insertar
            cursor.execute(ad_salon, values)
            db.commit()

            cursor.close()
            db.close()

            return redirect("/")

        except Exception  as e:
            print(e)
            return redirect("/")


def getAlumno():
    db = mysql.connector.connect(
                              host = "us-cdbr-east-04.cleardb.com",
                              user="bf26d23eee2a45",
                              password="13abc30a",
                              database ="heroku_a623e026293c263"
                              )

    cursor = db.cursor()

    query = ("SELECT nombre, matricula FROM alumno ")

    cursor.execute(query)

    for (nombre, matricula) in cursor:
        print (nombre, matricula)

    cursor.close()
    db.close()
    
    return jsonify({"message":"succes"}) 

def getCuarto():
    db = mysql.connector.connect(
                              host = "us-cdbr-east-04.cleardb.com",
                              user="bf26d23eee2a45",
                              password="13abc30a",
                              database ="heroku_a623e026293c263"
                              )

    cursor = db.cursor()

    query = ("SELECT numMaxPersonas, dimensiones, numActualPersonas, idSalon  FROM cuarto")

    cursor.execute(query)

    for (numMaxPersonas, dimensiones, numActualPersonas, idSalon) in cursor:
        print (numMaxPersonas, dimensiones, numActualPersonas, idSalon)

    cursor.close()
    db.close()

    return jsonify({"message":"succes"})

def getParametro():
    db = mysql.connector.connect(
                              host = "us-cdbr-east-04.cleardb.com",
                              user="bf26d23eee2a45",
                              password="13abc30a",
                              database ="heroku_a623e026293c263"
                              )

    cursor = db.cursor()

    query = ("SELECT min, max FROM parametro ")

    cursor.execute(query)

    for (min, max) in cursor:
        print (min, max)

    cursor.close()
    db.close()
    
    return jsonify({"message":"succes"}) 

def getMedicion():
    db = mysql.connector.connect(
                                host = "us-cdbr-east-04.cleardb.com",
                                user="bf26d23eee2a45",
                                password="13abc30a",
                                database ="heroku_a623e026293c263"
                                )

    cursor = db.cursor()

    query = ("SELECT value, gasType, idCuarto, idParametro, idAlumno FROM medicion ")

    cursor.execute(query)

    for (value, gasType, idCuarto, idParametro, idAlumno) in cursor:
        print (value, gasType, idCuarto, idParametro, idAlumno)

    cursor.close()
    db.close()
    
    return jsonify({"message":"succes"}) 

def getSalon():
    db = mysql.connector.connect(
                              host = "us-cdbr-east-04.cleardb.com",
                              user="bf26d23eee2a45",
                              password="13abc30a",
                              database ="heroku_a623e026293c263"
                              )

    cursor = db.cursor()

    query = ("SELECT numSalon FROM salon")

    cursor.execute(query)

    for (numSalon) in cursor:
        print (numSalon)

    cursor.close()
    db.close()

    return jsonify({"message":"succes"})

    
if __name__ == "__main__":
    app.run(debug=True)


# cnx = mysql.connector.connect(
#                               host = "us-cdbr-east-04.cleardb.com",
#                               user="bf26d23eee2a45",
#                               password="13abc30a",
#                               database ="heroku_a623e026293c263"
#                               )
# cnx.close()