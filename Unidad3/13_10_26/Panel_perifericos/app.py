from flask import Flask

app = Flask(
    __name__,
    static_folder="static",
    static_url_path=""
) 

@app.get("/")
def inicio():
    return app.send_static_file("index.html")
        # send_static_file() es de Flask, envía archivos generados en HTML, CSS, JS, etc. desde la carpeta static

from flask import jsonify

@app.get("/api/config")
def obtener_configuracion():
    datos = {
        "titulo": "Panel de periféricos",
        "boton": "Ingresar",
        "enlace": {
            "texto": "Ver datos JSON",
            "url": "/api/config"
        },
        "imagen": {
            "src": "images/logo.png",
            "alt": "Ingeniería de Software"
        },
        "menu": ["Inicio", "Formulario", "Ayuda"]
    }
    return jsonify(datos)

if __name__ == "__main__":
    app.run(debug=True)