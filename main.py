# import libraries
from venv import main
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import wikipedia


class Window(Gtk.Window):
    def __init__(self):
        super().__init__(title="Wikipedia")
        self.set_border_width(10)
        self.set_default_size(600, 350)
        hbox = Gtk.Box()
        grid = Gtk.Grid()
        
    
        box_fatter = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        hbox_left = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        hbox.pack_start(box_fatter, True, True, 0)


        self.lbl_query = Gtk.Label()
        self.lbl_query.set_text("Buscar en Wikipedia: ")
        self.lbl_query.set_justify(Gtk.Justification.LEFT)
        hbox_left.pack_start(self.lbl_query, True, True, 0)

        self.query = Gtk.Entry()
        self.query.set_text("")
        hbox_left.pack_start(self.query, True, True, 0)

        
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        grid.attach(scrolledwindow, 0, 1, 10, 1)
        self.textview = Gtk.TextView()
        self.output = self.textview.get_buffer()
        self.output.set_text("Resultado de busqueda....")
        scrolledwindow.add(self.textview)
        

        button = Gtk.Button(label="buscar")
        button.connect("clicked", self.getQuery)
        hbox_left.pack_start(button, True, True, 0)
       
        
        
        box_fatter.pack_start(hbox_left, False, False, 0)
        box_fatter.pack_start(grid, True, True, 0)
        
        self.add(hbox)
        
    
    def getQuery(self,button):
        """
        Get query of wikipedia
        """ 
        wikipedia.set_lang("es")
        query = self.query.get_text()
        if query != "":
            try:
                result = wikipedia.summary(query, sentences=1)
                self.output.set_text("Resultado de busqueda\n"+result)
            except wikipedia.exceptions.PageError as e:
                self.output.set_text("'¡algo salio mal! \n"+str(e))
            except wikipedia.exceptions.DisambiguationError as e:
                self.output.set_text("'¡algo salio mal! \n"+str(e))
        else:
            self.output.set_text("¡campo vacío!\nNo hay resultados")

if __name__ == "__main__":
    win = Window()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()