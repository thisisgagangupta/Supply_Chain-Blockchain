from flask import flask, render_template, request
import pandas as pd
import your_analysis_script # your Jupyter Notebook code

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('flask.html')

@app.route('/result', methods=['POST'])
def result():
    # get the form input
    product_name = request.form['product_name']
    
    # run your analysis script with the input
    result_df = your_analysis_script.run(product_name)
    
    # convert the result to HTML table format
    result_table = result_df.to_html()
    
    # render the result template with the table
    return render_template('result.html', table=result_table)

if __name__ == '__main__':
    app.run(debug=True)
