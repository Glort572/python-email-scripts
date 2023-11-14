# Python scripts to delete (IMAP) e-mails and/or unsubscribe from every newsletter

These Python scripts will help you unsubscribing from newsletters whose **unsubscribe link** is in the message of the chosen e-mail, as well as deleting e-mails.

**_NOTE_** _The scripts work only with the IMAP protocol!_

`python_unsub_script.py` makes you simply unsubscribe from newsletters.

`python_delete_script.py` makes you delete e-mails.

`python_delete_and_unsub_script.py` makes you both unsubscribe from newsletters and delete e-mails.

## How to use them

In short:

- You will have to enter your e-mail username and a password you have to create [here](https://support.google.com/accounts/answer/185833?hl=en&sjid=11205608307902457777-EU).
- `imap.select()` makes you select a folder. Leave it as `imap.select('INBOX')` if you need to perform the operation on the inbox folder. If you want to perform it on another folder, replace `'INBOX'` with something like `'[Gmail]/<folder name>'`.
- To edit the addresses which you want to consider or ignore, go to `imap.search()` and replace or add the criterium/-a and the e-mail addresses.
- To edit the date, do the same as in the case above, although you must keep in mind that you're editing not the e-mail addresses but the date.
___Note:__ the date must be in `DD-MM-YYYY` format and in quotes inside of the string._

Here is a [list](https://www.rfc-editor.org/rfc/rfc3501#section-6.4.4) of available criteria for the last two cases (pages 49 to 54).

## Optional
If you're a mathematician or a maths lover, you surely heard of De Morgan's Laws. Funnily enough, you can use these laws to understand the way you can choose multiple e-mail addresses that you want to be ignored e.g.

`NOT OR FROM user_1@provider.domain FROM user_2@provider.domain` to say that you want to ignore the users number 1 and number 2.

`not (A or B) == (not A) and (not B)`

If you think that I missed something or want to give me some tips, open an issue or contact me via e-mail at glort572@outlook.it .
Happy coding!