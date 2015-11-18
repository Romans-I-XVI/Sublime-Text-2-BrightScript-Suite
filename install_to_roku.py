import sublime, sublime_plugin
import sys
import os
import zipfile
import pycurl

class InstallToRokuCommand(sublime_plugin.WindowCommand):
    def run(self, dirs):
		settings = sublime.load_settings("InstallToRoku.sublime-settings")
		username = sublime.Settings.get(settings, "roku_username")
		password = sublime.Settings.get(settings, "roku_password")
		ip = sublime.Settings.get(settings, "roku_ip_address")
		url = "http://"+ip+"/plugin_install"

		folder = dirs[0]
		zipfilename = "%s.zip" % (folder.replace("/", "_"))
		zfile = zipfile.ZipFile("channel.zip", 'w', zipfile.ZIP_DEFLATED)
		rootlen = len(folder) + 1
		for base, dirs, files in os.walk(folder):
		    for file in files:
		        fn = os.path.join(base, file)
		        zfile.write(fn, fn[rootlen:])
		zfile.close()

		curl = pycurl.Curl()
		curl.setopt(pycurl.POST, 1)
		curl.setopt(pycurl.URL, url)
		curl.setopt(pycurl.HTTPPOST, [("mysubmit", "Install"), ("archive", (curl.FORM_FILE, "channel.zip"))])
		curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_DIGEST)
		curl.setopt(pycurl.USERNAME, username)
		curl.setopt(pycurl.PASSWORD, password)
		curl.perform()

		os.remove("channel.zip")

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
