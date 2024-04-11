from flask import Flask, render_template

#Determina o nome do host
app = Flask("Ola")

#Define uma rota(uma pagina)
@app.route('/')
def ola():
    #Mostro onde esta o arquivo .html para ser mandada(isso atravez do ginja)
    return render_template('ola.html')
