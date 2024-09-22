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
    school_name = os.getenv('SCHOOL_NAME')
    city = os.getenv('CITY')
    weather = get_current_weather()

    desc = weather['weather'][0]['description'].capitalize()
    temperature = f'{weather['main']['temp']:.1f}°C'
    feels_like = f'{weather['main']['feels_like']:.1f}°C'

    return render_template("index.html",
                           school_name = school_name,
                           city=city,
                           desc = desc,
                           temp=temperature,
                           feels_like=feels_like)



@app.route('/chart')
def chart():
    str_input = request.args.get('n')
    if(str_input == None or len(str_input) < 1):
        str_input = 1
    N = float(str_input)
    print(N)
    
    
    x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
    y = np.exp(N * x)

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('y = e^(Nx)')

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
    return render_template("chart.html", n=N, chart_b64=chart_b64)

# def fig_to_base64(fig):
#     img = io.BytesIO()
#     fig.savefig(img, format='png',
#                 bbox_inches='tight')
#     img.seek(0)

#     return base64.b64encode(img.getvalue())



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    #serve(app, host="0.0.0.0", port=8000)