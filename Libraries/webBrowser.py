import webbrowser

# Remotely controls web browsers
# blocks on non gui based browser systems
# https://docs.python.org/3.7/library/webbrowser.html
firefox = webbrowser.get(using='firefox')
firefox.open("https://google.com")
