from flask import Flask,render_template,url_for,request,redirect,make_response
from datetime import datetime
app=Flask(__name__)
users={}
statements={}
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register',methods=['GET','POST'])
def Create_Account():
    if request.method=='POST':
        username=request.form['username']
        usermail=request.form['usermail']
        userpassword=request.form['userpassword']
        pinnumber=request.form['pinNumber']
        if username not in users and username not in statements:
            users[username]={'emailid':usermail,'userpassword':userpassword,'pin':pinnumber,'amount':0 }
            statements[username]={'deposit':[],'withdraw':[]}
            return redirect(url_for('Login'))
        else:
            return 'username already exists '
    return render_template('Register.html')
@app.route('/login',methods=['GET','POST'])
def Login():
    if request.method=='POST':
         username=request.form['username']
         userpassword=request.form['userpassword']
         pinnumber=request.form['pinNumber']
         if username in users:
             if users[username]['userpassword']==userpassword:
                 if users[username]['pin']==pinnumber:
                     resp=make_response(redirect(url_for('home')))
                     resp.set_cookie('username',username)
                     return resp
                 else:
                    return 'Pin Number is wrong'
             else:
                 return 'Password Number is wrong'
         else:
             return 'user name is wrong'
    return render_template('Login.html')
@app.route('/dashboard')
def home():
    if request.cookies.get('username'):
        username=request.cookies.get('username')
        return render_template('home.html',username=username) 
    else:
        return redirect(url_for('Login'))
@app.route('/deposit',methods=['GET','POST'])
def deposit():
     if request.cookies.get('username'):
        if request.method=='POST':
            username=request.cookies.get('username')
            amount=int(request.form['amount'])
            if amount>0:
                if amount<50000:
                    if amount%100==0:
                        users[username]['amount']+=amount
                        deposittime=datetime.now()
                        depositeddata=(amount,deposittime)
                        statements[username]['deposit'].append(depositeddata)
                        return redirect(url_for('balance'))
                    else:
                        return f'{amount} the amount should be multiply of 100'
                else:
                    return f'{amount} the amount exceeded than 50K'
            else:
                return f'{amount} the amount should be greater than 0'
        return render_template('deposit.html')
     else:
         return redirect(url_for('Login'))
@app.route('/withdraw',methods=['GET','POST'])
def withdraw():
    if request.cookies.get('username'):
        if request.method=='POST':
            username=request.cookies.get('username')
            useramount=users[username]['amount']
            amount=int(request.form['amount'])
            if amount>0 and amount<50000:
                    if amount<useramount:
                        if amount%100==0:
                            users[username]['amount']-=amount
                            withdrawtime=datetime.now()
                            withdrawdata=(amount,withdrawtime)
                            statements[username]['withdraw'].append(withdrawdata)
                            return redirect(url_for('balance'))
                        else:
                            return "amount not multiple of 100"
                    else:
                        return "insuffient balance"
            else:
                return "amount entered is negative"
        return render_template('withdrawal.html')
    else:
        return redirect(url_for('Login'))
@app.route('/balance',methods=['GET'])
def balance():
    if request.cookies.get('username'):
        username=request.cookies.get('username')
        balanceAmount=users[username]['amount']
        return render_template('balance.html',Balance=balanceAmount)
    else:
        return redirect(url_for('Login'))
@app.route('/mini_statements',methods=['GET'])
def mini_statements():
    if request.cookies.get('username'):
        username=request.cookies.get('username')
        deposit_statements=statements[username]['deposit']
        print(deposit_statements)
        withdraw_statements=statements[username]['withdraw']
        print(withdraw_statements)
        return render_template('statement.html',deposit_statements=deposit_statements,withdraw_statements=withdraw_statements)
    else:
        return redirect(url_for('Login'))
@app.route('/logout')
def logout():
    if request.cookies.get('username'):
        resp=make_response(redirect(url_for('Login')))
        resp.delete_cookie('username')
        return resp
    else:
        return 'PLEASE LOGIN TO LOGOUT'
@app.route('/delete')
def delete():
     if request.cookies.get('username'):
        username=request.cookies.get('username')
        users.pop(username)
        resp=make_response(redirect(url_for('Create_Account')))
        resp.delete_cookie('username')
        return resp
     else:
         return 'PLEASE LOGIN TO DELETE YOUR ACCOUNT'
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.cookies.get('username'):
        username = request.cookies.get('username')
        if request.method == 'POST':
            new_password = request.form['new_password']
            new_pin = request.form['new_pin']

            if new_password and new_pin:
                users[username]['userpassword'] = new_password
                users[username]['pin'] = new_pin
                return 'Account details updated successfully for user!'
            else:
                return ' Both fields are required!'
        return render_template('update.html', username=username)
    else:
        return redirect(url_for('Login'))