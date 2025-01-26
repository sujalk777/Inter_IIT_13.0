from flask import Flask, render_template, request
from coordinate_skibidi import generate_map  # Import your function from coordinate.py

app = Flask(__name__)

@app.route('/')
def index():
    """Render the index page for inputting coordinates."""
    return render_template('index.html')

@app.route('/generate_map', methods=['POST'])
def map_view():
    """Process the input coordinates and generate the map."""
    try:
        # Retrieve latitude and longitude from the form
        target_lat = float(request.form['latitude'])
        target_lon = float(request.form['longitude'])

        # Call the generate_map function from coordinate.py
        map_object = generate_map(target_lat, target_lon)

        # If no map is generated, return an error message
        if map_object is None:
            return render_template(
                'index.html',
                error="No polygons found for the given coordinates. Please try different coordinates."
            )

        # Convert the map object to HTML
        map_html = map_object._repr_html_()

        # Render the map.html template with the map
        return render_template('map.html', map_html=map_html)

    except (ValueError, KeyError):
        # Handle invalid or missing input
        return render_template(
            'index.html',
            error="Invalid coordinates provided. Please enter valid numerical values."
        )
    except Exception as e:
        # General error handling
        return render_template(
            'index.html',
            error=f"An unexpected error occurred: {e}"
        )

if __name__ == '__main__':
    app.run(debug=True)
