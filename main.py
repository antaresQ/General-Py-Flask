from flask import Flask, render_template, request
from waitress import serve
from dotenv import load_dotenv
import os
from services.weather import get_current_weather
import base64
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys
import base64


load_dotenv()

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    
    return render_template("index.html")



@app.route('/chart')
def chart():
    str_input = request.args.get('x_value')
    if(str_input == None or len(str_input) < 1):
        str_input = 1
    x_value = float(str_input)
    print(x_value)
    
    ypoints = []
    arr_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    for val in arr_values:
        ypoints.append(np.exp(val*x_value))
        
    plt.plot(ypoints)
    #plt.show()

    #render as image file
    # filename = "static/image.png"
    # plt.savefig(filename, format='png')
    
    fig = BytesIO()
    plt.savefig(fig, format='png')

    #fig.seek(0)
    fig_png_data = base64.b64encode(fig.getvalue()).decode('utf-8')
    chart_b64 = f"data:image/png;base64,{fig_png_data}"
    plt.close()
    return render_template("chart.html", x_value=x_value, chart_b64=chart_b64)

# def fig_to_base64(fig):
#     img = io.BytesIO()
#     fig.savefig(img, format='png',
#                 bbox_inches='tight')
#     img.seek(0)

#     return base64.b64encode(img.getvalue())



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    #serve(app, host="0.0.0.0", port=8000)