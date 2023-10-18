from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
root = Builder.load_string("""
<BoxDoubleButton>:
	size_hint:None, None
	size:"200dp", "200dp"
	radius:[30, 30, 30, 30]
	md_bg_color:[0, 220/float(255), 154/float(255), 1]
	orientation:"vertical"
	MDBoxLayout:
		Widget:
		MDIconButton:
			icon:"merge"
			size_hint:None, None
			size:"70dp", "70dp"
			icon_size:"35dp"
			pos_hint:{"center_x":.5, "center_y":.5}
			theme_text_color:"Custom"
			text_color:[0, 0, 0,  1]
		Widget:
	MDBoxLayout:
		Widget:
		MDIconButton:
			icon:"merge"
			size_hint:None, None
			size:"70dp", "70dp"
			icon_size:"35dp"
			pos_hint:{"center_x":.5, "center_y":.5}
			theme_text_color:"Custom"
			text_color:[0, 0, 0,  1]
		Widget:
<BoxButton>:
	size_hint:None, None
	size:"200dp", "200dp"
	radius:[30, 30, 30, 30]
	md_bg_color:[0, 220/float(255), 154/float(255), 1]
	Widget:
	MDIconButton:
		icon:"merge"
		size_hint:None, None
		size:"70dp", "70dp"
		icon_size:"70dp"
		pos_hint:{"center_x":.5, "center_y":.5}
		theme_text_color:"Custom"
		text_color:[0, 0, 0,  1]
	Widget:
<HomeScreen>:
	name:"home_screen"
	MDBoxLayout:
		orientation:"vertical"
		md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
		MDBoxLayout:
			size_hint_y:None
			height:"120dp"
			md_bg_color:[78/float(255), 128/float(255), 128/float(255), 1]
			radius:[0, 0, 30, 30]
		MDBoxLayout:
			orientation:"vertical"
			Widget:
			MDBoxLayout:
				size_hint_y:None
				height:"400dp"
				#orientation:"vertical"
				Widget:
				MDBoxLayout:
					size_hint:None, None
					size:"400dp", "400dp"
					#md_bg_color:[0, 0, 0, 1]
					MDGridLayout:
						spacing:10
						rows:2
						cols:2
						BoxButton:
						BoxButton:
						BoxDoubleButton:
						BoxButton:
				Widget:
			Widget:
			
			
""")
class BoxDoubleButton(MDBoxLayout):
	pass
class BoxButton(MDBoxLayout):
	pass
class HomeScreen(MDScreen):
	pass
class MainScreenManager(ScreenManager):
	pass
class MainApp(MDApp):
	def build(self):
		screen_manager = ScreenManager()
		home_screen = HomeScreen()
		screen_manager.add_widget(home_screen)
		return screen_manager
if __name__ == "__main__":
	MainApp().run()