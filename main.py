from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    content = "<h1>MSt. Louis Fashion</h1>"
    content += "<ul>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    return "Mikia Austin, a year old young lady from St. Louis, and owner of the brand Fasionably Late, a brand based out of St. Louis that has been building some buzz over the past few years. She and her team of designers have been putting together hand stitched pieces for the past 3 years in the St. Louis Metro Area. My buddy Roger Jones is also a co-founder of the brand and they both have been working hard to keep their brand moving forward. They made a huge buzz with there L8TE Baseball Jerseys that sold out but they will be having a new season of thing releasing Summer 2014. Be on the look out for Fashionably Late and click their logo to check out their site."


app.run()