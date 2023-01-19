from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo

@app.route('/dojos')
def home():
    return render_template('index.html', dojos = dojo.Dojo.get_all_dojos())

@app.route('/create/dojo', methods=["POST"])
def create_dojo():
    data = {
        'name': request.form['dojo_name']
    }
    dojo.Dojo.save_dojo(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        'id': dojo_id
    } 
    return render_template('show_dojo.html', dojo = dojo.Dojo.dojo_with_ninjas(data))