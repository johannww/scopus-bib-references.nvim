M = {}

-- TODO: this might be useful in the future
M.opts = {}

M.setup_config = function(opts)
    opts = opts or {}
    M.opts = vim.tbl_deep_extend("force", M.opts, opts)
end

return M
