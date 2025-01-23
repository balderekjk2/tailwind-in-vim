# tailwind-in-vim

## Preliminary assumptions

1. You have Python 3 installed on your system. See official downloads [here](https://www.python.org/downloads/).
   - In a shell type `python --version`
   - If you see `Python 3.x.x`, you have Python 3 installed
2. You have vim installed.

## Getting started

1. Download and extract zip from [GH repo](https://github.com/balderekjk2/tailwind-in-vim) OR `git clone https://github.com/balderekjk2/tailwind-in-vim.git` in desired directory.
2. Shell into that directory.
3. Copy and paste the following into your shell, then hit Enter:
   
   ```console
   python seed_tailwind_classes_table_at_lists_db.py && python tailwind_in_vim.py
   ```

   You will only ever need to run this one time, so feel free to (re)move these scripts after execution.
4. Open up vim and type :Twref
   - You should see `aspect-auto, aspect-video, aspect-square, container, mx-auto, max-width, min-width, columns-1, columns-2, columns-3^@`

## Post-setup usage

```console
usage: search_tailwind_classes.py [-h] [search_query] [num_matches] [{s,e,any}]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Search Tailwind class names in an SQLite database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

positional arguments:
  search_query  search query string (default: empty string)
  num_matches   max number of matches to return (default: 10)
  {s,e,any}     match from: "s" (start), "e" (end), "any" (anywhere)

optional arguments:
  -h, --help    show this help message and exit

~~~~~~~~~~
plug n play
~~~~~~~~~~
python twsearch.py "flex" 0 s
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- search for classes matching "flex" / no limit / that start with "flex"
- you will notice class "inline-flex" is excluded (does not start with "flex")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

To see the help screen any time run `python search_tailwind_classes.py -h` or in vim `:Twref -h`
