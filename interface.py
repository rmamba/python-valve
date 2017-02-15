#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import valve.rcon
import valve.source.a2s

class gui(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Server Manager")

		self.grid = Gtk.Grid(orientation=Gtk.Orientation.VERTICAL)
		self.add(self.grid)

		box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		self.grid.attach(box1, 0, 0, 1, 1)

		lbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
		box1.pack_start(lbox1, True, True, 0)
		box1.pack_start(box, True, True, 0)

		label1 = Gtk.Label("IP")
		label2 = Gtk.Label("Port")
		label3 = Gtk.Label("RCON password")
		label4 = Gtk.Label("")

		lbox1.pack_start(label1, True, False, 1)
		lbox1.pack_start(label2, True, False, 1)
		lbox1.pack_start(label3, True, False, 1)
		lbox1.pack_start(label4, True, False, 1)

		self.IPentry = Gtk.Entry()
		box.pack_start(self.IPentry, True, False, 1)


		self.Portentry = Gtk.Entry()
		box.pack_start(self.Portentry, True, False, 1)

		self.RCONentry = Gtk.Entry()
		box.pack_start(self.RCONentry, True, False, 1)	

		self.Okbutton = Gtk.Button(label="Ok")
		self.Okbutton.connect("clicked", self.getinfo)
		box.pack_start(self.Okbutton, True, False, 1)

		box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		self.grid.attach(box2, 0, 1, 1, 1)
		lbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
		box2.pack_start(lbox2, True, False, 1)
		rbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
		box2.pack_start(rbox2, True, False, 1)

		
		label1 = Gtk.Label("Name")
		label2 = Gtk.Label("Players")
		label3 = Gtk.Label("Platform")
		label4 = Gtk.Label("Map")

		lbox2.pack_start(label1, True, False, 1)
		lbox2.pack_start(label2, True, False, 1)
		lbox2.pack_start(label3, True, False, 1)
		lbox2.pack_start(label4, True, False, 1)

		self.namentry = Gtk.Entry()
		self.namentry.set_editable(False)
		self.playentry = Gtk.Entry()
		self.playentry.set_editable(False)
		self.platentry = Gtk.Entry()
		self.platentry.set_editable(False)
		self.pingentry = Gtk.Entry()
		self.pingentry.set_editable(False)

		rbox2.pack_start(self.namentry, True, False, 1)
		rbox2.pack_start(self.playentry, True, False, 1)
		rbox2.pack_start(self.platentry, True, False, 1)
		rbox2.pack_start(self.pingentry, True, False, 1)

		box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
		self.grid.attach(box3, 0, 2, 2, 1)
		
		self.commentry = Gtk.Entry()
		self.commButton = Gtk.Button(label="Send")
		self.commButton.connect("clicked", self.execRCON)
		box3.pack_start(self.commentry, True, True, 1)
		box3.pack_start(self.commButton, True, True, 1)
		
	def getinfo(self, widget):
		self.servIP = self.IPentry.get_text()
		self.servPort = self.Portentry.get_text()
		servRCON = self.RCONentry.get_text()
		self.servPort = int(self.servPort)
		self.SERVER_ADDRESS = (self.servIP, self.servPort)
		self.RCON = servRCON

		server = valve.source.a2s.ServerQuerier(self.SERVER_ADDRESS)
		self.servname = server.info()["server_name"]
		self.players = "{player_count}/{max_players}".format(**server.info())
		self.platform = server.info()["platform"]
		self.ping = server.info()["map"]
		self.players = str(self.players)
		self.platform = str(self.platform)
		
		namelen = len(self.servname)
		self.namentry.set_width_chars(namelen)
		self.namentry.set_text(self.servname)
		self.playentry.set_text(self.players)
		self.platentry.set_text(self.platform)

	def execRCON(self, widget):
		command = self.commentry.get_text()
		valve.rcon.execute(self.SERVER_ADDRESS, self.RCON, command)

	

window = gui()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
