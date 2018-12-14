from flask import Flask, render_template

app=Flask(__name__)#almasena el nombre del modulo donde estamos


@app.route("/")
def index():
	return render_template("index.html")

if __name__=="__main__":
	app.run(debug=True,host="0.0.0.0")  #debung ecucha los cambios sin necesidad de reiniciar el servidor
						 #port recibe entero y cambia el puerto utilizado 
						 #host="0.0.0.0" esto abre al aplicacivo para escuchar peticiones de una red lan

# el commit empiesa aqui


#segundo commit par aver 
