import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from main import app, db, bcrypt
from main.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, EventoForm
from main.models import User, Post, Evento
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    events = Evento.query.all()
    return render_template('home.html', posts=posts, events=events)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, nombreCompleto=form.nombreCompleto.data, numTelefono=form.numTelefono.data, edad=form.edad.data, residencia=form.residencia.data, empresa=form.empresa.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    users = User.query.all()
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form,users=users)

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='Registrar Nuevo Evento', form=form, legend='Registrar Nuevo Evento')

@app.route('/evento/registar', methods=['GET', 'POST'])
@login_required
def new_event():
    form = EventoForm()
    if form.validate_on_submit():
        event = Evento(Nombre=form.nombre.data, Siglas=form.siglas.data, Decripcion=form.descripcion.data, Duracion=form.duracion.data, Cupo=form.asistentes.data, Costo=form.costo.data, Lugar=form.lugar.data, Fecha=form.fecha.data, imagen=form.imagen.data, empleado=current_user)
        db.session.add(event)
        db.session.commit()
        flash('¡Se ha creado el evento!', 'success')
        return redirect(url_for('home'))
    return render_template('registrar_evento.html', title='Registrar Nuevo Evento', form=form)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route('/evento/<int:evento_id>')
def evento(evento_id):
    event = Evento.query.get_or_404(evento_id)
    return render_template('evento.html', event=event)

 

@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Editar Evento', form=form, legend='Editar Evento')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/evento/<int:evento_id>/borrar", methods=['POST'])
@login_required
def borrar_evento(evento_id):
    evento = Evento.query.get_or_404(evento_id)
    if evento.empleado != current_user:
        abort(403)
    db.session.delete(evento)
    db.session.commit()
    flash('¡El evento ha sido eliminado con éxito!', 'success')
    return redirect(url_for('home'))

@app.route('/user/delete', methods=['GET', 'POST'])
@login_required
def borrar_usuario():
    User.query.filter_by(id=2).delete()
    db.session.commit()
    flash('Cuenta borrada exitosamente', 'success')
    return redirect(url_for('home'))





