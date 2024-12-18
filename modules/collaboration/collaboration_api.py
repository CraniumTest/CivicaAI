from flask import Flask, request, jsonify
from drafting_module import DraftingModule

app = Flask(__name__)

@app.route('/draft', methods=['POST'])
def draft():
    content = request.json
    draft_text = DraftingModule().generate_draft(content['input'])
    return jsonify({'draft': draft_text})

if __name__ == '__main__':
    app.run(debug=True)
