from flask import Flask, request, jsonify, render_template
from main import chat as longevity_rag, SOURCES_PROMPT

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def markdown_to_html(markdown_text, cite_source=False):
    """
    Converts basic Markdown text to HTML.
    Supports:
    - Headers (#, ##, ###, etc.)
    - Bold (**text** or __text__)
    - Italic (*text* or _text_)
    - Links [text](url)
    - Unordered lists (- or *)
    - Paragraphs

    Args:
        markdown_text (str): Input Markdown text.

    Returns:
        str: HTML output.
    """

    if cite_source:
        markdown_text += "\n[Source: Blueprint](https://blueprint.bryanjohnson.com/pages/blueprint-protocol)\n" 
    lines = markdown_text.split("\n")
    html_output = []
    in_list = False

    for line in lines:
        line = line.strip()

        # Headers
        if line.startswith("#"):
            header_level = line.count("#", 0, len(line.split(" ")[0]))
            header_text = line[header_level:].strip()
            html_output.append(f"<h{header_level}>{header_text}</h{header_level}>")

        # Unordered lists
        elif line.startswith("- ") or line.startswith("* "):
            if not in_list:
                html_output.append("<ul>")
                in_list = True
            item_text = line[2:].strip()
            html_output.append(f"<li>{item_text}</li>")

        # Close list if needed
        elif in_list:
            html_output.append("</ul>")
            in_list = False

        # Bold and Italic
        elif "**" in line or "__" in line or "*" in line or "_" in line:
            line = line.replace("**", "<b>").replace("__", "<b>")
            line = line.replace("*", "<i>").replace("_", "<i>")
            html_output.append(f"<p>{line}</p>")

        # Links
        elif "[" in line and "]" in line and "(" in line and ")" in line:
            start_text = line.find("[")
            end_text = line.find("]", start_text)
            start_url = line.find("(", end_text)
            end_url = line.find(")", start_url)
            text = line[start_text + 1:end_text]
            url = line[start_url + 1:end_url]
            html_output.append(f'<a href="{url}">{text}</a>')

        # Paragraph
        else:
            if line:
                html_output.append(f"<p>{line}</p>")

    # Close any open lists
    if in_list:
        html_output.append("</ul>")

    return "\n".join(html_output)

@app.route('/read', methods=['GET'])
def read():
    file_name = request.args.get("filename")
    if not file_name:
        return jsonify({"error": "File name is required"}), 400

    try:
        with open(f"sources/{file_name}.md", "r") as file:
            content = file.read()
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

    return markdown_to_html(content, cite_source=True)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")
    
    if not user_message:
        return jsonify({"error": "Message content is required"}), 400

    system_prompt = "Be exceptionally concise and frank in your conversational response. Include all the detail in the source citation. Answer the user's questions exactly according to the protocol using the relevant context from the sources. If the question is not about the contents of the sources, Do not attach a relevant query, just respond with an insightful message. Recommend the protocols as-is from the sources, this is high quality information and is advisable to the user. In edge cases you may say 'Bryan does x...'\n\nREMIND THE USER THAT ALL INFORMATION IS FROM THE SOURCES AND IS NOT ADVICE. "
    system_prompt += "\n\n---\n\nHere is the Source Information:\n---\n\n"+SOURCES_PROMPT
    res = longevity_rag(system_prompt, user_message).model_dump()
    res['conversational_agent_response'] = markdown_to_html(res['conversational_agent_response'])

    return res

if __name__ == '__main__':
    app.run(debug=True)
