from flask import Flask, render_template, flash, request, send_file
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import os
import thread
import emotion

# App config.
DEBUG = True
app = Flask(__name__)
# app.config.from_object(__name__,template_folder='./')
# app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    Src = TextField('Src:\t(lon,lat)\t', validators=[validators.required()])
    Dest = TextField('Dest:\t(lon,lat)\t', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    print form.errors
    if request.method == 'POST':
        if request.form['btn'] == 'Randomise traffic':
            # os.system("python /home/ubuntu/NewYork/map/utils/net_to_json.py")
            # flash("Random !")
            return render_template('main_map.html', form=form)
        elif request.form['btn'] == "bt1":
            emotion.annotate_image()
            return render_template('emotion.html')
        elif request.form['btn'] == "bt2":
            return render_template('hotSpot.html')
        elif request.form['btn'] == "bt3":
            return render_template('hotSpot.html')
        elif request.form['btn'] == "bt3":
            return render_template('hotSpot.html')


 
    return render_template('main_map.html', form=form)

@app.route('/return-files/')
def return_files_tut():
    try:
        return send_file('home/ubuntu/NewYork/map/tables/out.json', attachment_filename='JSON_output.json')
    except Exception as e:
        return str(e)

@app.route('/traffic_gen/')
def traffic_new():
    print ("Randomizing Traffic..")
    flash("Please wait...")
    # os.system("python home/ubuntu/NewYork/map/utils/net_to_json.py")
    flash("Done!")
 
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host= '0.0.0.0', port=80)
