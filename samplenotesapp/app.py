# a simple notes app made with flask
# inspired from making a form with flask
from flask import * 
import os

app = Flask(__name__)

# I think making this a function keeps me sane
def read_notes():
	notes = os.listdir("notes")
	global note_file_names
	global note_contents
	global read_note
	note_contents = []
	note_file_names = []
	for i in notes:
		# if this is not done, then you will notice two empty note boxes (preferbly on UNIX I think)
		if not i.startswith("."):
			note_root_path = "notes/" + i
			note_file_names.append(i)
			note_text = open(note_root_path, "r")
			# keep an original copy
			read_note = note_text.read()
			# I need this because I found a bug that the button glitches out if the notebox has anything more than 500+ characters
			read_note_sliced = read_note[0:150]
			note_contents.append(read_note_sliced)

@app.route("/editor")
def editor():
	return render_template("editor.html")
	
@app.route("/submit", methods=["POST"])
def save_note():
	note = request.form["note"]
	filename = request.form["filename"]
	if request.form["filetype"] == "md":
		filename = "notes/" + filename + ".md"
	elif request.form["filetype"] == "txt":
		filename = "notes/" + filename + ".txt"
	elif request.form["filetype"] == "html":
		filename = "notes/" + filename + ".html"
	with open(filename, "w") as file: 
		file.write(note)
	return redirect(url_for("index"))

@app.route("/index")
def index():
	read_notes()
	return render_template("index.html", noteitems=zip(note_file_names, note_contents))

@app.route("/edit", methods=["GET", "POST"])
def edit_note():
	print("Success!")
	note_file_name = request.args.get("title")
	# find note_content by file name instead
	note_content_file = open("notes/" + note_file_name, "r")
	note_content = note_content_file.read()
	note_name, extension = os.path.splitext(note_file_name)
	return render_template("editor.html", note_file_name=note_name, note=note_content)

@app.route("/delete", methods=["GET", "POST"])
def delete_note():
	note_file_name = request.args.get("title")
	file_path = os.path.join("notes", note_file_name)
	os.remove(file_path)
	return redirect(url_for("index"))
	# googling instead of reading docs :-|

if __name__=="__main__":
    print("PLEASE VISIT THIS INSTEAD: http://127.0.0.1:5000/index.")
    # remove host=0.0.0.0 if u don't want other devices to access on LAN
    app.run(host="0.0.0.0", use_reloader=False, debug=True)

