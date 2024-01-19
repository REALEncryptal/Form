from flask import Flask, render_template, request, redirect, url_for, jsonify
import csv
import os
import csv
from flask import redirect

app = Flask(__name__)

@app.route('/form1', methods=['POST'])
def form1():
    if request.method == 'POST':
        # Get data and write to CSV
        data = request.form.to_dict()
        fieldnames = data.keys()  # Get the keys as fieldnames
        csv_exists = os.path.isfile('form1.csv')  # Check if CSV file exists

        with open('form1.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not csv_exists:
                writer.writeheader()
            else:
                # Add csv headers that don't yet exist
                existing_headers = set()
                with open('form1.csv', 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    existing_headers = set(next(reader, []))

                new_headers = [header for header in fieldnames if header not in existing_headers]
                if new_headers:
                    writer.writerow({header: header for header in new_headers})

            writer.writerow(data)

        return redirect('http://127.0.0.1:5500/thanks.html')
    
@app.route('/form2', methods=['POST'])
def form2():
        if request.method == 'POST':
            # Get data and write to CSV
            data = request.form.to_dict()
            fieldnames = data.keys()  # Get the keys as fieldnames
            csv_exists = os.path.isfile('form2.csv')  # Check if CSV file exists

            with open('form2.csv', 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                if not csv_exists:
                    writer.writeheader()
                else:
                    # Add csv headers that don't yet exist
                    existing_headers = set()
                    with open('form2.csv', 'r') as csvfile:
                        reader = csv.reader(csvfile)
                        existing_headers = set(next(reader, []))

                    new_headers = [header for header in fieldnames if header not in existing_headers]
                    if new_headers:
                        writer.writerow({header: header for header in new_headers})

                writer.writerow(data)

            return redirect('http://127.0.0.1:5500/thanks.html')
    
@app.route('/data1', methods=['GET'])
def data1():
    with open('form1.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return jsonify({'data': data})

@app.route('/data2', methods=['GET'])
def data2():
    with open('form2.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return jsonify({'data': data})
        

@app.route('/delete1', methods=['GET'])
def delete1():
    try:
        # Remove everything but headers
        with open('form1.csv', 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Get the headers
    
        with open('form1.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)  # Write the headers back to the file
    except:
        return {"message": "Error deleting file."}

    return {"message": "Deleted successfully."}

@app.route('/delete2', methods=['GET'])
def delete2():
    try:
        # Remove everything but headers
        with open('form2.csv', 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Get the headers
    
        with open('form2.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)  # Write the headers back to the file
    except:
        return {"message": "Error deleting file."}

    return {"message": "Deleted successfully."}


@app.route('/', methods=['GET'])
def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Api</title>

    <style>
        body {
            background-color: rgb(21, 30, 42);
            font-family: Arial, Helvetica, sans-serif;
            display: flex;
            justify-content: center;
        }
        h2 {color: #fff;}
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 500px;
        }
        h1 {
            color: #fff;
            text-align: center;
        }
        ul {
            list-style-type: none;
        }
        li {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }
        a {
            margin-right: 20px;
            text-decoration: none;
            color: rgb(131, 131, 255);
            transition: .1s;
        }
        a:hover {
            font-size: 18px;
            transition: .1s;
            text-shadow: rgba(203, 203, 255, 0.435) 0px 0px 10px;
        }
        p {
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Alex's Api Home</h1>
        <h2>Api Routes:</h2>
        <ul>
            <li><a href="/">This Page</a> <p>This page</p></li>
            <li><a href="/form1">/form1</a> <p>Takes post requests and writes form to csv</p></li>
            <li><a href="/form2">/form2</a> <p>Takes post requests and writes form to csv</p></li>
            <li><a href="/data1">/data1</a> <p>Returns form1 data</p></li>
            <li><a href="/data2">/data2</a> <p>Returns form2 data</p></li>
            <li><a href="/delete1">/delete1</a> <p>Deletes form1 data</p></li>
            <li><a href="/delete2">/delete2</a> <p>Deletes form2 data</p></li>
        </ul>
    </div>
</body>
</html>"""


