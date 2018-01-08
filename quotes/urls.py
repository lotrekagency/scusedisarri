from .views import QuoteView

urls = (
    ('/dice', QuoteView()),
    ('/dice/{quote}', QuoteView())
)