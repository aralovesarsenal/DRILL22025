from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value

    # Clear the output div first
    document.querySelector("#output").innerText = ""

    # Multiline message using input values
    message = f""" Student Profile
    Name   : {name}
    Age    : {age}
    School : {school}

    ✏️ Notes:
    {name} is currently {age} years old and studies at {school}!

    display(message, target="output")

