from js import document  # type: ignore
from pyodide.ffi import create_proxy #type:ignore
attempts = 0
secret_number = 87
def check_guess(event):
    global attempts 
    attempts += 1
    guess_input = document.querySelector("#number").value
    if not guess_input:
        return
    guess = int(guess_input)
    message = document.querySelector(".message")
    if guess < secret_number:
        message.innerText = "🔻 Too low! Try again."
    elif guess > secret_number:
        message.innerText = "🔺 Too high! Try again."
    else:
        message.innerText = f"✅ Congratulations! You guessed it in {attempts} attempts."
        attempts=0
    message.style.display = "block"
    message.style.textAlign="center"
check_guess_proxy = create_proxy(check_guess)
document.querySelector(".but1").addEventListener("click", check_guess_proxy)
def reset(event):
    document.querySelector("#number").value = ""
    message = document.querySelector(".message")
    message.innerText = ""
reset_proxy=create_proxy(reset)
document.querySelector(".but2").addEventListener("click",reset_proxy)