# Automated Scopus Bib References

If you are an academic writer that needs to **QUICKLY** get a bib reference, this plugin is for you!

Scopus Bib References allows you to get the bib reference right at your **clipboard**
without having to manually download it:

https://github.com/user-attachments/assets/e1aa4403-a0cb-4de1-9271-727cef41b754

# Current database support

Scopus, IEEE, ACM, Springer, ScienceDirect, and MDPI

> [!WARNING]
> You might need to use a VPN from your university to use the API.

# Dependencies

- python virtual environment
```bash
pip install virtualenv
```
```bash
sudo apt install python3-venv
```
```bash
sudo pacman -S python-virtualenv
```

# Installation

Lazy:

```lua
{
    "johannww/scopus-bib-references.nvim",
    cmd = { "ScopusBibReference" },
    config = true,
},

```
