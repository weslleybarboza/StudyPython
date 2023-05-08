#function with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    f_name_formated = f_name.title()
    l_name_formated = l_name.title()
    return f"Result: {f_name_formated} {l_name_formated}."

print(format_name("WesLLey", "KdijHg"))

