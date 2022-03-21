from simple_term_menu import TerminalMenu
from download_file import get_file_io

from list_files import get_files
from simple_term_menu import TerminalMenu
import polars as pl


def main():
    files = get_files()
    print("Select file to download:\n\n")
    terminal_menu = TerminalMenu([file.get("name") for file in files])
    menu_entry_index = terminal_menu.show()
    file_id = files[menu_entry_index].get("id")
    mime_type = files[menu_entry_index].get("mimeType")
    buf = get_file_io(file_id, mime_type)
    df = pl.read_csv(buf, ignore_errors=True)
    print(df)


if __name__ == '__main__':
    main()
