from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
root = Builder.load_string("""
<SelectFileScreen>:
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
					size_hint:None, None
					sie:"30dp", "30dp"
					icon_size:"30dp"
					icon:"arrow-left"
					pos_hint:{"center_x":.5, "centery":.05}
				Widget:
		MDBoxLayout:
			orientation:"vertical"
			MDBoxLayout:
				size_hint_y:None
				height:"50dp"
				Widget:
				MDIconButton:
					icon:"undo"
					size_hint:None, None
					size:"40dp", "40dp"
					icon_size:"30dp"
				Widget:
			FileChooserIconView:
		MDBoxLayout:
			size_hint_y:None
			height:"60dp"
			padding:10
			MDBoxLayout: 
				md_bg_color:[0, 0, 0, 1]
				radius:[40, 40, 40, 40]
				MDLabel:
					text:"Next"
					bold:True
					font_size:"18dp"
					text_size:self.size
					halign:"center"
					valign:"middle"
					color:[1, 1, 1, 1]
""")
class SelectFileScreen(MDScreen):
	pass
class App(MDApp):
	def build(self):
		root = SelectFileScreen()
		return root
if __name__  == "__main__":
	App().run()