from flask import Flask, request
import os
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route('/set_query', methods=['POST'])
def set_query():
    data = request.json
    query = data.get('query')
    
    if query:
        os.environ['QUERY'] = query
        # Generate a timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"data_{timestamp}.txt"
        # Execute the main.py script
        subprocess.run(['python3', 'main.py', '--start=1', '--stop=5', f'--file={filename}'])
        return f"Query updated to: {query}", 200
    else:
        return "Query not provided", 400

if __name__ == '__main__':
    app.run(debug=True)
