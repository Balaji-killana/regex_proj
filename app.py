from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form.get("test_string")
    regex_pattern = request.form.get("regex_pattern")
    # Perform regex matching and store results
    matched_strings = perform_regex_matching(test_string, regex_pattern)
    return render_template("results.html", matched_strings=matched_strings)

@app.route("/validate_email", methods=["POST"])
def validate_email():
    email = request.form.get("email")
    # Perform email validation
    is_valid = validate_email_address(email)
    return render_template("email_validation_result.html", email=email, is_valid=is_valid)

def perform_regex_matching(test_string, regex_pattern):
    import re
    return re.findall(regex_pattern, test_string)

def validate_email_address(email):
    import re
    # Regular expression pattern for validating email addresses
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
