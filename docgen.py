import os
import docgen_file as docgen

path = "pages/"
savepath = "../gmas_webdriver_wiki/"

for f in os.listdir(path):
	if "SCR" in f and f[-2:] == "py":
		# get the filename/classname (f[:-3])
		doc = ""
		try:
			doc = docgen.get_method_list(f[:-3])
		except:
			print "ERROR %s" % f[:-3]

		if doc != "":
			with open("%s%s.md" % (savepath, f[:-3]), "w") as file:
				file.write(doc)
