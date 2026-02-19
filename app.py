from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
import os 

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-key')

# In-memory storage for registered students (in production, use a database)
registered_students = []

# IT Events with predefined timings
IT_EVENTS = {
    'Web Development Workshop': {'time': '9:30 AM - 10:30 AM', 'venue': 'Computer Lab 1'},
    'AI & Machine Learning Seminar': {'time': '11:00 AM - 12:00 PM', 'venue': 'Seminar Hall A'},
    'Cybersecurity Awareness': {'time': '1:00 PM - 2:00 PM', 'venue': 'Auditorium'},
    'Cloud Computing Basics': {'time': '2:30 PM - 3:30 PM', 'venue': 'Computer Lab 2'},
    'Data Science Bootcamp': {'time': '9:00 AM - 11:00 AM', 'venue': 'Conference Room'},
    'Mobile App Development': {'time': '10:00 AM - 11:30 AM', 'venue': 'IT Block - Room 301'},
    'Blockchain Technology': {'time': '12:00 PM - 1:00 PM', 'venue': 'Seminar Hall B'},
    'IoT Innovations': {'time': '3:00 PM - 4:00 PM', 'venue': 'Innovation Lab'},
    'Python Programming Contest': {'time': '9:30 AM - 12:30 PM', 'venue': 'Computer Lab 3'},
    'UI/UX Design Workshop': {'time': '2:00 PM - 3:30 PM', 'venue': 'Design Studio'}
}

# Admin credentials (use environment variables in production)
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')

@app.route('/')
def index():
    """Home page with registration form"""
    return render_template('index.html', events=IT_EVENTS)

@app.route('/register', methods=['POST'])
def register():
    """Handle student registration"""
    # Generate registration ID in format HME001, HME002, etc.
    registration_id = f"HME{str(len(registered_students) + 1).zfill(3)}"
    
    student_data = {
        'id': len(registered_students) + 1,
        'registration_id': registration_id,
        'name': request.form.get('name'),
        'phone': request.form.get('phone'),
        'register_number': request.form.get('register_number'),
        'department': request.form.get('department'),
        'year': request.form.get('year'),
        'college': request.form.get('college'),
        'events': request.form.getlist('events'),
        'date': request.form.get('date'),
        'registration_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Add event details for each selected event
    student_data['event_details'] = []
    for event_name in student_data['events']:
        if event_name in IT_EVENTS:
            student_data['event_details'].append({
                'name': event_name,
                'time': IT_EVENTS[event_name]['time'],
                'venue': IT_EVENTS[event_name]['venue']
            })
    
    registered_students.append(student_data)
    
    return redirect(url_for('success', student_id=student_data['id']))

@app.route('/success/<int:student_id>')
def success(student_id):
    """Success page after registration"""
    student = next((s for s in registered_students if s['id'] == student_id), None)
    if not student:
        return redirect(url_for('index'))
    
    return render_template('success.html', student=student)

@app.route('/registered-students')
def registered_students_page():
    """Page showing all registered students"""
    return render_template('registered_students.html', students=registered_students)

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin_login.html', error='Invalid credentials')
    
    return render_template('admin_login.html')

@app.route('/admin-dashboard')
def admin_dashboard():
    """Admin dashboard - requires login"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return render_template('admin_dashboard.html', students=registered_students)

@app.route('/admin-logout')
def admin_logout():
    """Admin logout"""
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/get-server-url')
def get_server_url():
    """Get server URL for QR code"""
    # In production, this should return your deployed URL
    # e.g., https://your-app.render.com or https://your-app.railway.app
    
    # Try to get from environment variable (for production deployment)
    deployed_url = os.environ.get('DEPLOYED_URL')
    
    if deployed_url:
        return jsonify({
            'url': deployed_url,
            'type': 'public',
            'message': 'Works on mobile data & any network!'
        })
    else:
        # Local development fallback
        return jsonify({
            'url': request.url_root.rstrip('/'),
            'type': 'local',
            'message': 'Local development mode'
        })

@app.route('/test')
def test():
    """Test route to verify server is running"""
    return render_template('test.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    
    print("\n" + "="*70)
    print("🎓 Event Registration Portal")
    print("="*70)
    print(f"🌐 Server starting on port {port}")
    print(f"🔧 Debug mode: {debug}")
    print("="*70 + "\n")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
