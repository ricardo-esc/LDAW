from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from main.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Usuario', 
                            validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Correo',
                            validators=[DataRequired(), Email()])
    nombreCompleto = StringField('Nombre Completo',validators=[DataRequired()] )
    numTelefono = StringField('Telefono',validators=[DataRequired()] )
    edad = IntegerField('Edad', validators=[DataRequired()])
    residencia = StringField('Lugar de Residencia',validators=[DataRequired()] )
    empresa = StringField('Empresa', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña', 
                            validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Registrarse')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Ya existe una cuenta con ese nombre de usuario. Intenta con otro')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Ya existe una cuenta con ese correo. Intenta con otro')

class LoginForm(FlaskForm):
    email = StringField('Correo Electronico',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember = BooleanField('Recuerdame')
    
    submit = SubmitField('Ingresar')

class UpdateAccountForm(FlaskForm):
    username = StringField('Usuario', 
                            validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Correo Electronico',
                            validators=[DataRequired(), Email()])

    picture = FileField('Actualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Actualizar')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Ya existe una cuenta con ese nombre de usuario. Intenta con otro')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Ya existe una cuenta con ese correo. Intenta con otro')

class PostForm(FlaskForm):
    title= StringField('Nombre', validators=[DataRequired()])
    content = TextAreaField('Descripcion', validators=[DataRequired()])
    submit = SubmitField('Registrar Evento')

class EventoForm(FlaskForm):
    nombre= StringField('Nombre Evento', validators=[DataRequired()])
    siglas= StringField('Siglas', validators=[DataRequired()])
    descripcion= TextAreaField('Descripcion', validators=[DataRequired()])
    duracion= StringField('Duracion', validators=[DataRequired()])
    asistentes= IntegerField('Numero Asistentes', validators=[DataRequired()])
    costo= IntegerField('Costo', validators=[DataRequired()])
    lugar= StringField('Lugar', validators=[DataRequired()])
    fecha = DateField('Fecha', validators=[DataRequired()])
    imagen = StringField('Imagen', validators=[DataRequired()])
    submit = SubmitField('Registrar Evento')