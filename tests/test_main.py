from bonjour.__main__ import greeting


def test_greeting():
    assert greeting() == "Hello from PDM!"
