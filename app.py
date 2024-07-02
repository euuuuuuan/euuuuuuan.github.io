from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 가상의 블로그 포스트 데이터
blog_posts = [
    {'title': 'First Blog Post', 'content': 'This is the content of the first blog post.'},
    {'title': 'Second Blog Post', 'content': 'This is my second blog post. More content to come!'},
    {'title': 'Another Interesting Post', 'content': 'This blog post is about something really interesting.'}
]

comments = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', blog_posts=blog_posts, comments=comments)

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
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    comments.append({'comment': comment, 'timestamp': timestamp})
    return jsonify({'status': 'success', 'comment': comment, 'timestamp': timestamp})

@app.route('/delete_comment', methods=['POST'])
def delete_comment():
    comment_id = request.json['comment_id']
    if 0 <= comment_id < len(comments):
        comments.pop(comment_id)
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'}), 400

@app.route('/update_comment', methods=['POST'])
def update_comment():
    comment_id = request.json['comment_id']
    new_comment = request.json['new_comment']
    if 0 <= comment_id < len(comments):
        comments[comment_id]['comment'] = new_comment
        comments[comment_id]['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return jsonify({'status': 'success', 'new_comment': new_comment, 'timestamp': comments[comment_id]['timestamp']})
    return jsonify({'status': 'error'}), 400

@app.route('/search_posts', methods=['GET'])
def search_posts():
    query = request.args.get('query', '').lower()
    results = [post for post in blog_posts if query in post['title'].lower() or query in post['content'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
