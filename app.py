import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.album import *
from lib.artist import *
from lib.artist_repository import *


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


@app.route('/albums', methods = ['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection) 
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    repository.create(album)
    return ""

# new html route
@app.route('/albums', methods = ['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/index.html', albums=albums)

# new html route
@app.route('/albums/<id>', methods = ['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    repository = ArtistRepository(connection)
    artist = repository.find(album.artist_id)
    return render_template('albums/show.html', album=album, artist=artist)

@app.route('/albums/<id>', methods=['DELETE'])
def delete_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.delete(id)
    return "Album deleted successfully"

@app.route('/artists', methods = ['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('artists/index.html', artists=artists)

@app.route('/artists/<id>', methods = ['GET'])
def get_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find_with_albums(id)
    return render_template('artists/show.html', artist=artist)

@app.route('/artists', methods = ['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection) 
    artist = Artist(None, request.form['name'], request.form['genre'], [])
    repository.create(artist)
    return ""


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
