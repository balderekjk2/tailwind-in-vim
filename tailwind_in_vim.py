from pathlib import Path

home_path = Path.home()
this_dir = Path.cwd()

with open(f"{home_path}/.vimrc", "a") as file:
  vimcmd = f"command! -nargs=* Twref echom system('python {this_dir}/search_tailwind_classes.py <args>')"
  file.write(vimcmd)
