from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)

def store_data_in_textfile(data):
    with open('database.txt',mode='a') as database:
        mail=data['mail']
        subject=data['subject']
        message=data['message']
        database.write(f'{mail}-{subject}-{message}')
    return 'Added to database'

def store_data_in_csvfile(data):
    with open('database2.csv',mode='a',newline='') as database2:
        mail=data['mail']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(database2, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([mail, subject, message])
    return 'Added to database'


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(store_data_in_csvfile(data))
        return render_template('thankyou.html')
    else:
        return 'error'


