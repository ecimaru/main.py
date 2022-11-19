from flask import Flask, request, render_template, redirect, url_for
import sys
app = Flask(__name__)
from bank import *
from wtforms import Form, StringField, PasswordField, TextAreaField, validators

class CaForm(Form):
    c_id = StringField('고객 아이디: ', [validators.length(max=20)])
    a_num = StringField('계좌 번호: ', [validators.length(max=20)])

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        op = request.form['option']
        if op == '0':
            return redirect(url_for('ccpage'))
        elif op == '1':
            return redirect(url_for('capage'))
        elif op == '2':
            return redirect(url_for('dwpage',c_id='Nan' ,a_num='Nan'))
        elif op == '3':
            return redirect(url_for('viewpage'))

    return render_template('index.html')

@app.route("/ccpage", methods=['POST', 'GET'])
def ccpage():
    if request.method == 'POST':
        c_id = request.form['cId']
        c_name = request.form['cName']
        create_customer(c_id, c_name)

        return redirect('/')

    return render_template('ccpage.html')


@app.route("/capage", methods=['POST', 'GET'])
def capage():
    form = CaForm(request.form)
    if request.method == 'POST' and form.validate():
        c_id = form.c_id.data
        a_num = form.a_num.data
        customer = search_customer(c_id)
        customer.add_account(a_num)
        update(customer)
        return redirect('/')

    return render_template('capage.html', form=form)
@app.route("/dwpage/<c_id>/<a_num>", methods=['POST', 'GET'])
def dwpage(c_id= 'Nan', a_num='Nan'):
    form = CaForm(request.form)
    if request.method == 'POST':
        c_id = request.form['cId']          #1
        a_num = request.form['aNum']        #2
        op = request.form['option']         #3
        amount = request.form['amount']     #4
        customer = search_customer(c_id)    #5
                                            #6
        if op == '0' :      #입금
            customer.add_amount(a_num,int(amount))
        elif op == '1':     #출금
            customer.sub_amount(a_num,int(amount))
        update(customer)           #7

        # 1 , 2 계좌번호, 3 입출금 옵션, 4 입력금액 요청 폼에서 받아오기
        # 5 고객 아이디로 고객인스턴스 생성
        # 6 입출금 옵션이 입금이면 고객인스턴스에서 입금함수 실행 아니면 출금함수 실행
        # 7 데이터 업데이트
    return render_template('dwpage.html', c_id= c_id,a_num= a_num ,form=form)

@app.route("/viewpage", methods=['POST', 'GET'])
def viewpage():
    if request.method == 'POST':
        c_id = request.form['inputCId']
        customer_view, accounts_view = show_customer(c_id)

        return render_template('viewpage.html',
                               customers=customer_view,
                               accounts=accounts_view
                               )

    return render_template('viewpage.html',
                           customers=show_list(),
                           accounts=None
                           )

if __name__ == '__main__':
    app.run('0.0.0.0',9999, debug=True)