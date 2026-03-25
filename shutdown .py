def shutdown(user_input):
    if user_input == "Yes":
        return "Shutting down"
    elif user_input == "No":
        return "Abort shutdown"
    else:
        return "Sorry"
