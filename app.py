from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['GET', 'POST'])
def simulate():
    if request.method == 'POST':
        # Get user input from the form
        ball_velocity = float(request.form.get('ball_velocity', 0))
        train_velocity = float(request.form.get('train_velocity', 0))
        angle = float(request.form.get('angle', 0))
        
        # Convert angle to radians
        angle_rad = math.radians(angle)
        
        # Calculate parameters for the ball
        g = 9.81  # acceleration due to gravity
        max_height = (ball_velocity**2) * (math.sin(angle_rad)**2) / (2 * g)
        time_of_ascent = (ball_velocity * math.sin(angle_rad)) / g
        time_of_flight = (2 * ball_velocity * math.sin(angle_rad)) / g
        horizontal_range = ball_velocity * math.cos(angle_rad) * time_of_flight
        
        # Prepare data to send to the results page
        return render_template('results.html',
                               ball_velocity=ball_velocity,
                               train_velocity=train_velocity,
                               max_height=max_height,
                               time_of_ascent=time_of_ascent,
                               time_of_flight=time_of_flight,
                               horizontal_range=horizontal_range,
                               angle=angle)
    else:
        # Handle GET request for animation
        ball_velocity = float(request.args.get('ball_velocity', 0))
        train_velocity = float(request.args.get('train_velocity', 0))
        angle = float(request.args.get('angle', 0))
        
        return render_template('simulate.html',
                               ball_velocity=ball_velocity,
                               train_velocity=train_velocity,
                               angle=angle)

if __name__ == '__main__':
    app.run(debug=True)
