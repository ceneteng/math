# app/views.py

from flask import render_template, flash, redirect, request, url_for
from app import app
from .forms import nameform, gameform, playform
from .mymath import getnums



@app.route('/')
def index():
  
    form = nameform()
    return render_template('login.html', form = form)

@app.route('/hello/', methods=['POST'])
def hello():
    name = request.form['name']
    return render_template('index.html', name=str.title(str(name)))

@app.route('/confgame')
def confgame():
    form = gameform()
    return render_template('gameconf.html',form=form)

@app.route('/start/', methods=['POST'])
def start():
    problems = request.form['problems']
    prbtype = request.form['prbtype']
    values = request.form['ceiling']
    return render_template('startgame.html', problems=problems,prbtype=prbtype,values=values)

@app.route('/cookie', methods=['GET', 'POST'] )
def setcook():
    problems = request.form['problems']
    prbtype = request.form['prbtype']
    ceiling = request.form['ceiling']
    redirect_to_game = redirect('/game')
    response = app.make_response(redirect_to_game)
    response.set_cookie('counter',value = '1')
    response.set_cookie('problems',value = problems)
    response.set_cookie('prbtype',value = prbtype)
    response.set_cookie('ceiling',value = ceiling)
    response.set_cookie('answer',value = '0')
    return response

@app.route('/inccookie', methods=['GET', 'POST'])
def inccook():
    redirect_to_game = redirect('/game')
    response = app.make_response(redirect_to_game) 
    cookinc = int(request.cookies.get('counter')) + 1
    response.set_cookie('counter',value = str(cookinc))
    response.set_cookie('answer', value = int(answer))
    return response

@app.route('/game', methods=['GET', 'POST'])
def game():
    
    form = playform()
    checknum = int(request.cookies.get('counter'))
    problems = int(request.cookies.get('problems'))
    ceiling = int(request.cookies.get('ceiling'))
    prevans = int(request.cookies.get('answer'))
    if checknum < problems:	
        nums = getnums(ceiling)
        return render_template('game.html',num0=nums[0],num1=nums[1],num2=nums[2],checknum=checknum,problems = problems, answer=prevans, form=form)

    else:
        return redirect(url_for('confgame'))
        
    
    
        

    
