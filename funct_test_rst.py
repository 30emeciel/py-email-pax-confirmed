from box import Box
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    from rst import generate_confirmed_pax_html_text
    pax = Box({
        "name": "Hello"
    })
    data = Box({
        "pax": pax
    })
    html = generate_confirmed_pax_html_text(data)
    with open("test.html", mode='wb') as f:
        f.write(html.encode())

