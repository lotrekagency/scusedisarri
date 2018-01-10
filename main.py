import pylla

app = pylla.App()

app.add_routes('sarri.urls')
app.add_routes('quotes.urls')
