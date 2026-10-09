from flask import Flask, request, make_response

app = Flask(__name__)
FLAG = "picoCTF{c00k1es_4r3_cl13nt_s1d3}"

@app.route("/")
def index():
    resp = make_response("""
    <h1>Cookie Monster's Snack Bar</h1>
    <p>You are currently NOT a VIP. Check <a href="/vip">/vip</a> if you think you are one.</p>
    """)
    if not request.cookies.get("vip"):
        resp.set_cookie("vip", "false")
    return resp

@app.route("/vip")
def vip():
    is_vip = request.cookies.get("vip", "false")
    if is_vip == "true":
        return f"<h1>Welcome, VIP!</h1><p>Flag: {FLAG}</p>"
    return "<h1>Sorry, you're not VIP.</h1>", 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
