import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from pathlib import Path


class ScanSorterApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.github.scan_sorter")
        self.folder = None
        self.images = []
        self.image_box = None

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

        self.image_box = Gtk.FlowBox()
        self.image_box.set_column_spacing(12)
        self.image_box.set_row_spacing(12)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_vexpand(True)
        scrolled_window.set_child(self.image_box)

        main_box.append(scrolled_window)

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
            self.folder = dialog.select_folder_finish(result)
            path = Path(self.folder.get_path())

            image_extensions = {".jpg", ".jpeg", ".png", ".tiff"}

            self.images = []

            for item in path.iterdir():
                if item.is_file() and item.suffix.lower() in image_extensions:
                    self.images.append(item)
            for image in self.images:
                print(image)

            for image_path in self.images:
                image = Gtk.Image.new_from_file(str(image_path))
                image.set_pixel_size(200)
                self.image_box.append(image)

        except Exception:
            print("No folder selected")

def main() -> int:
    app = ScanSorterApplication()
    return app.run()


if __name__ == "__main__":
    raise SystemExit(main())
