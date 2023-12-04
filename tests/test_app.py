from playwright.sync_api import Page, expect

# Tests for your routes go here
"""
When I call GET /albums 
All albums are returned 
"""
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")

    div_items = page.locator("p")

    text = ["Title: DoolittleReleased: 1989",
    "Title: WaterlooReleased: 1974",
    "Title: LoverReleased: 2019",
    "Title: BaltimoreReleased: 1978"]
    
    expect(div_items).to_have_text(text)

    
"""
When I call GET /albums/<id> with an album.id
That album is returned
"""
def test_get_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")

    album_title = page.locator("h1")
    album_release = page.locator("p")
    
    expect(album_title).to_have_text("Doolittle")
    expect(album_release).to_have_text(["Release Year: 1989", "Artist: Pixies"])


"""
The page returned by GET /albums should contain a link for each album listed.
It should link to '/albums/<id>, where '<id>' is the corresponding album's id.
That page should then show information about the album.
"""
def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Doolittle'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Doolittle")
    p_tage = page.locator("p")
    expect(p_tage).to_have_text(["Release Year: 1989", "Artist: Pixies"])

def test_album_show_page_goes_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Doolittle'")
    page.click("text='Back to all albums'")
    div_items = page.locator("p")
    text = ["Title: DoolittleReleased: 1989",
    "Title: WaterlooReleased: 1974",
    "Title: LoverReleased: 2019",
    "Title: BaltimoreReleased: 1978"]
    expect(div_items).to_have_text(text)


"""
When I call GET /artists/<id>
The corresponding artist page is returned
"""
def test_get_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/1")

    artist_name = page.locator("h1")
    genre = page.locator("p")
    
    expect(artist_name).to_have_text("Pixies")
    expect(genre).to_have_text(["Genre: Rock", "Doolittle"])


"""
When I call GET /artists
All artists are returned
"""
def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")

    div_items = page.locator("p")
    text = ["Pixies",
    "ABBA",
    "Taylor Swift",
    "Nina Simone"]
    expect(div_items).to_have_text(text)


def test_artist_show_page_goes_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'")
    page.click("text='Back to all artists'")
    artist_list = page.locator("p")
    text = ["Pixies",
    "ABBA",
    "Taylor Swift",
    "Nina Simone"]
    expect(artist_list).to_have_text(text)




"""
When I call GET /albums 
All albums are returned
"""
# def test_get_albums(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")

#     get_response = web_client.get("/albums")
#     assert get_response.status_code == 200
#     assert get_response.data.decode("utf-8") == "Album(1, Doolittle, 1989, 1), Album(2, Waterloo, 1974, 2), Album(3, Lover, 2019, 3), Album(4, Baltimore, 1978, 4)"

"""
When I call GET /albums/<id>
The album with the correspdonding id is returned
"""
# def test_get_album(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     get_response = web_client.get("/albums/3")
#     assert get_response.status_code == 200
#     assert get_response.data.decode("utf-8") == "Album(3, Lover, 2019, 3)"

"""
When I call POST /albums with album info
That album is now in the list returned by GET /albums
"""
# def test_post_albums(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post("/albums", data =
#     {
#         'title': 'Little Girl Blue',
#         'release_year': '1959',
#         'artist_id': 4
#     })
#     assert post_response.status_code == 200
#     assert post_response.data.decode("utf-8") == ""

#     get_response = web_client.get("/albums")
#     assert get_response.status_code == 200
#     assert get_response.data.decode("utf-8") == "Album(1, Doolittle, 1989, 1), Album(2, Waterloo, 1974, 2), Album(3, Lover, 2019, 3), Album(4, Baltimore, 1978, 4), Album(5, Little Girl Blue, 1959, 4)"

"""
When I call GET /artists
All artists are returned
"""
# def test_get_artists(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")

#     get_response = web_client.get("/artists")
#     assert get_response.status_code == 200
#     assert get_response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone"

"""
When I call POST /artists with artist info name = 'Wild Nothing' and genre 'Indie'
That artist is now in the list returned by GET /artists
"""
# def test_post_artists(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")

#     post_response = web_client.post("/artists", data = 
#     {
#         'name': 'Wild Nothing',
#         'genre': 'Indie'
#     })

#     assert post_response.status_code == 200
#     assert post_response.data.decode("utf-8") == ""

#     get_response = web_client.get("/artists")
#     assert get_response.status_code == 200
#     assert get_response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild Nothing"










# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")


"""
GET /emoji
"""
# def test_get_emoji(web_client):
#     response = web_client.get("/emoji")
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
