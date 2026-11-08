--!strict
-- No gameplay/UI is installed yet. Preserve the Roblox default camera and controls.
local Players = game:GetService("Players")
local player = Players.LocalPlayer
assert(player ~= nil, "Client must have LocalPlayer")
