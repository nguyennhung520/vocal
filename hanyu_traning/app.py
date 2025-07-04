from flask import Flask, render_template, request, redirect
from extensions import db
from models import Vocal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vocal.db'
db.init_app(app)

@app.route('/')
def index():
    words = Vocal.query.all()
    return render_template('index.html', words=words)
@app.route('/add', methods=['POST'])
def add_word():
    example = request.form['example']
    pinyin = request.form['pinyin']
    mean = request.form['mean']
    new = request.form['new']
    note = request.form.get('note', '')
    
    new_word = Vocal(example=example, pinyin=pinyin, mean=mean, new=new, note=note)
    db.session.add(new_word)
    db.session.commit()
    
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)