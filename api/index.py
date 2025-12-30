from flask import Flask, render_template
import os

# Set template and static folders relative to the project root
template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def home():
    services = [
        "Land Clearing",
        "Site Preparation",
        "Earthmoving",
        "Grading (Land Leveling)",
        "Excavation for Foundations",
        "Road Base Preparation",
        "Backfilling",
        "Demolition Support",
        "Contour Shaping",
        "Material Transportation (Sand, Soil, Bricks, Aggregates)",
        "Trailer Hauling",
        "Field & Plot Leveling",
        "Light Excavation",
        "Debris Removal",
        "Sand & Soil Spreading",
        "Stone & Brick Loading Support"
    ]
    
    # Updated Gallery with proper categories
    gallery_images = [
        "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800&q=80",  # Luxury Hotel
        "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800&q=80",  # Modern Villa
        "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800&q=80",  # Apartments
        "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&q=80",  # Commercial Building
        "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800&q=80",  # Site Work
        "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=800&q=80"   # Infrastructure
    ]
    
    return render_template('index.html', services=services, gallery_images=gallery_images)

# For Vercel deployment, the app object is the handler
# For local development
if __name__ == '__main__':
    app.run(debug=True)
