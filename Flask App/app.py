from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Adding Data from Statistics Canada
data = {
    "Year": [2016, 2017, 2018, 2019, 2020],
    "Canada": [30239099, 30533736, 30892653, 31160188, 31454765],
    "Newfoundland and Labrador": [376679, 378543, 378277, 379254, 392426],
    "Prince Edward Island": [76476, 77187, 77594, 78153, 78712],
    "Nova Scotia": [654852, 656662, 657687, 659765, 661845],
    "New Brunswick": [462807, 463435, 466747, 467126, 467505],
    "Quebec": [7321813, 7371397, 7455725, 7496383, 7542294],
    "Ontario": [12007013, 12104237, 12191709, 12279179, 12366649],
    "Manitoba": [985123, 1005401, 1033845, 1046667, 1059487],
    "Saskatchewan": [733983, 744737, 760605, 772759, 786531],
    "Alberta": [3395021, 3472853, 3577799, 3655091, 3732390],
    "British Columbia": [4198259, 4231834, 4264838, 4297607, 4338345],
    "Yukon": [27073, 27450, 27827, 28204, 28581],
    "Northwest Territories": [None, None, None, None, None],  # Used None if no data available for the particular year
    "Nunavut": [None, None, None, None, None],  
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)
