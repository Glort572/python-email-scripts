# Python scripts to delete (IMAP) e-mails and/or unsubscribe from every newsletter

These Python scripts are designed to help you unsubscribe from newsletters containing an **unsubscribe link** in the e-mail message, as well as delete e-mails.

**_Note:_** _These scripts only work with the IMAP protocol!_

- `python_unsub_script.py` allows you to unsubscribe from newsletters.
- `python_delete_script.py` allows you to delete e-mails.
- `python_delete_and_unsub_script.py` allows you to both unsubscribe from newsletters and delete e-mails.

## How to Use

In brief:

1. Enter your e-mail username and a password that you create [here](https://support.google.com/accounts/answer/185833?hl=en&sjid=11205608307902457777-EU).
2. Use `imap.select()` to choose a folder. Leave it as `imap.select('INBOX')` for the inbox folder. To perform operations on another folder, replace `'INBOX'` with something like `'[Gmail]/<folder name>'`.
3. Edit the addresses you want to consider or ignore in `imap.search()` by replacing or adding criteria and e-mail addresses.
4. To edit the date, follow the same steps as above, keeping in mind that you're modifying the date, not the e-mail addresses. The date must be in `DD-MM-YYYY` format and enclosed in quotes within the string.

Here is a [list](https://www.rfc-editor.org/rfc/rfc3501#section-6.4.4) of available criteria for the last two cases (pages 49 to 54).

## Optional

If you're a mathematician or are keen on maths, you may be familiar with **[De Morgan's Laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws)**. Interestingly, you can use these laws to understand how to choose multiple e-mail addresses to be ignored, e.g.,

```plaintext
NOT OR FROM user_1@provider.domain FROM user_2@provider.domain
```
This means you want to ignore users number 1 and number 2.

```plaintext
not (A or B) == (not A) and (not B)
```

If you think I missed something or want to provide tips, open an issue or contact me via e-mail at glort572@outlook.it .

Happy coding!
