from fasthtml.common import *

app = FastHTML()


@app.get("/")
def home():
    page = Html(
        Head(Title("Some Heading")),
        Body(
            Div(
                "Some Text",
                A("A Link", href="https://www.youtube.com"),
                Img(src="https://placehold.co/200"),
                cls="my_class",
            )
        ),
    )
    return page


serve()
