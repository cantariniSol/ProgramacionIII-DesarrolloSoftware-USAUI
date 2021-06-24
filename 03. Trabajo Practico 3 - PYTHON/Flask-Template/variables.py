#Importamos  "render_template"
from flask import Flask, render_template

#Creamos la instancia Flask
app=Flask(__name__)

#Definimos el route
@app.route("/")

#Un segundo route con el name parámentro
@app.route('/user/<name>')
def user(name="Mirta"): #Inicializamos Mirta por defaul
    age=21 #Creamos la variable age
    my_list=[1,2,3,4] #Creamos la variable my_list
    #Retornamos la plantilla 'user.html'
    #Le pasamos el parámetro al método render template
    return render_template("user.html", name=name, age=age, list=my_list)

if __name__ =='__main__':
    app.run(debug = True, port= 8000)



