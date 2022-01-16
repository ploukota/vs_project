from Main import text_do_mors, mors_do_text, main

pole = "priklad"


def test_main_chec_text_do_mors():
    text_do_mors(pole)


def test_main_chec_mors_do_text():
    mors_do_text(pole)


def test_mors_do_text1():
    mors = "... --- ..."
    assert mors_do_text
    ("S O S") == mors


def test_text_do_mors1():
    text = "S O S"
    assert text_do_mors
    ("... --- ...") == text


def test_main():
    print("1")
    response = "1"
    assert main
    ("Napiste morseovku (s mezerou mezi kazdym pismenem): ") == response


def test_main2():
    print("2")
    response2 = "2"
    assert main
    ("Napište text: ") == response2
