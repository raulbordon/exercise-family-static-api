@app.route('/members', methods=['POST'])
def add_member():
    member_data = request.get_json()
    new_member = jackson_family.add_member(member_data)
    return jsonify(new_member), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    success = jackson_family.delete_member(member_id)
    return jsonify({"done": success}), 200
