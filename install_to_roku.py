import sublime, sublime_plugin
import os
import subprocess

class InstallToRokuCommand(sublime_plugin.WindowCommand):
	def run(self, dirs):
		settings = sublime.load_settings("InstallToRoku.sublime-settings")
		username = sublime.Settings.get(settings, "roku_username")
		password = sublime.Settings.get(settings, "roku_password")
		ip = sublime.Settings.get(settings, "roku_ip_address")
		url = "http://"+ip+"/plugin_install"
		folder = dirs[0]

		if sublime.ok_cancel_dialog("Install folder '"+dirs[0]+"' to Roku at "+ip+"?", "Install"):
			install = True

			if not os.path.isfile(folder+"/manifest"):
				sublime.message_dialog("'manifest' file missing")
				install = False

			if not os.path.isdir(folder+"/source"):
				sublime.message_dialog("'source' directory missing")
				install = False

			if install:
				subprocess.Popen(["python", "BrightScript-Installer-Plugin/install.py", username, password, url, folder])
				sublime.message_dialog("Your channel is being installed.\nPlease be patient, this may take a while.")

	def is_visible(self, dirs):
		return len(dirs) > 0

class InstallToRokuSettingsIpCommand(sublime_plugin.WindowCommand):
	def run(self):
		settings = sublime.load_settings("InstallToRoku.sublime-settings")
		ip = sublime.Settings.get(settings, "roku_ip_address")

		def on_done(user_input):
			sublime.Settings.set(settings, "roku_ip_address", user_input)
			sublime.save_settings("InstallToRoku.sublime-settings")

		def on_change(user_input):
			pass

		def on_cancel():
			print "changes not saved"

		sublime.Window.show_input_panel(sublime.active_window(), "Roku Ip Address", ip, on_done, on_change, on_cancel)

class InstallToRokuSettingsUsernameCommand(sublime_plugin.WindowCommand):
	def run(self):
		settings = sublime.load_settings("InstallToRoku.sublime-settings")
		username = sublime.Settings.get(settings, "roku_username")

		def on_done(user_input):
			sublime.Settings.set(settings, "roku_username", user_input)
			sublime.save_settings("InstallToRoku.sublime-settings")

		def on_change(user_input):
			pass

		def on_cancel():
			print "changes not saved"
			
		sublime.Window.show_input_panel(sublime.active_window(), "Roku Developer Username", username, on_done, on_change, on_cancel)

class InstallToRokuSettingsPasswordCommand(sublime_plugin.WindowCommand):
	def run(self):
		settings = sublime.load_settings("InstallToRoku.sublime-settings")
		password = sublime.Settings.get(settings, "roku_password")

		def on_done(user_input):
			sublime.Settings.set(settings, "roku_password", user_input)
			sublime.save_settings("InstallToRoku.sublime-settings")

		def on_change(user_input):
			pass

		def on_cancel():
			print "changes not saved"
			
		sublime.Window.show_input_panel(sublime.active_window(), "Roku Developer Password", password, on_done, on_change, on_cancel)
