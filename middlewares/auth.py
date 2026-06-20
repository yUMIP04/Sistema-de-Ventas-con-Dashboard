import os
import jwt
from flask import request, jsonify,session
from functools import wraps
from dotenv import load_dotenv

load_dotenv()
SecretKey_JWT = os.getenv("SECRET_KEYJWT")


def token_required(f):

    @wraps(f)

    def token_verificar(*args, **kwargs):

        token = request.cookies.get('token')

        if not token and 'nombre_usuario' in session:

            return f(*args, **kwargs)
        if not token:

            return jsonify({"mensaje": "Falta el token"}), 401
        
        try:

            token_desincriptado = jwt.decode(token, SecretKey_JWT, algorithms=["HS256"])
            print(f"El usuario puede entrar con el token: {token_desincriptado}" )

        except Exception as e:

            return jsonify({"error": "El token no es valido"}), 401
        
        return f(*args, **kwargs)
    
    return token_verificar