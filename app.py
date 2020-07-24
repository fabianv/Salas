from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


# initializations
app = Flask(__name__)

#conexion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sgs_2'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

#routes
  
@app.route('/')
def Index():
    return render_template('index.html')


#profesor

@app.route('/profesor')
def profesor():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sgs_profesor')
    data = cur.fetchall()
    cur.close()
    return render_template('profesor.html',contacts = data)

@app.route('/edit_profesor', methods=['POST'])
def edit_profesor():
    if request.method == 'POST':
        sp_rut = request.form['sp_rut']
        sp_nombre = request.form['sp_nombre']
        sp_paterno = request.form['sp_paterno']
        sp_materno = request.form['sp_materno']
        sp_correo = request.form['sp_correo']
        sp_telefono = request.form['sp_telefono']
        sp_preferencia = request.form['sp_preferencia']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sgs_profesor (sp_rut, sp_nombre, sp_paterno, sp_materno, sp_correo, sp_telefono, sp_preferencia) VALUES (%s,%s,%s,%s,%s,%s,%s)", (sp_rut, sp_nombre, sp_paterno, sp_materno, sp_correo, sp_telefono, sp_preferencia))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('profesor'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_profesor(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sgs_profesor WHERE sp_rut = "{0}"'.format(id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit_profesor.html', contact = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_profesor(id):
    if request.method == 'POST':
        sp_rut = request.form['sp_rut']
        sp_nombre = request.form['sp_nombre']
        sp_paterno = request.form['sp_paterno']
        sp_materno = request.form['sp_materno']
        sp_correo = request.form['sp_correo']
        sp_telefono = request.form['sp_telefono']
        sp_preferencia = request.form['sp_preferencia']
        cur = mysql.connection.cursor()
        cur.execute( 'UPDATE sgs_profesor SET sp_rut = %s, sp_nombre = %s, sp_paterno = %s, sp_materno = %s, sp_correo = %s, sp_telefono = %s, sp_preferencia = %s where sp_rut = %s',(sp_rut,sp_nombre ,sp_paterno , sp_materno, sp_correo, sp_telefono, sp_preferencia,id))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('profesor'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_profesor(id):
    cur = mysql.connection.cursor()
    print(id)
    cur.execute('DELETE FROM sgs_profesor WHERE sp_rut = "{0}"'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')  
    return redirect(url_for('profesor'))

#alumno

@app.route('/alumno')
def alumno():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sgs_alumno')
    data = cur.fetchall()
    cur.close()
    return render_template('alumno.html',contacts = data)

@app.route('/edit_alumno', methods=['POST'])
def edit_alumno():
    if request.method == 'POST':
        sal_rut = request.form['sal_rut']
        sal_nombre = request.form['sal_nombre']
        sal_paterno = request.form['sal_paterno']
        sal_materno = request.form['sal_materno']
        sal_correo = request.form['sal_correo']
        sal_carrera = request.form['sal_carrera']
        sal_telefono = request.form['sal_telefono']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sgs_alumno (sal_rut, sal_nombre, sal_paterno, sal_materno, sal_correo, sal_carrera, sal_telefono) VALUES (%s,%s,%s,%s,%s,%s,%s)", (sal_rut, sal_nombre, sal_paterno, sal_materno, sal_correo, sal_carrera, sal_telefono))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('alumno'))

@app.route('/editAl/<id>', methods = ['POST', 'GET'])
def get_alumno(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sgs_alumno WHERE sal_rut = "{0}"'.format(id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit_alumno.html', contact = data[0])

@app.route('/updateAl/<id>', methods=['POST'])
def update_alumno(id):
    if request.method == 'POST':
        sal_rut = request.form['sal_rut']
        sal_nombre = request.form['sal_nombre']
        sal_paterno = request.form['sal_paterno']
        sal_materno = request.form['sal_materno']
        sal_correo = request.form['sal_correo']
        sal_carrera = request.form['sal_carrera']
        sal_telefono = request.form['sal_telefono']
        cur = mysql.connection.cursor()
        cur.execute( 'UPDATE sgs_alumno SET sal_rut = %s, sal_nombre = %s, sal_paterno = %s, sal_materno = %s, sal_correo = %s, sal_carrera = %s, sal_telefono = %s where sal_rut = %s',(sal_rut,sal_nombre ,sal_paterno , sal_materno, sal_correo, sal_carrera, sal_telefono, id))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('alumno'))

@app.route('/deleteAl/<string:id>', methods = ['POST','GET'])
def delete_alumno(id):
    cur = mysql.connection.cursor()
    print(id)
    cur.execute('DELETE FROM sgs_alumno WHERE sal_rut = "{0}"'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')  
    return redirect(url_for('alumno'))

#asignatura

@app.route('/asignatura')
def asignatura():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sgs_asignatura')
    data = cur.fetchall()
    cur.close()
    return render_template('asignatura.html',contacts = data)

@app.route('/edit_asignatura', methods=['POST'])
def edit_asignatura():
    if request.method == 'POST':
        sa_id = request.form['sa_id']
        sa_nombre = request.form['sa_nombre']
        sa_cupos = request.form['sa_cupos']
        sa_inscritos = request.form['sa_inscritos']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sgs_asignatura (sa_id, sa_nombre, sa_cupos, sa_inscritos) VALUES (%s,%s,%s,%s)", (sa_id, sa_nombre, sa_cupos, sa_inscritos))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('asignatura'))

@app.route('/editAs/<id>', methods = ['POST', 'GET'])
def get_asignatura(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sgs_asignatura WHERE sa_id = {0}'.format(id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit_asignatura.html', contact = data[0])

@app.route('/updateAs/<id>', methods=['POST'])
def update_asignatura(id):
    if request.method == 'POST':
        sa_id = request.form['sa_id']
        sa_nombre = request.form['sa_nombre']
        sa_cupos = request.form['sa_cupos']
        sa_inscritos = request.form['sa_inscritos']
        cur = mysql.connection.cursor()
        cur.execute( 'UPDATE sgs_asignatura SET sa_id = %s, sa_nombre = %s, sa_cupos = %s, sa_inscritos = %s where sa_id = %s',(sa_id, sa_nombre, sa_cupos, sa_inscritos, id))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('asignatura'))

@app.route('/deleteAs/<string:id>', methods = ['POST','GET'])
def delete_asignatura(id):
    cur = mysql.connection.cursor()
    print(id)
    cur.execute('DELETE FROM sgs_asignatura WHERE sa_id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')  
    return redirect(url_for('asignatura'))

#salas

@app.route('/salas')
def salas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sgs_sala')
    data = cur.fetchall()
    cur.close()
    return render_template('salas.html',contacts = data)

@app.route('/edit_salas', methods=['POST'])
def edit_salas():
    if request.method == 'POST':
        ss_id = request.form['ss_id']
        sad_rut = request.form['sad_rut']
        ss_tipo = request.form['ss_tipo']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sgs_sala (ss_id, sad_rut, ss_tipo) VALUES (%s,%s,%s)", (ss_id, sad_rut, ss_tipo))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('salas'))

@app.route('/editSA/<id>', methods = ['POST', 'GET'])
def get_salas(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sgs_sala WHERE ss_id = {0}'.format(id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit_salas.html', contact = data[0])

@app.route('/updateSA/<id>', methods=['POST'])
def update_salas(id):
    if request.method == 'POST':
        ss_id = request.form['ss_id']
        sad_rut = request.form['sad_rut']
        ss_tipo = request.form['ss_tipo']
        cur = mysql.connection.cursor()
        cur.execute( 'UPDATE sgs_sala SET ss_id = %s, sad_rut = %s, ss_tipo = %s where ss_id = %s',(ss_id, sad_rut, ss_tipo, id))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('salas'))

@app.route('/deleteSA/<string:id>', methods = ['POST','GET'])
def delete_salas(id):
    cur = mysql.connection.cursor()
    print(id)
    cur.execute('DELETE FROM sgs_sala WHERE ss_id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')  
    return redirect(url_for('salas'))

#dicta

@app.route('/dicta')
def dicta():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sgs_dicta')
    data = cur.fetchall()
    cur.close()
    return render_template('dicta.html',contacts = data)

@app.route('/edit_dicta', methods=['POST'])
def edit_dicta():
    if request.method == 'POST':
        ss_id = request.form['ss_id']
        sa_id = request.form['sa_id']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sgs_dicta (ss_id, sa_id) VALUES (%s,%s)", (ss_id, sa_id))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('dicta'))

@app.route('/editDI/<id>', methods = ['POST', 'GET'])
def get_dicta(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sgs_dicta WHERE ss_id = {0}'.format(id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit_dicta.html', contact = data[0])

@app.route('/updateDI/<id>', methods=['POST'])
def update_dicta(id):
    if request.method == 'POST':
        ss_id = request.form['ss_id']
        sa_id = request.form['sa_id']
        cur = mysql.connection.cursor()
        cur.execute( 'UPDATE sgs_dicta SET ss_id = %s, sa_id = %s where ss_id = %s',(ss_id, sa_id, id))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('dicta'))

@app.route('/deleteDI/<string:id>', methods = ['POST','GET'])
def delete_dicta(id):
    cur = mysql.connection.cursor()
    print(id)
    cur.execute('DELETE FROM sgs_dicta WHERE ss_id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')  
    return redirect(url_for('dicta'))

@app.route('/ocupacion')
def ocupacion():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM ocupacion')
    data = cur.fetchall()
    cur.close()
    return render_template('ocupacion.html',contacts = data)    

@app.route('/edit_ocupacion', methods=['POST','GET'])
def edit_ocupacion():
    if request.method == 'POST':
        sp_rut = request.form['sp_rut']
        cur = mysql.connection.cursor()
        cur.execute('select * from ocupacion where sp_rut = "{0}"'.format(sp_rut))
        data = cur.fetchall()
        cur.close()
        return render_template('edit_ocupacion.html',contacts = data)

@app.route('/asistencia/<id>', methods=['POST'])
def asistencia(id):
     return redirect(url_for('dicta'))
    
# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
