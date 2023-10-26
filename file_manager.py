from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.filechooser import FileChooserIconView
from touch import TouchBox
from kivy.lang import Builder
root = Builder.load_string("""
<SelectFileScreen>:
	id:select_file_screen
	name:"select_file_screen"
	MDBoxLayout:
		md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"120dp"
			radius:[0, 0, 30, 30]
			md_bg_color:[78/float(255), 128/float(255), 128/float(255), 1]
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
				orientation:"vertical"
				Widget:
				MDIconButton:
					root:select_file_screen
					size_hint:None, None
					size:"50dp", "50dp"
					icon:"arrow-left"
					pos_hint:{"center_x":.5, "center_y":.5}
					icon_size:"30dp"
					theme_text_color:"Custom"
					text_color:[1, 1, 1, 1]
					on_press:root.goBackToHomeScreen()
				Widget:
			MDBoxLayout:
				MDLabel:
					text:"File System"
					font_size:"18dp"
					text_size:self.size
					halign:"center"
					valign:"middle"
					color:[1, 1, 1, 1]
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
		MDBoxLayout:
			MyFiles:
				id:files_layout
		MDBoxLayout:
			size_hint_y:None
			height:"60dp"
			padding:10
			NextButton: 
				root:select_file_screen
				md_bg_color:[0, 154/float(255), 220/float(255), 1]
				radius:[40, 40, 40, 40]
				MDLabel:
					text:"Next"
					font_size:"18dp"
					text_size:self.size
					halign:"center"
					valign:"middle"
					color:[1, 1, 1, 1]
""")
class NextButton(TouchBox):
	def respondToTouch(self):
		if len(self.root.ids.files_layout.selection) >= 1:
			pass
class MyFiles(FileChooserIconView):
	pass
class SelectFileScreen(MDScreen):
	def goBackToHomeScreen(self):
		self.parent.transition = SlideTransition(direction = "right")
		self.parent.current = "home_screen"
class App(MDApp):
	def build(self):
		root = SelectFileScreen()
		return root
if __name__  == "__main__":
	App().run()