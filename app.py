from flask import (render_template, url_for, request, redirect)

from models import (Piece, Drawn, Film, Animation, Game, db, app)

import webbrowser

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/library')
def searcher():
    pieces = Pieces.query.all()
    return render_template('library.html', pieces=pieces)

@app.route('/piece/new', methods=['GET', 'POST'])
def add_piece():
    if request.form:
        match request.form['type']:
            case '' | '':
                new_project = Project(title=request.form['title'], 
                    date=datetime.datetime.strptime(request.form['date'], "%Y-%m"), 
                    description=request.form['desc'], 
                    skills=request.form['skills'], 
                    link=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form_add.html')

@app.route('/piece/<id>')
def view_piece(id):
    piece = Piece.query.get_or_404(id)
    return render_template('detail.html', piece=piece)

@app.route('/piece/<id>/edit', methods=['GET', 'POST'])
def edit_piece():
    return render_template('form_edit.html')

@app.route('/piece/<id>/delete')
def delete_piece(id):
    piece = Piece.query.get_or_404(id)
    db.session.delete(piece)
    db.session.commit()
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404

site = "http://127.0.0.1:8000"

if __name__ == '__main__':
    webbrowser.open_new_tab(site)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')
