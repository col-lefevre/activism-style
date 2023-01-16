from flask import Flask, render_template, redirect, url_for, request, session
import sys

app = Flask(__name__)
app.secret_key='prohealth'

sys.path.insert(1, app.root_path)
import myfunc

def isQuizDone():
    return session.get('quizDone', False)

def getStyleRank():
    styleRanks = session.get('styleRanks', None)
    if styleRanks:
        styleRanks = [x[0] for x in styleRanks]
    return styleRanks

def getStylePercent():
    stylePerc = session.get('styleRanks', None)
    if stylePerc:
        stylePerc = [x[1] for x in stylePerc]
    return stylePerc

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():  
    return redirect(url_for('question', qInput=1))

@app.route('/quiz/<int:qInput>', methods=['GET', 'POST'])
def question(qInput):
    if qInput == 13:
        return redirect(url_for('result'))
    elif qInput == 0:
        return redirect(url_for('index'))
    
    qNum = int(qInput)

    if request.method == 'GET':
        saved_resp = int(session.get(('q' + str(qNum)), '-1'))
        return render_template('question.html', \
            q_num=qNum, \
            q_desc=myfunc.getQDesc(qNum), \
            q_label=myfunc.getQLabels(qNum), \
            prog_bar=(qNum*100/12), \
            s_resp=saved_resp)
    
    elif request.method == 'POST':
        session['q' + str(qNum)] = request.form['QUESTION']
        return redirect(url_for('question', qInput=qNum+1))

@app.route('/results')
def result():
    qAnswers = []
    for i in range(1, 13):
        answer = int(session.get('q' + str(i), -1))
        if answer == -1:
            return redirect(url_for('index'))
        qAnswers.append(answer)
    
    rankedStyles = myfunc.calcStyleRanks(qAnswers)
    session['styleRanks'] = rankedStyles
    session['quizDone'] = True

    return render_template('results.html', ranked_styles=rankedStyles)

@app.route('/style/<string:styleName>')
def styles(styleName):
    return render_template('style.html', \
        style_intro=myfunc.getStyleIntro(styleName, isQuizDone(), getStyleRank(), getStylePercent()), \
        style_nav=myfunc.getStyleNav(styleName, isQuizDone(), getStyleRank()), \
        style_info=myfunc.getStyleInfo(styleName),\
        style_pos=myfunc.getMapPos(styleName), \
        style_descs=myfunc.getMapDesc(styleName),\
        style_involved=myfunc.getInvolved(styleName),\
        style_rank=getStyleRank(),\
        quiz_status=isQuizDone(),\
        style_name=styleName)

@app.route('/style')
@app.route('/styles')
@app.route('/explore')
def explore():
    return render_template('explore.html', style_blurbs=myfunc.getStyleBlurb())

@app.route('/data')
def privacy():
    return render_template('data.html')

@app.route('/data/clear')
def dataclear():
    session.clear()
    return redirect(url_for('privacy'))
    
@app.route('/about')
def about():
    return render_template('about.html',\
        team_info=myfunc.getTeamInfo())