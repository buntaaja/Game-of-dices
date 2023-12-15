import simple_colors

def introduction(text):
    print(simple_colors.red((text), ['bold']))

def show(text):
    print(simple_colors.blue(text))

def warning(text):
    print(simple_colors.yellow(text))

def warning_input(text):
    return input(simple_colors.yellow(text)).strip().upper()

def text_input(text):
    return input(text).strip().upper()

def success(text):
    print(simple_colors.green(text))

def error(text):
    print(simple_colors.red(text))

def sorry(text):
    print(simple_colors.magenta(text))