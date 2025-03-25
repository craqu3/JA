from flask import Flask, request, jsonify
import mysql.connector
import bcrypt
import datetime

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="jasolvex25",
        database="solvex"
    )


@app.route("/register", method="POST")
def register():
    data = request.get_json()

    email = request.form.get("email")
    password = request.form.get("password")
    email = request.form.get("email")
    email = request.form.get("email")
    

    password_criptografada = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password_criptografada))
        conn.commit()
        return jsonify({"message": "Usuário registrado com sucesso!"}), 201
    except mysql.connector.errors.IntegrityError:
        return jsonify({"error": "Usuário já existe"}), 400
    finally:
        cursor.close()
        conn.close()



@app.route("/get-user/<user_id>")
def get_user(user_id):
    if int(user_id) <= 0:
        return jsonify("Error"),404
    else:
        user_data = {
            "id": user_id,
            "nome": "Ana Lopes",
            "idade": 20,
            "email": "ana.lopes@gmail.com"
        }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    other = request.args.get("other")
    if other:
        user_data["other"] = other

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug = True)

