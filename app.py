from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# 가상의 데이터베이스
comments = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', comments=comments)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # 이메일 보내기 로직 또는 데이터베이스 저장 로직 추가 가능
        return redirect(url_for('home'))
    return render_template('contact.html')

@app.route('/add_comment', methods=['POST'])
def add_comment():
    comment = request.json['comment']
    comments.append(comment)
    return jsonify({'status': 'success', 'comment': comment})

if __name__ == '__main__':
    app.run(debug=True)

