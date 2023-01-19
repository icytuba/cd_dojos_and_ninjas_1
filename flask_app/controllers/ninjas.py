from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/create/ninja')
def add_ninja():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template('create_ninja.html', dojos=dojos)

@app.route('/process/ninja', methods=["POST"])
def process_ninja():
    data={
        'dojo_id':request.form['dojo_id'],
        'fn':request.form['fname'],
        'ln':request.form['lname'],
        'age':request.form['age']
    }
    ninja.Ninja.save_ninja(data)
    return redirect('/dojos')

@app.route('/edit/<int:id>')
def edit_ninja(id):
    data ={
        'id': id
    }
    ninja_shown = ninja.Ninja.get_one_ninja(data)
    return render_template('edit_ninja.html', dojos = dojo.Dojo.get_all_dojos(), ninja= ninja_shown)

@app.route('/update/ninja/<int:id>', methods=["POST"])
def process_edit(id):
    data ={
        'id':id,
        'dojo_id':request.form['dojo_id'],
        'fn':request.form['fname'],
        'ln':request.form['lname'],
        'age':request.form['age']
    }
    ninja.Ninja.process_update(data)
    return redirect('/dojos')

@app.route('/delete/<int:id>')
def delete_ninja(id):
    data ={
        'id':id
    }
    ninja.Ninja.delete_ninja(data)
    return redirect('/dojos')