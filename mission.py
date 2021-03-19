from flask import Flask, request, url_for, render_template
app = Flask(__name__)


@app.route('/index/<tit>')
def index(tit):
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title=tit, 
                           username=user)
  
  
if __name__ == "__main__":
    app.run(port=8080, debug=True)
