from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Users with roles and passwords
users = {
    "doctor": {"username": "doctor1", "password": "docpass"},
    "lab_technician": {"username": "labtech1", "password": "labpass"},
    "pharmacist": {"username": "pharma1", "password": "pharmapass"},
    "receptionist": {"username": "reception1", "password": "receptionpass"},
    "accountant": {"username": "account1", "password": "accountpass"}
}


@app.route('/')
def home():
    # Serve the public.html file directly from the current directory
    return send_from_directory('.', 'public.html')


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if role in users:
        user = users[role]
        if user["username"] == username and user["password"] == password:
            return jsonify({"success": True, "message": "Logged in successfully", "role": role.capitalize()})

    return jsonify({"success": False, "message": "Failed to log in"})


if __name__ == "__main__":
    app.run(debug=True)
