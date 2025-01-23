import sqlite3
import argparse
import sys

def search_tailwind_classes(search_query, num_matches, match_position):
    """
    Search Tailwind class names in the SQLite database.

    :param search_query: The string to search for in class names.
    :param num_matches: The maximum number of matches to return.
    :param match_position: The string indicated match position ('s, 'e', 'any').
    """
    try:
        # Connect to the database
        conn = sqlite3.connect("./lists.db")
        cursor = conn.cursor()

        # Execute parameterized query
        if match_position == 'any':
          search_query = f"%{search_query}%"
        elif match_position == 's':
          search_query = f"{search_query}%"
        elif match_position == 'e':
          search_query = f"%{search_query}"
        limit_clause = "" if num_matches == 0 else f"LIMIT {num_matches}"
        query = f"SELECT class_name FROM tailwind_classes WHERE class_name LIKE ? {limit_clause};"
        cursor.execute(query, (search_query,))

        # Fetch results
        results = cursor.fetchall()

        # Print results
        print(', '.join((result[0] for result in results or [])) or 'No matches found.')

    except sqlite3.Error as e:
        print(f"Database error: {e}", file=sys.stderr)

    finally:
        # Ensure connection is closed
        if conn:
            conn.close()

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Search Tailwind class names in an SQLite database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""",
        epilog="""
~~~~~~~~~~~
plug n play
~~~~~~~~~~~
python twsearch.py "flex" 0 s
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- search for classes matching "flex" / no limit / that start with "flex"
- you will notice class "inline-flex" is excluded (does not start with "flex")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
    )
    parser.add_argument(
        "search_query",
        type=str,
        nargs="?",
        default="",
        help="search query string (default: empty string)"
    )
    parser.add_argument(
        "num_matches",
        type=int,
        nargs="?",
        default=10,
        help="max number of matches to return (default: 10)"
    )
    parser.add_argument(
        "match_position",
        type=str,
        nargs="?",
        choices=["s", "e", "any"],
        default="any",
        help="match from: \"s\" (start), \"e\" (end), \"any\" (anywhere)",
    )

    # Parse arguments
    args = parser.parse_args()

    # Validate num_matches
    if args.num_matches < 0:
        print("Error: num_matches must be zero or greater.", file=sys.stderr)
        sys.exit(1)

    # Call the search function
    search_tailwind_classes(args.search_query, args.num_matches, args.match_position)


if __name__ == "__main__":
    main()

