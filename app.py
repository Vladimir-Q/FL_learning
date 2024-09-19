from flask import Flask

app = Flask(__name__)

def get_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

@app.route('/')
def main():
    """Entry point; the view for the main page"""
    cities = [(record.city_id, record.city_name) for record in data]
    return render_template('main.html', cities=cities)


@app.route('/main.png')
def main_plot():
    """The view for rendering the scatter chart"""
    img = get_main_image()
    response = send_file(img, mimetype='image/png')
    get_headers(response)
    return response

if __name__ == '__main__':
    app.run()
