import hou

def show_message(text):
    hou.ui.displayMessage(text, title="COMING SOON!")


def run():

    message = "THIS FEATURE IS NOT YET AVAILABLE"

    secondmessage = "Stay Tuned!"



    show_message(message + "\n\n" + secondmessage)