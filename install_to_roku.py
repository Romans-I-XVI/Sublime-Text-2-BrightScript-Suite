import sublime, sublime_plugin
import sys
import os
import pycurl

class InstallToRokuCommand(sublime_plugin.WindowCommand):
    def run(self, dirs):
    	# sys.path.append(os.path.join(os.path.dirname(__file__), "/home/asojka09/.config/sublime-text-2/Packages/User/pycurl.egg"))
    	# sys.path.remove(os.path.join(os.path.dirname(__file__), "/usr/lib/python2.7/site-packages"))
        if sublime.ok_cancel_dialog("Install To Roku?", "Install"):
			username = "rokudev"
			password = "password"
			url = "192.168.0.43"+"/plugin_install"
			package = "/home/asojka09/Development/Roku/installer-test/package.zip"


			curl = pycurl.Curl()
			curl.setopt(pycurl.POST, 1)
			curl.setopt(pycurl.URL, url)
			curl.setopt(pycurl.HTTPPOST, [("mysubmit", "Install"), ("archive", (curl.FORM_FILE, package))])
			curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_DIGEST)
			curl.setopt(pycurl.USERNAME, username)
			curl.setopt(pycurl.PASSWORD, password)
			curl.perform()

    def is_visible(self, dirs):
        return len(dirs) > 0
