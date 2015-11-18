import sublime, sublime_plugin
import sys
import os
import zipfile
import pycurl

class InstallToRokuCommand(sublime_plugin.WindowCommand):
    def run(self, dirs):
        if sublime.ok_cancel_dialog("Install To Roku?", "Install"):
			folder = dirs[0]
			zipfilename = "%s.zip" % (folder.replace("/", "_"))
			zfile = zipfile.ZipFile("channel.zip", 'w', zipfile.ZIP_DEFLATED)
			rootlen = len(folder) + 1
			for base, dirs, files in os.walk(folder):
			    for file in files:
			        fn = os.path.join(base, file)
			        zfile.write(fn, fn[rootlen:])
			zfile.close()

			username = "rokudev"
			password = "password"
			url = "192.168.1.10"+"/plugin_install"

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
