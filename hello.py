def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
        "Japanese": "Ohaiyo", ### homework = with myanmar greeting
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a Personal Greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="I like ladies"
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=['English','Spanish','German','Japanese'],
        help="The language of the greeting."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)
