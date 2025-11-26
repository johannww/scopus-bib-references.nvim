M = {}

local util = require("scopus-bib-references.util")
local config = require("scopus-bib-references.config")
local pythonScriptDir = debug.getinfo(1, "S").source:sub(2):gsub("lua/scopus%-bib%-references/init%.lua", "")

M.scopusBibReference = function()
    local article_url = vim.fn.input("Enter the article url: ")
    local output = ""
    if vim.loop.os_uname().sysname == 'Windows_NT' then
        output = util.call_venv_python(pythonScriptDir .. "\\scripts\\scopus_reference.py" .. " \"" .. article_url .. "\"")
    else
        output = util.call_venv_python(pythonScriptDir .. "/scripts/scopus_reference.py" .. " '" .. article_url .. "'")
    end

    if output == "" then
        print("No reference found")
    else
        vim.fn.setreg('"', output)
    end
end

M.setup = function(opts)
    vim.fn.system("python -c \"import venv\"")
    if vim.v.shell_error ~= 0 then
        error("install python venv module before loading scopus-bib-references")
        return
    end

    config.setup_config(opts)
    util.start_python_venv()

    local requirements_file = debug.getinfo(1, "S").source:sub(2):gsub("lua/scopus%-bib%-references/init%.lua", "requirements.txt")
    util.install_modules(requirements_file)
    util.init_pybliometrics_config(pythonScriptDir)
end

return M

