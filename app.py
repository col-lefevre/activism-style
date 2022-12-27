from flask import Flask, render_template, redirect, url_for, request, session
import sys

app = Flask(__name__)
app.secret_key='prohealth'

sys.path.insert(1, app.root_path)
import myfunc

@app.route('/')
def index():
    return render_template('index.html')

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
        return render_template('question.html', q_num=qNum, q_desc=myfunc.getQDesc(qNum), q_label=myfunc.getQLabels(qNum), prog_bar=(qNum*100/12), s_resp=saved_resp)
    
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
    
    rankedStyles = myfunc.getStyles(qAnswers)

    return render_template('results.html', \
        style1_name=rankedStyles[0][2], style1_perc=rankedStyles[0][1], style1_img=url_for('static', filename=('images/styles/'+rankedStyles[0][0]+'.png')),\
        style2_name=rankedStyles[1][2], style2_perc=rankedStyles[1][1], style2_img=url_for('static', filename=('images/styles/'+rankedStyles[1][0]+'.png')),\
        style3_name=rankedStyles[2][2], style3_perc=rankedStyles[2][1], style3_img=url_for('static', filename=('images/styles/'+rankedStyles[2][0]+'.png')))

@app.route('/test/<string:styleName>')
def test(styleName):
    if styleName not in ['emp', 'edu', 'org', 'phi', 'pro']:
        return redirect(url_for('index'))
    return render_template('test.html', style_pos=[2], \
        style_src=url_for('static', filename=('images/styles/'+styleName+'.png')))