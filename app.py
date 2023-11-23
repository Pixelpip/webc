from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_qrcode import QRcode

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///participants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
qrcode = QRcode(app)

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    qr_code = db.Column(db.String(200), unique=True)
    canceled = db.Column(db.Boolean, default=False)
    payment = db.Column(db.Boolean, default=False)
    checked_in = db.Column(db.Boolean, default=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/event')
def event():
    return render_template('event.html')

@app.route('/participant')
def participant():
    participants = Participant.query.all()
    return render_template('participant.html', participants=participants)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        canceled = False if request.form.get('canceled') is None else True

        participant = Participant(name=name, department=department, canceled=canceled)
        db.session.add(participant)
        db.session.commit()

        return redirect(url_for('qr', participant_id=participant.id))

    return render_template('register.html')

@app.route('/qr/<int:participant_id>')
def qr(participant_id):
    participant = Participant.query.get(participant_id)
    participant.qr_code = f'http://yourwebsite.com/checkin/{participant.id}'
    db.session.commit()
    return render_template('generate_qr.html', participant=participant)

@app.route('/checkin/<int:participant_id>', methods=['GET', 'POST'])
def checkin(participant_id):
    participant = Participant.query.get(participant_id)

    if request.method == 'POST':
        participant.payment = True if request.form.get('payment') is not None else False
        participant.checked_in = True
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('checkin.html', participant=participant)

@app.route('/admin')
def admin():
    arrived_participants = Participant.query.filter_by(checked_in=True).all()
    pending_participants = Participant.query.filter_by(checked_in=False).all()
    return render_template('admin.html', arrived_participants=arrived_participants, pending_participants=pending_participants)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
