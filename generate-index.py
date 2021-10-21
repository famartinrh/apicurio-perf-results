import os

indexTextStart = """<!DOCTYPE html>
<html>
<head><title>Index of {folderPath}</title></head>
<body>
    <h2>Index of {folderPath}</h2>
    <hr>
    <ul>
		<li>
			<a href='../'>../</a>
		</li>
"""
indexTextEnd = """
	</ul>
</body>
</html>
"""

def index_folder(folderPath):
	print("Indexing: " + folderPath +'/')
	#Getting the content of the folder
	allfiles = os.listdir(folderPath)

	files = []
	for af in allfiles:
		if af == ".git":
			continue
		if af == ".github":
			continue
		if af == "scripts" and folderPath == ".":
			continue
		files.append(af)

	it = ""
	for file in files:
		print("Processing file: " + file )
		if file == 'index.html' and not folderPath == ".":
			it += "\t\t<li>\n\t\t\t<a href='" + folderPath+ "/"+file + "'>" + folderPath+ "/"+file + "</a>\n\t\t</li>\n"
		#Recursive call to continue indexing
		if os.path.isdir(folderPath+'/'+file):
			it += index_folder(folderPath + '/' + file)
	return it

#Indexing root directory (Script position)
it = indexTextStart.format(folderPath="Root")
it += index_folder('.')
it += indexTextEnd
index = open('./index.html', "w")
#Save indexed content to file
index.write(it)
