from cmath import log
from re import S
from flask import Flask, redirect, request,render_template

app = Flask(__name__)

# login処理です
@app.route('/', methods=['GET', 'POST'])
def form():
    # ２回目以降データが送られてきた時の処理です
    if request.method == 'POST':
        log_ID = str(request.form['id'])
        log_Pass = str(request.form['pwd'])
        print("POSTされたIDは？" + str(request.form['id']))
        print("POSTされたPASSWORDは？" + str(request.form['pwd']))
        if log_ID == 'Tiamat':
            if log_Pass == 'Tiamat0225':
                #return render_template('Success.html')
                return redirect('https://tiamat-kit.github.io/')
            else:
                print('POSTされたPASSが間違っています')
                return render_template('fail.html')
        else:
            print("POSTされたIDは登録されていないIDです")
            return render_template('fail.html')
    # １回目のデータが何も送られてこなかった時の処理です。
    else:
        return render_template('form.html')

# アプリケーションを動かすためのおまじない
if __name__ == "__main__":
    app.run(port=12345, debug=False)