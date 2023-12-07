from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField
)
from wtforms.validators import (
    InputRequired,
    URL
)


class QRForm(FlaskForm):
    url = StringField('Input a URL:',
        validators=[InputRequired(), URL(
                    require_tld=True,
                    message='<h3>URL not valid!</h3><p>Be sure to prefix the appropriate protocol.<br>(HTTP:// | HTTPS:// | FTP:// | etc)</p>')],
        render_kw={"id": "url",
                   'class': 'uk-input uk-form-large uk-border-pill',
                   "placeholder": "https://example.com"})

    submit = SubmitField('Generate QR Code', render_kw={
                        'id': 'submit',
                        'class': 'uk-button uk-button-primary uk-border-pill uk-width-1-1'})

