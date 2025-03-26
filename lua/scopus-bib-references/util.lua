local nvimDataPath = vim.fn.stdpath("data")
local venv_path = nvimDataPath .. "/python-virtenv-scopus"
if vim.loop.os_uname().sysname == 'Windows_NT' then
    venv_path = nvimDataPath .. "\\python-virtenv-scopus"
end

local M = {}

M.venv_source_cmd = ""
M.venv_source_file = ""

M.install_modules = function(requirements_file)
    vim.fn.system(M.venv_source_cmd .. " " .. M.venv_source_file .. " && python3 -c \"import pybliometrics; import bs4; import bibtexparser; import requests\"")
    if vim.v.shell_error == 0 then
        return
    end

    local ret = vim.fn.system(M.venv_source_cmd .. " " .. M.venv_source_file .. "  && pip install -r " .. requirements_file)
    local module_install_status = vim.v.shell_error
    if module_install_status ~= 0 then
        print("error installing modules")
    end
end

M.start_python_venv = function()
    if vim.loop.os_uname().sysname == 'Windows_NT' then
        M.venv_source_cmd = "call"
        M.venv_source_file = venv_path .. "\\Scripts\\activate.bat"
    else
        M.venv_source_cmd = "source"
        M.venv_source_file = venv_path .. "/bin/activate"
    end

    if vim.fn.isdirectory(nvimDataPath .. "/python-virtenv-scopus") == 0 then
        local venv_create_status = os.execute("cd " .. nvimDataPath .. " && python3 -m venv python-virtenv-scopus")
        if venv_create_status ~= 0 then
            print("python venv create error")
        end
    end
end

M.call_venv_python = function(python_args)
    local output = ""
    output = vim.fn.system(M.venv_source_cmd .. " " .. M.venv_source_file .. " && python3 " .. python_args)
    return output
end

return M
