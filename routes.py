from flask import render_template, request, redirect, url_for, flash, session
from models import db, Post, User
from auth import login_required
from utils import validate_post

def init_routes(app):
    @app.route('/')
    def index():
        posts = Post.query.order_by(Post.created_at.desc()).all()
        return render_template('index.html', posts=posts)

    @app.route('/post/<int:post_id>', methods=['GET', 'POST'])
    def post(post_id):
        post = Post.query.get_or_404(post_id)
        if request.method == 'POST':
            if 'user_id' not in session or session['user_id'] != post.author_id:
                flash('You are not authorized to edit this post.', 'error')
                return redirect(url_for('post', post_id=post_id))
            
            title = request.form.get('title')
            content = request.form.get('content')
            category = request.form.get('category')
            
            if not validate_post(title, content, category):
                flash('All fields are required.', 'error')
                return render_template('post.html', post=post)
            
            post.title = title
            post.content = content
            post.category = category
            db.session.commit()
            flash('Post updated successfully.', 'success')
            return redirect(url_for('post', post_id=post_id))
        
        return render_template('post.html', post=post)

    @app.route('/create', methods=['POST'])
    @login_required
    def create_post():
        title = request.form.get('title')
        content = request.form.get('content')
        category = request.form.get('category')
        
        if not validate_post(title, content, category):
            flash('All fields are required.', 'error')
            return redirect(url_for('index'))
        
        post = Post(
            title=title,
            content=content,
            category=category,
            author_id=session['user_id']
        )
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully.', 'success')
        return redirect(url_for('index'))

    @app.route('/delete/<int:post_id>', methods=['POST'])
    @login_required
    def delete_post(post_id):
        post = Post.query.get_or_404(post_id)
        if session['user_id'] != post.author_id:
            flash('You are not authorized to delete this post.', 'error')
            return redirect(url_for('post', post_id=post_id))
        
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted successfully.', 'success')
        return redirect(url_for('index'))
