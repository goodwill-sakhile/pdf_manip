from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder 
root  = Builder.load_string("""
<MainPDFManipBox>:
	orientation:"vertical"
	md_bg_color:[255/float(255), 255/float(255), 0, 1]
	MDBoxLayout:
		size_hint_y:None
		height:"100dp"
		md_bg_color:[0, 0, 0, 1]
		radius:[0, 0, 50, 0]
		padding:[15, 0, 0, 0]
		MDLabel:
			text:"_pdf_manip/"
			text_size:self.size
			halign:"left"
			valign:"middle"
			color:[1, 1, 1, 1]
			font_size:"30dp"
	MDBoxLayout:
		md_bg_color:[0, 0, 0, 1]
		MDBoxLayout:
			orientation:"vertical"
			md_bg_color:[255/float(255), 255/float(255), 0, 1]
			radius:[50, 0, 0, 0]
			padding:10
			spacing:10
			MDBoxLayout:
				spacing:10
				MDBoxLayout:
					md_bg_color:[0, 0, 0, 1]
					radius:[30, 0, 30, 0]
					orientation:"vertical"
					MDBoxLayout:
					MDBoxLayout:
						size_hint_y:None
						height:"50dp"
						MDLabel:
							text:"<_merge_pdf's>"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:[1, 1, 1, 1]
				MDBoxLayout:
					md_bg_color:[0, 0, 0, 1]
					radius:[30, 0, 30, 0]
					orientation:"vertical"
					MDBoxLayout:
						Widget:
						MDIconButton:
							size_hint:None, None
							size:"100dp", "100dp"
							icon_size:"50dp"
							user_font_size:"100dp"
							theme_text_color:"Custom"
							text_color:[1, 1, 1, 1]
							icon:"file-lock"
							pos_hint:{"center_x":.5, "center_y":.5}
						Widget:
					MDBoxLayout:
						size_hint_y:None
						height:"50dp"
						MDLabel:
							text:"<_encryp_pdf's>"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:[1, 1, 1, 1]
			MDBoxLayout:
				spacing:10
				MDBoxLayout:
					md_bg_color:[0, 0, 0, 1]
					radius:[30, 0, 30, 0]
					MDBoxLayout:
						size_hint_y:None
						height:"50dp"
						MDLabel:
							text:"<_compress_pdf's>"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:[1, 1, 1, 1]
				MDBoxLayout:
					md_bg_color:[0, 0, 0, 1]
					radius:[30, 0, 30, 0]
					MDBoxLayout:
						size_hint_y:None
						height:"50dp"
						MDLabel:
							text:"<_pdf's_to_image's>"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:[1, 1, 1, 1]
""")
class MainPDFManipBox(MDBoxLayout):
	pass
class MainApp(MDApp):
	def build(self):
		root = MainPDFManipBox()
		return root
if __name__ == "__main__":
	MainApp().run()