from flask import Flask, request, jsonify
import pandas as pd


app = Flask(__name__)

# Load and clean the data (reusing the previous cleaning script)
# the cleaned dataframe from previous steps
df = pd.read_csv("dataset\cleaned_departments_dataset.csv")


@app.route('/')
def index():
    return """
    <h1>Welcome to the Employee Data API</h1>
    <p>Use the following endpoints to interact with the API:</p>
    <ul>
        <li><strong>/top_n_employees?n=N</strong> - Get the top N highest-paid employees. Replace <em>N</em> with the number of employees.</li>
        <li><strong>/employee_count?department=DEPARTMENT</strong> - Get the number of employees in a specific department. Replace <em>DEPARTMENT</em> with the department name.</li>
    </ul>
    <p>Examples:</p>
    <ul>
        <li><a href="/top_n_employees?n=3">/top_n_employees?n=3</a> - Get the top 3 highest-paid employees.</li>
        <li><a href="/employee_count?department=Finance">/employee_count?department=Finance</a> - Get the number of employees in the Finance department.</li>
    </ul>
    """


@app.route('/top_n_employees', methods=['GET'])
def get_top_n_employees():
    # Default to top 3 employees if 'n' is not specified
    n = int(request.args.get('n', 3))
    top_n_employees = df.nlargest(n, 'Salary')[['Name', 'Salary']]
    return jsonify(top_n_employees.to_dict(orient='records'))


@app.route('/employee_count', methods=['GET'])
def get_employee_count():
    department = request.args.get('department')
    count = df[df['Department'] == department].shape[0] # Number of rows in the filtered DataFrame (the count of rows).
    return jsonify({department: count})


if __name__ == '__main__':
    app.run(debug=True)
