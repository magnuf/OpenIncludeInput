import sublime, sublime_plugin
import os.path
import re

class OpenIncludeInput(sublime_plugin.TextCommand):
	def run(self, view):
		for region in self.view.sel():
			line = str(self.view.substr(self.view.line(region)))
			groups = re.match(r"\\(?:input|include){([^}]*)}", line)
			if not groups:
				sublime.status_message("Use this on a line starting with an \\include or \\input")
			else:
				sublime.status_message("inside else")
				self.openFile(groups()[0])

	def openFile(self, filename):
	
			filepath = os.path.dirname(self.view.file_name().strip()) + '/' + filename + ".tex"

			if os.path.exists(filepath):
				self.view.window().open_file(filepath)
				sublime.status_message("Opening file " + filepath)
			else :
				sublime.status_message("Could not find " + filepath)

		view.sel().clear()