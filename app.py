from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de données temporaire (en mémoire)
users = {}

@app.route("/")
def home():
    return "Bienvenue sur notre API DevSecOps !"

# Création d'un utilisateur
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Tous les champs sont obligatoires"}), 400

    if len(password) < 8:
        return jsonify({"message": "Le mot de passe doit contenir au moins 8 caractères"}), 400

    if username in users:
        return jsonify({"message": "Utilisateur déjà existant"}), 400

    users[username] = password

    return jsonify({"message": "Utilisateur créé avec succès"}), 201


# Connexion
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"message": "Utilisateur inconnu"}), 404

    if users[username] != password:
        return jsonify({"message": "Mot de passe incorrect"}), 401

    return jsonify({"message": "Connexion réussie"}), 200


if __name__ == "__main__":
    app.run(debug=True)