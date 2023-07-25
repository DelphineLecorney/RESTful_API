from flask import jsonify
from models.Post import Post
from config.config import app, db

# Define a route to delete a post by its ID
@app.route('/api/v1/posts/<int:post_id>', methods=['DELETE'])
def deletePostById(post_id):
    post = Post.query.get(post_id)

    if post is None:
        return jsonify({'message': 'Post not found'}), 404

    try:
        db.session.delete(post)
        db.session.commit()
        return jsonify({'message': 'Post successfully deleted'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error deleting post.', 'details': str(e)}), 500
