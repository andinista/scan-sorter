import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class ScanSorterApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.github.scan_sorter")

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self)
        window.set_title("Scan Sorter")
        window.set_default_size(900, 600)

        main_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=12,
        )

        main_box.set_margin_top(12)
        main_box.set_margin_bottom(12)
        main_box.set_margin_start(12)
        main_box.set_margin_end(12)

        open_button = Gtk.Button(label="Open Folder")
        open_button.set_halign(Gtk.Align.START)
        open_button.connect("clicked", self.on_open_folder_clicked)

        main_box.append(open_button)
        window.set_child(main_box)

        window.present()

    def on_open_folder_clicked(self, button):
        dialog = Gtk.FileDialog()
        dialog.set_title("Choose a folder")

        dialog.select_folder(
            parent=self.get_active_window(),
            cancellable=None,
            callback=self.on_folder_selected,
        )

    def on_folder_selected(self, dialog, result):
        try:
            folder = dialog.select_folder_finish(result)
            print(folder.get_path())
        except Exception:
            print("No folder selected")

def main() -> int:
    app = ScanSorterApplication()
    return app.run()


if __name__ == "__main__":
    raise SystemExit(main())
