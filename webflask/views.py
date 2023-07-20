import time
#import subprocess
import json
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from zapv2 import ZAPv2
from webflask.models import Note, User, TestRequest, Service
from webflask import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home_page():
    show_div = True  # Set the value of show_div
    return render_template("base.html", show_div=show_div, user=current_user)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added successfully!', category='success')

    show_search = True  # show_search bar
    return render_template("services.html", user=current_user, show_search=show_search, username=current_user.username)


@views.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    results = []  # Initialize results with an empty list
    search_query = ''  # Assign an initial value to search_query
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        results = Note.query.filter(
            Note.data.ilike(f'%{search_query}%'),
            Note.user_id == current_user.id).all()

    show_search = True  # show_search bar
    return render_template('search.html', results=results, query=search_query, show_search=show_search, user=current_user)


@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/scan_url', methods=['GET', 'POST'])
# @login_required
def scan_url():
    if request.method == 'POST':
        scan_url = request.form.get('scan_url')
        try:
            # Start OWASP ZAP as a subprocess
            #zap_process = subprocess.Popen(['owasp-zap', '-daemon', '-host', '0.0.0.0', '-port', '8080'])

            # Wait for ZAP to initialize
            # time.sleep(20)
            time.sleep(5)

            # Initialize the ZAP API client
            zap_api_key = 'fullstack'  # Replace with your ZAP API key
            # Replace with the base URL of your ZAP instance
            zap_base_url = 'http://localhost:8080'
            zap = ZAPv2(apikey=zap_api_key, proxies={
                        'http': zap_base_url, 'https': zap_base_url})

            # Start a new ZAP session
            zap.core.new_session()

            # Open the target URL in ZAP
            zap.spider.scan(scan_url)

            # Wait for ZAP to complete its scanning actions
            while zap.spider.status() != '100':
                time.sleep(5)

            # Retrieve the ZAP alerts
            alerts = zap.core.alerts()

            # Store the alerts in a list
            unique_alerts = {}  # To keep track of unique alerts

            # Iterate over the alerts and add unique alerts to the dictionary
            for alert in alerts:
                alert_string = alert.get('alert')
                risk = alert.get('risk')
                solution = alert.get('solution')
                if alert_string not in unique_alerts:
                    unique_alerts[alert_string] = {
                        'risk': risk, 'solution': solution}

            # Stop the OWASP ZAP subprocess
            # zap_process.terminate()
            # zap_process.wait()

            return render_template('scan_url.html', user=current_user, scan_url=scan_url, alerts=unique_alerts)
        except Exception as e:
            error_message = str(e)

            # Stop the OWASP ZAP subprocess
            # zap_process.terminate()
            # zap_process.wait()
            return render_template('scan_url.html', user=current_user, error_message=error_message)
    return render_template('scan_url.html', user=current_user)


@views.route('/admin-panel')
@login_required
def admin_panel():
    if current_user.is_admin:
        users = User.query.all()
        return render_template('admin_panel.html', users=users, user=current_user)
    else:
        flash('You are not authorized to access the admin panel.', 'error')
        return redirect(url_for('views.home'))


@views.route('/submit-test-request', methods=['POST', 'GET'])
@login_required
def submit_test_request():
    # Retrieve form data
    if request.method == 'POST':
        selected_service = request.form.getlist('services')
        ip_address = request.form.get('ip')

        if not ip_address:
            flash('IP address is required!', category='error')
        else:
            services = Service.query.filter(Service.name.in_(
                selected_service)).order_by(Service.service_id).all()

            # Create a new test request and associate selected services
            if services:
                new_request = TestRequest(
                    user_id=current_user.id, ip=ip_address, services=services)
                db.session.add(new_request)
                db.session.commit()
                flash('Test request submitted successfully!', category='success')
            else:
                flash('No services selected!', category='error')

    return render_template('services.html', user=current_user, username=current_user.username)


@views.route('/services/delete-test-request/<int:request_id>', methods=['POST'])
@login_required
def delete_test_request(request_id):
    test_request = TestRequest.query.get(request_id)
    # Check if the test request exists and belongs to the current user
    if test_request and test_request.user_id == current_user.id:
        db.session.delete(test_request)
        db.session.commit()
        return '', 204  # Return 'No Content' status for successful deletion
    else:
        # Test request not found or user does not have permission
        return 'Unauthorized', 401  # Return 'Unauthorized' status
