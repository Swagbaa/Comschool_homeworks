from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev-secret-key'

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    course = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.Float, nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Student {self.id}: {self.name} ({self.email}) - {self.course}, შეფასება: {self.grade}>"


@app.route('/')
def index():
    students = Student.query.order_by(Student.date_added.desc()).all()
    return render_template('index.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        course = request.form.get('course', '').strip()
        grade = request.form.get('grade', '').strip()

        if not name or not email or not course:
            flash('შეავსეთ ყველა სავალდებულო ველი.', 'error')
            return redirect(url_for('add_student'))

        try:
            grade_value = float(grade) if grade else None
        except ValueError:
            flash('შეფასება უნდა იყოს რიცხვი.', 'error')
            return redirect(url_for('add_student'))

        new_student = Student(
            name=name,
            email=email,
            course=course,
            grade=grade_value
        )

        try:
            db.session.add(new_student)
            db.session.commit()
            flash(f'სტუდენტი "{name}" წარმატებით დაემატა!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'დაფიქსირდა შეცდომა: შესაძლოა ეს მეილი უკვე დარეგისტრირებულია.', 'error')
            return redirect(url_for('add_student'))

    return render_template('add.html')


@app.route('/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    flash(f'სტუდენტი "{student.name}" წაიშალა.', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)