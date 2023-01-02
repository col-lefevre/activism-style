from flask import Flask, render_template, redirect, url_for, request, session
import sys

app = Flask(__name__)
app.secret_key='prohealth'

sys.path.insert(1, app.root_path)
import myfunc

def isQuizDone():
    return session.get('quizDone', False)

def getStyleRank():
    return session.get('styleRanks', None)

def getDefaultStyle():
    styleRank = getStyleRank()
    if styleRank == None:
      return 'edu'
    else:
        return styleRank[0]

@app.route('/')
def index():
    return render_template('index.html', style_blurbs=myfunc.getStyleBlurb())

@app.route('/quiz')
def quiz():  
    return redirect(url_for('question', qInput=1))

@app.route('/quiz/<int:qInput>', methods=['GET', 'POST'])
def question(qInput):
    if (qInput < 0) or (qInput > 13):
        return redirect(url_for('index'))
    elif qInput == 13:
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
            # Replace with error page
            return redirect(url_for('index'))
        qAnswers.append(answer)
    
    rankedStyles = myfunc.getStyleRanks(qAnswers)
    session['quizDone'] = True
    session['styleRanks'] = [x[0] for x in rankedStyles]

    return render_template('results.html', \
        style1_name=rankedStyles[0][2], style1_perc=rankedStyles[0][1], style1_img=url_for('static', filename=('images/styles/'+rankedStyles[0][0]+'.png')),\
        style2_name=rankedStyles[1][2], style2_perc=rankedStyles[1][1], style2_img=url_for('static', filename=('images/styles/'+rankedStyles[1][0]+'.png')),\
        style3_name=rankedStyles[2][2], style3_perc=rankedStyles[2][1], style3_img=url_for('static', filename=('images/styles/'+rankedStyles[2][0]+'.png')))

@app.route('/style')
@app.route('/styles')
def style():
    return redirect(url_for('styles', styleName=getDefaultStyle()))

@app.route('/style/<string:styleName>')
def styles(styleName):
    styleInfo = myfunc.getStyleInfo(styleName)
    return render_template('style.html', \
        style_intro = myfunc.getStyleIntro(styleName, isQuizDone(), getStyleRank()), \
        style_nav=myfunc.getStyleNav(styleName, isQuizDone(), getStyleRank()), \
        style_title = styleInfo['title'], \
        style_adj = styleInfo['adj'], \
        style_desc = styleInfo['desc'], \
        style_img=url_for('static', filename=('images/styles/'+styleName+'.png')),\
        style_pos=myfunc.getMapPos(styleName), \
        style_descs=myfunc.getMapDesc(styleName),\
        style_name=styleName)

@app.route('/nextsteps')
@app.route('/nextsteps/')
@app.route('/nextsteps/<string:stepType>/')
def nextstep(stepType='methods'):
    return redirect(url_for('nextsteps', stepType=stepType, styleName=getDefaultStyle()))

@app.route('/nextsteps/<string:stepType>/<string:styleName>')
def nextsteps(stepType, styleName):
    return render_template('nextsteps.html',\
        step_intro = myfunc.getNextStepsIntro(stepType=stepType, styleName=styleName),\
        step_info = myfunc.getNextSteps(stepType=stepType, styleName=styleName),\
        step_type=stepType,\
        style_name=styleName\
        )

@app.route('/data-privacy')
def privacy():
    return redirect(url_for('index'))

@app.route('/about-us')
def about():
    return redirect(url_for('index'))

