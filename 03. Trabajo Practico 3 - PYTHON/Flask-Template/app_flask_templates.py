#Importamos "render_template"
from flask import Flask, render_template

#Creamos la instancia de Flask
app=Flask(__name__)

#Definimos la ruta
@app.route("/")

#Un segundo route con el nombre del parámetro
@app.route('/<nombre>')
def render(nombre=None): #Inicializamos nombre
    #Retornamos la plantilla 'Index.html'
    #Le pasamos el parámetro al método render template
    return render_template("index.html", nombre=nombre)

#Inicilizamos la aplicación
app.run()