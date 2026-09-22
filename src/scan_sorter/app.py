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
        window.present()


def main() -> int:
    app = ScanSorterApplication()
    return app.run()


if __name__ == "__main__":
    raise SystemExit(main())
