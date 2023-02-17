# 4th class - Command Line

1. **Print "hello world" on the terminal in a single command.**

`echo hello world`

---

2. **Print the current working directory.**

`echo $PWD`

---

3. **List names of all the files in the current directory, one file per line.**

`ls -l`

---

4. **There is a file named access.log in the current directory. Print the contents.**

`cat access.log`

---

5. **Print the last 5 lines of "access.log".**

`tail -5 access.log`

---

6. **Create an empty file named take-the-command-challenge in the current working directory.**

`touch take-the-command-challenge`

---

7. **Create a directory named tmp/files in the current working directory**

`mkdir tmp/ touch tmp/files`

---

8. **Copy the file named take-the-command-challenge to the directory tmp/files**

`cp take-the-command-challenge tmp/files`

---

9. **Move the file named take-the-command-challenge to the directory tmp/files**

`mv take-the-command-challenge tmp/files`

---

10. **Create a symbolic link named take-the-command-challenge that points to the file tmp/files/take-the-command-challenge.**

`ln -s tmp/files/take-the-command-challenge take-the-command-challenge`

- `ln` = link
- `-s` = symbolic
- `tmp/files/take-the-command-challenge` = where the symbolic file is meant to point
- `take-the-command-challenge`= name of the symbolic file

---

11. **Delete all of the files in this challenge directory including all subdirectories and their contents.**

`rm -rf * .*`

- `rm` = remove
- `-rf` =

  1. `-r` = Attempt to remove the file hierarchy rooted in each file argument. The -R option implies the -d option.

     - `-d`= Attempt to remove directories as well as other types of files.

  2. `-f` = Attempt to remove the files without prompting for confirmation, regardless of the file's permissions. If the file does not exist, do not display a diagnostic message or modify the exit status to reflect an error. The -f option overrides any previous -i options.

     - `-i` = Request confirmation before attempting to remove each file, regardless of the file's permissions, or whether the standard input device is a terminal. If the response from the standard input begins with the first character for the YES response in the current locale, the file is removed. The -i option overrides any previous -f options.

> **Note**: `-f` and `-i` override each other.

- `*` = all files
- `.*` = all hidden files

---

12. **Remove all files with the .doc extension recursively in the current working directory.**

`rm -rf **/*.doc`

- `rm` = remove
- `rf`=

  1. `-r` = Attempt to remove the file hierarchy rooted in each file argument. The -R option implies the -d option.

     - `-d`= Attempt to remove directories as well as other types of files.

  2. `-f` = Attempt to remove the files without prompting for confirmation, regardless of the file's permissions. If the file does not exist, do not display a diagnostic message or modify the exit status to reflect an error. The -f option overrides any previous -i options.

     - `-i` = Request confirmation before attempting to remove each file, regardless of the file's permissions, or whether the standard input device is a terminal. If the response from the standard input begins with the first character for the YES response in the current locale, the file is removed. The -i option overrides any previous -f options.

> **Note**: `-f` and `-i` override each other.

- `**/` = current working directory
- `*.doc` = all files with the `.doc` extension

---

13. **There is a file named access.log in the current working directory. Print all lines in this file that contains the string "GET".**

`grep 'GET' access.log`

- `grep` = Searches for a string of characters in a specified file. The text search pattern is called a regular expression. When it finds a match, it prints the line with the result.

- `'GET'` = The regular expression to be searched for.

- `access.log` = The file to be searched within.

---

14. **Print all files in the current directory, one per line (not the path, just the filename) that contain the string "500".**

`grep -l '500' *`

- `grep` = Searches for a string of characters in a specified file. The text search pattern is called a regular expression. When it finds a match, it prints the line with the result.

- `-l` = "Long" version of the list of files (with more details).

- `'500'` = The regular expression to be searched for.

- `*` = current directory 🤔

---

15. **Print the relative file paths, one path per line for all filenames that start with "access.log" in the current directory.**

`ls access.log*`

- `ls` = Lists all files in the current directory except for hidden files.

- `access.log*`= all files starting with 'access.log'

---

16. **Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log" that contain the string "500".**

`grep -rh "500" **/access.log*` 🤔

- `grep` = Searches for a string of characters in a specified file. The text search pattern is called a regular expression. When it finds a match, it prints the line with the result.

- `-r` = [RECURSIVELY] Searches also in subdirectories of the specified filepattern.

- `h` = [HELP - also `--help`] To automatically get generated help text for the command-line program.

- `"500"` = the string being looked for.

- `**/` = "under the current directory"

- `access.log*` = all files starting with "access.log"

---

17. **Extract all IP addresses from files that start with "access.log" printing one IP address per line.**

- `grep -ro ^[0-9.]*` 😱

---

18. **Count the number of files in the current working directory. Print the number of files as a single integer.**

`ls -l | wc -l`

- `ls` = Lists all files in the current directory except for hidden files.

- `-l` = "Long" version of the list of files (with more details).

- `|` = The pipe operator directs the output of the preceding command as input to the succeeding command. It is most commonly used to filter data with the `grep` command.

- `wc` = Counts words and provides a summary of what is found.

- `-l` = "Long" version of the list of files (with more details).

---

19. **Print the contents of access.log sorted.**

`sort access.log`

- `sort` = Sorts a file, arranging the records in a particular order. By default, the sort command sorts file assuming the contents are ASCII. Using options in the sort command can also be used to sort numerically. More info at [https://www.geeksforgeeks.org/sort-command-linuxunix-examples/]

- `access.log` = the file whose content which we want to sort.

---

20. **Delete all the content of a directory without deleting the directory itself**

`rm -r foldername/*`

- `rm`: remove

- `-r`: recursively

- `foldername/*`: everything (`*`) within `foldername`
