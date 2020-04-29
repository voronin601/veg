from app import app
from flask import render_template, flash, redirect, request, url_for, session
from app.data_base.register import proof_reg, reg
from app import SMS
import hashlib


def new_session(*arg):
    for idd, i in enumerate(arg):
        if idd%2 == 0: session[i] = arg[idd + 1]

def del_session(*arg):
    for i in arg:
        session.pop(i, None)

#начальная страница с входом / кнопкой регистрации
@app.route("/", methods = ['GET', 'POST'])
def start():
    if request.method == 'GET':
        if "user" in session:
            return redirect(url_for("vegaterian"))
        if 'num' in session:
            return render_template("enter.html", ent = session['ent'], number = session['num'], ko = session['ko'])
        else: return render_template("enter.html", ent = True, number = "+7xxxxxxxxxx", ko = False)
    else:
        if request.form['start'] == 'Come':
            new_session('num', request.form['num'], 'KOD', SMS.KOD(), 'ent', False, 'ko', False)
            SMS.enter_SMS(session['num'], "Код подтверждения: %s" %session['KOD'])
            return redirect(url_for("start"))
        elif request.form['start'] == 'Enter':
            if request.form['kod'] == session['KOD']:
                session['user'] = hashlib.md5(bytes(session['num'], 'utf-8')).hexdigest() + SMS.kript()
                if proof_reg(num = session['user']):
                    return redirect(url_for("vegaterian"))
                else: redirect(url_for("start"))

            else: 
                new_session('KOD', SMS.KOD(), 'ent', False, 'ko', True)
                SMS.enter_SMS(session['num'], "Код подтверждения: %s" %session['KOD'])
                return redirect(url_for("start"))
        else: 
            del_session('num', 'KOD', 'ko', 'ent', 'user')
            return redirect(url_for('start'))

@app.route("/vegeterian", methods = ["GET", "POST"])
def vegaterian():
    if request.method == "GET":
        if 'user' in session:
            del_session('num', 'KOD', 'ko', 'ent')
            return "Hello"
        else: return redirect(url_for('start'))


@app.route("/admin")
def admin():
    return "qwer"

@app.route("/proverka", methods = ['GET'])
def  prov():
    try:
        if 'user' in session:
            return  render_template("prov.html", Sessi_user = session['user'])
        return  render_template("prov.html", Sessi_user = session['user'])
    except: return "Пользователь не авторизовался"