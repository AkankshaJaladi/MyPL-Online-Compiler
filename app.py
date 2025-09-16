from flask import Flask, render_template, request, jsonify
import sys
import importlib.util

# Load your interpreter
spec = importlib.util.spec_from_file_location("basic", "basic.py")
basic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(basic)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_code():
    code = request.json.get("code", "")

    import io, sys
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    result, error = basic.run("<web>", code)

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    if error:
        return jsonify({"output": error.as_string()})
    else:
        # Include PRINT outputs + returned result (if any)
        if result is not None:
            output += str(result)
        return jsonify({"output": output.strip()})


if __name__ == "__main__":
    app.run(debug=True)
