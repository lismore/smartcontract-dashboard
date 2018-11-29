from flask import *
import csv
import json
from etherscanScraper import *


app = Flask(__name__, static_url_path='/static/')
app._static_folder = os.path.abspath("static/")

@app.route('/')
def my_form():
    return render_template("index.html") # this should be the name of your html file

@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static', 'js'),   filename) 

@app.route('/static/<path:filename>')
def serve_static_css(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static/css', 'css'),   filename) 

@app.route('/tokenholders', methods=['GET'])
def getTokenholders():
    csvfilename = 'results.csv'
    csvfile = open(csvfilename, 'r')
    jsonfile = open('resultsjson.json', 'w')
    reader = csv.DictReader(csvfile)

    fieldnames = ('Rank', 'Address', 'Quantity', 'Percentage')

    output = []

    for each in reader:
        row = {}
        for field in fieldnames:
            row[field] = each[field]
        
        output.append(row)

    json.dump(output, jsonfile, indent=2, sort_keys=True)
    
    return json.dumps(output)

@app.route('/updatechart', methods=['GET'])
def updatechart():
    main()
    resp = jsonify(success=True)
    return resp

if __name__ == '__main__':
    app.run()