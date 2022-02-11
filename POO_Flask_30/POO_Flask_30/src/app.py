from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

conexion = MySQL(app)


@app.route('/reading')
def listar_reading():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM sensors.reading"
        cursor.execute(sql)
        resultado = cursor.fetchall()


        readings = []
        for file in resultado:
            reading = {'idReading': file[0],
                       'idSensor': file[1],
                       'timestamp': file[2],
                       'value': file[3]}
            readings.append(reading)

        #print(clientes)
        return jsonify({"readings": readings, "message":"Everything went well!"})
    except Exception as ex:
        return jsonify({"message":"Something went bad!"})

@app.route('/reading/<idreading>', methods=['GET'])
def ler_reading_especifico(idreading):
    try:
        idreading = str(idreading)
        cursor = conexion.connection.cursor()
        sql = f""" SELECT * FROM sensors.reading WHERE idReading = {idreading} """
        cursor.execute(sql)
        resultado = cursor.fetchone()
        if resultado != None:
            reading = {'idReading': resultado[0],
                       'idSensor': resultado[1],
                       'timestamp': resultado[2],
                       'value': resultado[3]}
            return jsonify({"readings": reading, "message": "Everything went well!"})
        else:
            return jsonify({"message":"reading nao encontrado"})
    except Exception as ex:
        return jsonify({"message":"Something went bad!"})

@app.route('/reading', methods=['POST'])
def inserir_reading():
    try:
        print(request.json)
        cursor = conexion.connection.cursor()
        sql = f"""INSERT INTO sensors.reading (idReading, idSensor, timestamp, value)  
                           VALUES (
                           {request.json['idReading']},
                           {request.json['idSensor']},
                           {request.json['timestamp']},
                           {request.json['value']}) """
        print(sql)
        cursor.execute(sql)
        print(sql)
        conexion.connection.commit()  # insere na base de dados

        return jsonify({"message": "Reading Criado!"})

    except Exception as ex:
        return jsonify({"message":"Something went bad!"})


@app.route('/reading/<idreading>', methods=['DELETE'])
def apagar_reading(idreading):
    try:
        idreading = str(idreading)
        cursor = conexion.connection.cursor()
        sql = f""" DELETE FROM sensors.reading WHERE idReading = {idreading} """
        cursor.execute(sql)
        conexion.connection.commit() #confirma a ação de deletar
        return jsonify({'message': 'Reading was deleted!'})
    except Exception as ex:
        return jsonify({'message': 'Something went bad!'})

@app.route('/reading/<idreading>', methods=['PUT'])
def editar_reading(idreading):
    try:
        idreading = str(idreading)
        print(request.json)
        cursor = conexion.connection.cursor()
        sql = f""" UPDATE sensors.reading SET value = {request.json['value']} 
                   WHERE idReading = {idreading} """
        print(sql)
        cursor.execute(sql)
        print(sql)
        conexion.connection.commit()  # atualiza na base de dados

        return jsonify({"message": "Reading Editado!"})
    except Exception as ex:
        return jsonify({"message":"Something went bad!"})

def pagina_nao_encontrada(error):
    return "<h1> A Página não foi encontrada!!!... </h1>", 404

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_nao_encontrada)
    app.run()
