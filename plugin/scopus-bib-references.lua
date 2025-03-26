-- create new command for lazy loading
vim.api.nvim_create_user_command("ScopusBibReference",
    function()
        require("scopus-bib-references").scopusBibReference()
    end,
    {}
)

