# app/views.py

from flask import render_template, flash, redirect, request, url_for
from app import app
from .forms import nameform, gameform, playform
from .mymath import getnums



@app.route('/')
@app.route('/index')
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
    name = str(request.cookies.get('name'))
    if 'counter' in request.cookies:
        lastTotalProbs = int(request.cookies.get('counter'))
        lastCorrect = int(request.cookies.get('correct'))
        return render_template('gameconf.html', lastCorr = lastCorrect, lastTot = lastTotalProbs, form=form, name = name)

    else:
        return render_template('gameconfstart.html', form=form, name=name)

@app.route('/start/', methods=['POST'])
def start():
    problems = request.form['problems']
    prbtype = request.form['prbtype']
    values = request.form['ceiling']
    return render_template('startgame.html', problems=problems,prbtype=prbtype,values=values)

@app.route('/delcookie', methods=['GET', 'POST'] )
def delcook():
    redirect_to_login = redirect('/')
    response = app.make_response(redirect_to_login)
    response.set_cookie('problems',max_age=0)
    response.set_cookie('prbtype',max_age=0)
    response.set_cookie('ceiling',max_age=0)
    response.set_cookie('answer',max_age=0)
    response.set_cookie('correct',max_age=0)
    response.set_cookie('counter',max_age=0)
    response.set_cookie('name',max_age=0)
    return response

@app.route('/cookie', methods=['GET', 'POST'] )
def setcook():

    name = request.form['name']
    redirect_to_setup = redirect('/confgame')
    response = app.make_response(redirect_to_setup)
    response.set_cookie('problems',max_age=0)
    response.set_cookie('prbtype',max_age=0)
    response.set_cookie('ceiling',max_age=0)
    response.set_cookie('answer',max_age=0)
    response.set_cookie('correct',max_age=0)
    response.set_cookie('counter',max_age=0)
    response.set_cookie('name',max_age=0)
    response.set_cookie('name', value = name)
    return response

@app.route('/expcookie', methods=['GET', 'POST'])
def excook():
    problems = request.form['problems']
    prbtype = request.form['prbtype']
    ceiling = request.form['ceiling']
    redirect_to_game = redirect('/game')
    response = app.make_response(redirect_to_game)
    response.set_cookie('problems',value = problems)
    response.set_cookie('prbtype',value = prbtype)
    response.set_cookie('ceiling',value = ceiling)
    response.set_cookie('answer',value = '0')
    response.set_cookie('correct',value = '0')
    response.set_cookie('counter',value= '0')
    return response

@app.route('/inccookie', methods=['GET', 'POST'])
def inccook():
    redirect_to_game = redirect('/game')
    response = app.make_response(redirect_to_game) 
    cookinc = int(request.cookies.get('counter')) + 1
    ansinc = request.form['answer']
    totalinc = request.form['total']
    response.set_cookie('counter',value = str(cookinc))
    response.set_cookie('answer', value = str(ansinc))
    if totalinc == ansinc:
        countcor = int(request.cookies.get('correct')) + 1
        response.set_cookie('correct',value = str(countcor))

       
    return response

@app.route('/game', methods=['GET', 'POST'])
def game():
    
    form = playform()
    checknum = int(request.cookies.get('counter'))
    problems = int(request.cookies.get('problems'))
    prbtype = str(request.cookies.get('prbtype'))
    ceiling = int(request.cookies.get('ceiling'))
    answer = int(request.cookies.get('answer'))
    if checknum < problems:	
        nums = getnums(ceiling, prbtype)
        form = playform(total = nums[2])
        if prbtype == "subtraction":
            if nums[0] > nums[1]:
                msg = "Subtract $s from $s" % (nums[0], nums[1])
                return render_template('game.html', num2=nums[2],
                                        checknum=checknum, problems = problems, answer=answer,
                                         msg = msg, form=form)
            elif nums[0] < nums[1]:
                msg = "Subtract $s from $s" % (nums[1], nums[0])
                return render_template('game.html', num2=nums[2],
                                        checknum=checknum, problems = problems, answer=answer,
                                         msg = msg, form=form)
        else:
            msg = "Add $s and $s" % (nums[0], nums[1])
            return render_template('game.html',num2=nums[2],
                                    checknum=checknum,problems = problems, answer=answer, msg = textadd,
                                     form=form)

    else:
        return redirect(url_for('confgame'))
        
    
    
        

    
