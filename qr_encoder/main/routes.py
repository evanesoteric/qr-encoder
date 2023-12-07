from flask import render_template, request, jsonify, Blueprint
import io
from base64 import b64encode
from datetime import datetime
import qrcode
from qr_encoder.main.forms import QRForm

main = Blueprint('main', __name__)


@main.context_processor
def inject_year():
    year = datetime.now().year
    return dict(current_year=year)

@main.context_processor
def inject_year():
    app_name = "QR Encoder"
    return dict(app_name=app_name)


def process_qr(url):
    img_io = io.BytesIO()
    qr = qrcode.make(url)
    qr.save(img_io)
    img_io.seek(0)
    encoded_img_data = b64encode(img_io.getvalue())
    encoded_img_data = encoded_img_data.decode('utf-8')
    return encoded_img_data


@main.route('/', methods=['GET', 'POST'])
def index():
    form = QRForm()
    if form.validate_on_submit():
        url = form.url.data
        qr_code = process_qr(url)
        qr_code = 'data:image/png;base64,{}'.format(qr_code)
        data = {
            'url': url,
            'qr_code': qr_code
        }
        # add to database
        # ...
        return jsonify(data)
    if request.method == 'POST':
        errors = form.errors
        qr_code = '/static/images/qr-placeholder.png'
        data = {
            'errors': errors['url'],
            'qr_code': qr_code
        }
        return jsonify(data)

    return render_template('index.html', form=form)


















