from shiny import reactive
from shiny.express import input, render, ui

ui.h2("Word Counter")
ui.input_text_area("text_input", "Enter text:", rows=10, width="100%")
ui.input_action_button("count_button", "Count Words")


@render.code
@reactive.event(input.count_button)
def word_count_code():
    text = input.text_input()
    words = text.split()
    if not len(words):
        return "Error: Some text input is required."
    word_count = len(words)
    return word_count
