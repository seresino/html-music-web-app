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
When I create a new album
I can see it in the albums index
"""
def test_create_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")

    page.fill("input[name='title']", "Little Girl Blue")
    page.fill("input[name='release_year']", "1959")
    page.fill("input[name='artist_id']", "4")
    page.click("text=Add Album")

    album_title = page.locator("h1")
    expect(album_title).to_have_text("Little Girl Blue")

"""
If we create a new album without a title, release_year or artist_id
We see an error message
"""
def test_create_album_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.click("text=Add Album")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Title can't be blank, Release Year can't be blank, Artist can't be blank")





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
When I create a new artist
I can see it in the artists index
"""
def test_create_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist")

    page.fill("input[name='name']", "Ruby Seresin")
    page.fill("input[name='genre']", "Pop")
    page.click("text=Add Artist")

    name = page.locator("h1")
    expect(name).to_have_text("Ruby Seresin")

"""
If we create a new artists without a name or genre
We see an error message
"""
def test_create_artist_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist")
    page.click("text=Add Artist")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Name can't be blank, Genre can't be blank")

"""
When we delete a book
We no longer see it in the books index
"""
# def test_delete_book(db_connection, page, test_web_address):
#     db_connection.seed("seeds/book_store.sql")
#     page.goto(f"http://{test_web_address}/books")
#     page.click("text=Invisible Cities by Italo Calvino")
#     page.click("text=Delete Book")
#     list_items = page.locator("li")
#     expect(list_items).to_have_text([
#         "The Man Who Was Thursday by GK Chesterton",
#         "Bluets by Maggie Nelson",
#         "No Place on Earth by Christa Wolf",
#         "Nevada by Imogen Binnie",
#     ])








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
