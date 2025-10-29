import glob


def rewriter(file_path, search_list):
    """Rewrites lines matching certain criteria by commenting them out in html"""
    print("-" * 50, "\nProcessing file:", file_path)

    with open(file_path, "r", encoding="utf-8") as file:
        inputs = file.readlines()

    outputs = inputs.copy()

    line_found = False
    # Check every line if it contains a particular substring and apply html comment if it does
    for key, line in enumerate(inputs):
        if any(string in line for string in search_list) and "<!--" not in line:
            print(f"Rewriting line {key}:", line)
            # Add '<!--' to the start and '-->' after the first '</script>'
            commented_line = "<!--" + line.rstrip().replace("</script>", "</script> -->\n", 1)
            outputs[key] = commented_line
            line_found = True

    # Rewrite the file if any of the lines meet the criteria
    if line_found:
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(outputs)
    else:
        print("Didn't find anything to rewrite")


files = glob.glob(".\\docs\\**\\*.html", recursive=True)
# If these substrings are present in a line, comment the line out
search_scripts = [
    "https://cdnjs.cloudflare.com/polyfill",
    "https://cdn.jsdelivr.net/npm/mathjax",
    "https://cdnjs.cloudflare.com/ajax/libs/",
    "https://cdn.jsdelivr.net/npm/jquery",
    "https://cdn.jsdelivr.net/npm/",
    """type="application/javascript">define('jquery'"""
]

for f in files:
    rewriter(f, search_scripts)

print("\nFinished cleanup")
