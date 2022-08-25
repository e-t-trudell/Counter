from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret8675309key'

@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    else: 
        session['count']+=1
    return render_template("index.html")

# @app.route('/views', methods=['POST'])
# def views():
#     print("Got Post Info")
#     # this prints to the console in the virtual environment
#     print(request.form)
#     session['Count'] = request.form['Count']
#     session['Email'] = request.form['Email']
#     return redirect('/')

# this route needs to clear the session and redirect to the root
@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)