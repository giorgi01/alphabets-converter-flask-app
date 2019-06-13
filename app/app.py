from flask import Flask, request, render_template
from a_converter import Text


app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def converted():
    mkhedruli = request.form['mkhedruli']
    khutsuri = request.form['khutsuri']
    asomtavruli = request.form['asomtavruli']
    if mkhedruli != '':
        text = Text(mkhedruli, 'მხედრული')
        return f'ნუსხა-ხუცური: {text.convert_to_khutsuri()}, ' \
               f' ასომთავრული: {text.convert_to_asomtavruli()}'
    elif khutsuri != '':
        text = Text(khutsuri, 'ხუცური')
        return f'მხედრული: {text.convert_to_mkhedruli()}, ' \
               f' ასომთავრული: {text.convert_to_asomtavruli()}'
    elif asomtavruli != '':
        text = Text(asomtavruli, 'ასომთავრული')
        return f'მხედრული: {text.convert_to_mkhedruli()}, ' \
               f'ნუსხა-ხუცური: {text.convert_to_khutsuri()}'


app.run(host='0.0.0.0')

