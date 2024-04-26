from flask import Blueprint, request, jsonify, session
import sqlite3
from flask_jwt_extended import decode_token

course_routes = Blueprint('course_routes', __name__)

# Dummy function to enroll in a course
def enroll_course(user_id, course_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    try:
        # Check if the enrollment already exists
        c.execute("SELECT COUNT(*) FROM Course_Enrolled WHERE uid = ? AND cid = ?", (user_id, course_id))
        count = c.fetchone()[0]
        if count > 0:
            return False  # Enrollment already exists
        else:
            c.execute("INSERT INTO Course_Enrolled (uid, cid, status) VALUES (?, ?, ?)", (user_id, course_id, 'enrolled'))
            conn.commit()
            return True  # Successfully enrolled
    except sqlite3.Error as e:
        print("Error enrolling in course:", e)
        return False  # Failed to enroll
    finally:
        conn.close()


# Dummy function to delete enrollment for a course
def delete_enrollment(user_id, course_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    try:
        c.execute("DELETE FROM Course_Enrolled WHERE uid = ? AND cid = ?", (user_id, course_id))
        conn.commit()
        return True  # Successfully deleted enrollment
    except sqlite3.Error as e:
        print("Error deleting enrollment:", e)
        return False  # Failed to delete enrollment
    finally:
        conn.close()

# Function to retrieve users enrolled in a course by course ID
def get_users_by_course_id(course_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    try:
        c.execute("SELECT u.id, CASE WHEN u.status = 0 THEN u.email ELSE 'Private Profile' END AS email FROM Users u JOIN Course_Enrolled ce ON u.id = ce.uid WHERE ce.cid = ?", (course_id,))
        users = c.fetchall()
        return users
    except sqlite3.Error as e:
        print("Error retrieving users by course ID:", e)
        return []
    finally:
        conn.close()

@course_routes.route('/enroll-course', methods=['GET'])
def enroll_course_route():
    token = session.get('token')
    if not token:
        return jsonify({'message': 'Token is missing.'}), 400

    # Implement your logic to decode the token and get user ID
    user_id = decode_token(token)['sub']

    course_id = request.args.get('cid')
    if not course_id:
        return jsonify({'error': 'Course ID is required'}), 400

    if enroll_course(user_id, course_id):
        return jsonify({'message': 'Enrolled successfully'}), 200
    else:
        return jsonify({'error': 'Failed to enroll'}), 500


@course_routes.route('/delete-enrollment', methods=['DELETE'])
def delete_enrollment_route():
    token = request.args.get('token')
    if not token:
        return jsonify({'message': 'Token is missing.'}), 400

    # Implement your logic to decode the token and get user ID
    user_id = decode_token(token)['sub']

    course_id = request.args.get('cid')
    if not course_id:
        return jsonify({'error': 'Course ID is required'}), 400

    if delete_enrollment(user_id, course_id):
        return jsonify({'message': 'Enrollment deleted successfully'}), 200
    else:
        return jsonify({'error': 'Failed to delete enrollment'}), 500

@course_routes.route('/get-users-by-course-id', methods=['GET'])
def get_users_by_course_id_route():
    course_id = request.args.get('cid')
    if not course_id:
        return jsonify({'error': 'Course ID is required'}), 400

    users = get_users_by_course_id(course_id)
   
    users_list = [{'id': user[0], 'email': user[1]} for user in users]
    return jsonify({'users': users_list}), 200
