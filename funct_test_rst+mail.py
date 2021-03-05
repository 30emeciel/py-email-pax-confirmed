from datetime import date

from box import Box
from dotenv import load_dotenv


def func_test_rst_mail():
    pax = Box({
        "name": "Hello"
    })
    data = Box({
        "pax": pax,
    })

    html = generate_confirmed_pax_html_text(data)
    send_mail("tony.lbvre@gmail.com", "Test Reservation Mail", html)


if __name__ == "__main__":
    load_dotenv()
    from mail import send_mail
    from rst import generate_confirmed_pax_html_text
    func_test_rst_mail()
